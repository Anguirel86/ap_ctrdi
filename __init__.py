from __future__ import annotations

import base64
import hashlib
import logging
import os
import pickle
import random
import sys
import typing
from pathlib import Path

# Add the ctrando lib to sys path
base_path = Path(__file__).resolve().parent
lib_path = base_path / "lib"
sys.path.append(str(lib_path))

# RDI randomizer imports
from ctrando import randomizer
from ctrando.arguments import arguments, argumenttypes, tomloptions
from ctrando.base import multiworld
from ctrando.common import ctenums, ctrom, randostate
from ctrando.common.ctenums import ItemID
from ctrando.strings import ctstrings
from ctrando.treasures import treasuretypes as tty

# Archipelago imports
import settings
import worlds
from BaseClasses import CollectionState, Item, ItemClassification, Location, MultiWorld, Tutorial
from Options import Choice, FreeText, OptionList, Range, Toggle
from Utils import read_snes_rom
from worlds.AutoWorld import WebWorld, World

# Local APWorld imports
from . import items, locations
from .client import CTRDIClient  # noqa: F401  # pyright: ignore[reportUnusedImport]
from .options import CTRDIOptions, option_groups

rdi_logger = logging.getLogger("RDI")

CTUSA_MD5_HASH:str = "a2bc447961e52fd2227baed164f729dc"
RDI_NAME = "Chrono Trigger Rando-Dalton Imperial"


@typing.final
class CTRDIPatch(worlds.Files.APProcedurePatch):
    """
    Patch file definition for RDI.
    """
    hash = CTUSA_MD5_HASH
    game = RDI_NAME
    patch_file_ending: str = ".apctrdi"

    procedure:typing.ClassVar[list] = [
        ("apply_rdi_patch", []),
    ]

    @typing.override
    @classmethod
    def get_source_data(cls) -> bytes:
        return CTRDIWorld.get_base_rom_bytes()

@typing.final
class RDIPatchExtension(worlds.Files.APPatchExtension):
    """
    Patch extension class to apply the RDI patch on the client machine.
    """
    game = RDI_NAME

    @staticmethod
    def apply_rdi_patch(caller: CTRDIPatch, rom: bytes) -> bytes:
        patch_dict = pickle.loads(caller.get_file("patch_data.pickle"))
        rng = random.Random()
        rng.seed(patch_dict["rdi_reseed"], version=2)

        ct_rom = ctrom.CTRom(rom)
        config = randomizer.get_random_config(
            patch_dict["settings"],
            patch_dict["romless_config"],
            ct_rom,
            rng)

        out_rom = randomizer.get_ctrom_from_config(
            ct_rom, patch_dict["settings"], config)

        multiworld.write_player_validation_data(out_rom, patch_dict["hashed_name"])
        return bytes(out_rom.getbuffer())

@typing.final
class CTRDISettings(settings.Group):
    @typing.final
    class RomFile(settings.SNESRomPath):
        """File name of the CT ROM"""
        description = "Chrono Trigger (USA) ROM"
        copy_to = "Chrono Trigger (USA).sfc"
        md5s = [CTRDIPatch.hash]  # noqa: RUF012  # pyright: ignore[reportAssignmentType]

    rom_file: RomFile = RomFile(RomFile.copy_to)

@typing.final
class CTRDIWebWorld(WebWorld):
    tutorials = [Tutorial(  # noqa: RUF012
        "Multiworld Setup Guide",
        "Setup guide for CTRDI multiworld",
        "English",
        "multiworld_en.md",
        "multiworld/en",
        ["Pseudoarc", "Anguirel"]
    )]
    option_groups = option_groups

@typing.final
class CTRDIWorld(World):
    """
    Rando-Dalton Imperial is a highly customizable open world randomizer for
    the SNES version of Chrono Trigger. It focuses on retaining as much of
    the vanilla experience as possible but offers a wide array of options
    to allow the player to tailor their play experience however they want.
    """
    game = RDI_NAME
    topology_present = True
    origin_region_name = "starting_rewards"
    options_dataclass = CTRDIOptions
    Options: CTRDIOptions  # pyright: ignore[reportUninitializedInstanceVariable]
    settings_key = "ctrdi_options"
    settings: typing.ClassVar[CTRDISettings]  # pyright: ignore[reportIncompatibleVariableOverride]

    web = CTRDIWebWorld()

    rdi_settings: arguments.Settings
    romless_config: randostate.RomlessConfigState

    location_name_to_id = locations.location_name_to_id
    item_name_to_id = items.item_name_to_id

    hashed_name: bytes
    encoded_name: str
    rdi_reseed: int


    def __init__(self, world: MultiWorld, player: int):
        super().__init__(world, player)
        self.ds_replacements: dict[int, int] = {}

    @typing.override
    def generate_early(self):
        """
        Set up the RDI settings/config objects that will be used
        in subsequent stages to create items/regions/etc for the multiworld.
        """
        player_name = self.multiworld.player_name[self.player]
        self.hashed_name = hash(player_name).to_bytes(8, signed=True)
        self.encoded_name = base64.b64encode(self.hashed_name).decode()

        self._translate_settings()
        self.romless_config = randomizer.get_random_romless_config(self.rdi_settings, self.multiworld.random)
        self.ds_replacements = items.get_ds_replacement_map(self.romless_config)

        # This value will be used to reseed the RDI random number generator for any additional
        # randomness needed when applying the patch on the client side.
        self.rdi_reseed = self.multiworld.random.getrandbits(64)

    @typing.override
    def create_item(self, name: str) -> Item:
        """
        Create an AP item from the named RDI item.
        """
        return items.create_item_from_name(name, self.player)

    @typing.override
    def create_items(self) -> None:
        """
        Create the multiworld items for this player
        """
        self.multiworld.itempool += items.create_items(
            self.romless_config, self.player, self.ds_replacements)

    @typing.override
    def create_regions(self) -> None:
        """
        Create regions and locations for this player
        """
        # Create regions and connecting exits
        region_dict = locations.create_region_map(self.romless_config, self.multiworld, self.player)

        # Create treasure locations and game/logic event locations
        locations.create_locations_for_regions(
            region_dict, self.romless_config, self.rdi_settings, items.key_item_list, self.player)
        locations.create_recruit_events(region_dict, self.romless_config, self.player)
        locations.create_flag_events(region_dict, self.romless_config, self.player)

        # Create victory location
        menu_region = region_dict[self.origin_region_name].ap_region
        victory_loc = Location(self.player, "Victory", None, menu_region)
        victory_loc.place_locked_item(
            Item("Victory", ItemClassification.progression, None, self.player))
        victory_loc.access_rule = locations.create_victory_rule(self.player, self.rdi_settings)
        menu_region.locations.append(victory_loc)
        self.multiworld.completion_condition[self.player] = \
            lambda state: state.has("Victory", self.player)

        # Add all regions to the multiworld object
        self.multiworld.regions += [x.ap_region for x in region_dict.values()]

    @typing.override
    def get_filler_item_name(self) -> str:
        """
        Get a random filler item
        """
        # TODO: Real filler items - Ideally this will never be needed
        return str(ctenums.ItemID.MOP)

    @typing.override
    def modify_multidata(self, multidata):  # pyright: ignore[reportMissingParameterType]
        player_name = self.multiworld.player_name[self.player]
        multidata["connect_names"][self.encoded_name] = multidata["connect_names"][player_name]

    @typing.override
    def fill_slot_data(self) -> dict[str, typing.Any]:
        """
        Fill slot data for the client and tracker
        This includes the items that have been replaced by DS variants so that
        the client can report and deliver the correct item.
        """
        slot_data: dict[str, typing.Any] = {}
        slot_data["ds_replacements"] = self.ds_replacements
        return slot_data

    @typing.override
    def generate_output(self, output_directory: str):
        """
        Create the patch file for this game.
        """
        # Rewrite the treasure dictionary to handle local vs AP items
        self._modify_rom_treasures()

        # Create the patch file with the necessary data to create the ROM
        patch = CTRDIPatch()
        basename = self.multiworld.get_out_file_name_base(self.player)
        output_path = os.path.join(output_directory, f"{basename}{patch.patch_file_ending}")

        patch_data: dict = {
            "hashed_name": self.hashed_name,
            "settings": self.rdi_settings,
            "romless_config": self.romless_config,
            "rdi_reseed": self.rdi_reseed
        }
        patch.write_file("patch_data.pickle", pickle.dumps(patch_data))
        patch.write(output_path)

    @typing.override
    def collect_item(self, state: CollectionState, item: Item, remove: bool=False) -> str | None:
        return items.collect_item(state, item, remove)

    def _convert_setting_value(self, flag_name: str, spec):
        """
        Convert a value from an AP option type for use in an RDI settings dictionary
        """
        value = getattr(self.options, flag_name)  # pyright: ignore[reportAny]
        if isinstance(value, Choice):
            value = value.name_lookup[value.value]
        elif isinstance(value, Toggle):
            value = value.value == 1
        elif isinstance(value, Range):
            value = value.value
            if hasattr(spec, "type_fn") and spec.type_fn is not int:
                value = float(value / 100.0)
        elif isinstance(value, OptionList):
            value = value.value
        elif isinstance(value, FreeText):
            value = value.value
        else:
            raise Exception(f"Unknown argument type for {flag_name}")

        return value

    def _parse_group_spec(self, group_spec, data_dict):
        """
        Handle parsing options for the given group spec.
        """
        for flag_name, spec in group_spec.items():
            if isinstance(spec, dict):
                self._parse_group_spec(spec, data_dict)
            else:
                if hasattr(self.options, flag_name):
                    value = self._convert_setting_value(flag_name, spec)
                    if isinstance(spec, argumenttypes.StringArgument) and value == "":
                        # Skip string fields with no data
                        continue

                    if isinstance(spec, argumenttypes.DistArgument) and not value:
                        # Skip empty distribution args
                        continue

                    if isinstance(spec, argumenttypes.DiscreteCategorialArg):
                        # NOTE: This is a hack to get around the AP choice types reserving "random"
                        if value == "rdi_random":
                            value = "random"

                        # Handle character plando's "..." value, which breaks
                        # the option naming in choice types.
                        if value == "char_any":
                            value = "..."

                        # The ending selector flag contains strings that do not translate well
                        # into AP options. We sanitize them when creating the options object
                        # and have to convert them back to real values here.
                        if flag_name == "ending":
                            ending_num = getattr(self.options, flag_name).value  # pyright: ignore[reportAny]
                            value = spec.choices[ending_num]

                    data_dict[flag_name] = value

    def _translate_settings(self):
        """
        Set up a randomizer Settings object with the user's chosen AP options
        """
        # Parse options and convert them to something RDI can use
        data_dict = {}
        group_specs = arguments.Settings.get_argument_spec()
        for group_spec in group_specs.values():
            self._parse_group_spec(group_spec, data_dict)

        # TODO: Trading post spots will have flags soon,
        #       so this is just a temp fix to remove them
        #       while they are causing issues.
        import ctrando.arguments.arguments
        arg_specs = ctrando.arguments.arguments.Settings.get_argument_spec()
        spec = arg_specs["logic_options"]["excluded_spots"]  # pyright: ignore[reportIndexIssue]
        for loc in locations.locs_to_skip:
            data_dict["excluded_spots"].append(spec.str_from_choice_fn(loc))  # pyright: ignore[reportAttributeAccessIssue]

        # Enable multiworld support in the randomizer
        data_dict["general_options"] = {}
        data_dict["general_options"]["multiworld"] = True

        args = tomloptions.toml_data_to_args(data_dict)
        self.rdi_settings = randomizer.extract_settings(*args)

    def _modify_rom_treasures(self):
        """
        Write treasure data back to the config.

        The initial config gives us our items, but AP shuffles them around.
        Write the items back to the ROM, treating local items as local and remote
        items as a custom reward type.
        """
        filled = self.multiworld.get_filled_locations(self.player)
        for loc in filled:

            if loc.address is None:
                # Skip event locations
                continue

            # Sanity checks to make PyRight happy
            # get_filled_locations should already filter these out
            if loc.item is None or loc.item.code is None:
                continue

            is_local = loc.item.player == self.player
            tid = locations.get_tid_from_address(loc.address)

            if is_local:
                # Replace the reward here with whatever AP chose.
                # TODO: Character items (not implmenented in base randomizer yet)
                if items.is_tech_level_reward(loc.item.code):
                    char_id = items.convert_to_char_id(loc.item.code)
                    self.romless_config.treasure_assignment[tid] = tty.TechLevelReward(char_id)
                else:

                    if items.is_ds_item_reward(loc.item.code):
                        # Convert from the DS item to the base item it replaced
                        item_id = ItemID(self.ds_replacements[loc.item.code] - items.ITEM_ID_BASE)
                    elif items.is_progressive_item_reward(loc.item.code):
                        # Replace progressive items with their base item and let
                        # the ROM side handle the upgrade.
                        item_id = items.get_base_progressive_item(loc.item.code)
                    else:
                        item_id = items.item_name_to_rdi_type[loc.item.name]


                    self.romless_config.treasure_assignment[tid] = item_id
            else:
                # Replace reward here with the AP treasure type
                item_name = ctstrings.pre_process_string(loc.item.name)
                player_name = ctstrings.pre_process_string(self.multiworld.player_name[loc.item.player])
                self.romless_config.treasure_assignment[tid] = tty.APReward(item_name, player_name)

    @staticmethod
    def get_rom_path() -> str:
        """
        Get the path to the Chrono Trigger ROM
        """
        file_name = CTRDIWorld.settings.rom_file

        if not os.path.exists(file_name):
            raise ValueError("No Chrono Trigger ROM specified")

        return file_name

    @staticmethod
    def get_base_rom_bytes(file_name: str = "") -> bytes:
        """
        Get the base ROM data as a bytes object
        """
        base_rom_bytes = getattr(
            CTRDIWorld.get_base_rom_bytes, "base_rom_bytes", None)
        if not base_rom_bytes:
            file_name = CTRDIWorld.get_rom_path()
            base_rom_bytes = bytes(read_snes_rom(open(file_name, "rb")))

            basemd5 = hashlib.md5()
            basemd5.update(base_rom_bytes)
            if basemd5.hexdigest() != CTUSA_MD5_HASH:
                raise ValueError(
                    "Supplied base ROM does not match the known MD5 hash")

            CTRDIWorld.get_base_rom_bytes.base_rom_bytes = base_rom_bytes  # pyright: ignore[reportFunctionMemberAccess]

        return base_rom_bytes
