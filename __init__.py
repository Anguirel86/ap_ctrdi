from __future__ import annotations

import base64
import hashlib
import logging
import os
import typing

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
from BaseClasses import Item, ItemClassification, Location, MultiWorld, Tutorial
from Options import Choice, FreeText, OptionList, Range, Toggle
from Utils import read_snes_rom
from worlds.AutoWorld import WebWorld, World

# Local APWorld imports
from . import Items, Locations
from .Client import CTRDIClient  # noqa: F401  # pyright: ignore[reportUnusedImport]
from .Options import CTRDIOptions, option_groups

# TODO task list:
#  - Create tutorial docs


rdi_logger = logging.getLogger("RDI")

CTUSA_MD5_HASH = "a2bc447961e52fd2227baed164f729dc"


@typing.final
class CTRDIDeltaPatch(worlds.Files.APDeltaPatch):
    hash = CTUSA_MD5_HASH
    game = "Chrono Trigger Rando-Dalton Imperial"
    patch_file_ending = ".apctrdi"

    @classmethod
    def get_source_data(cls) -> bytes:
        return CTRDIWorld.get_base_rom_bytes()


@typing.final
class CTRDISettings(settings.Group):
    @typing.final
    class RomFile(settings.SNESRomPath):
        """File name of the CT ROM"""
        description = "Chrono Trigger (USA) ROM"
        copy_to = "Chrono Trigger (USA).sfc"
        md5s = [CTRDIDeltaPatch.hash]  # noqa: RUF012

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
    game = "Chrono Trigger Rando-Dalton Imperial"
    topology_present = True
    origin_region_name = "starting_rewards"
    options_dataclass = CTRDIOptions
    Options: CTRDIOptions  # pyright: ignore[reportUninitializedInstanceVariable]
    settings_key = "ctrdi_options"
    settings: typing.ClassVar[CTRDISettings]  # pyright: ignore[reportIncompatibleVariableOverride]

    web = CTRDIWebWorld()

    rdi_settings: arguments.Settings  # pyright: ignore[reportUninitializedInstanceVariable]
    config: randostate.ConfigState  # pyright: ignore[reportUninitializedInstanceVariable]

    location_name_to_id = Locations.location_name_to_id
    item_name_to_id = Items.item_name_to_id

    _item_name_to_rdi_type: dict[str, ItemID]

    hashed_name: bytes  # pyright: ignore[reportUninitializedInstanceVariable]
    encoded_name: str  # pyright: ignore[reportUninitializedInstanceVariable]
    ct_rom: randomizer.ctrom.CTRom  # pyright: ignore[reportUninitializedInstanceVariable]


    def __init__(self, world: MultiWorld, player: int):
        super().__init__(world, player)
        self._item_name_to_rdi_type = {str(x): x for x in ItemID}
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
        base_rom = ctrom.CTRom.from_file(self.get_rom_path())
        self.ct_rom = randomizer.ctrom.CTRom(base_rom.getvalue())
        self.config = randomizer.get_random_config(
            self.rdi_settings, self.ct_rom, self.multiworld.random)
        self.ds_replacements = Items.get_ds_replacement_map(self.config)

    @typing.override
    def create_item(self, name: str) -> Item:
        """
        Create an AP item from the named RDI item.
        """
        return Items.create_ap_item(self._item_name_to_rdi_type[name], self.player)

    @typing.override
    def create_items(self) -> None:
        """
        Create the multiworld items for this player
        """
        items = Items.create_items(self.config, self.player, self.ds_replacements)
        self.multiworld.itempool += items

    @typing.override
    def create_regions(self) -> None:
        """
        Create regions and locations for this player
        """
        # Create regions and connecting exits
        region_dict = Locations.create_region_map(self.config, self.multiworld, self.player)

        # Create treasure locations and game/logic event locations
        Locations.create_locations_for_regions(region_dict, self.config, self.rdi_settings, self.player)
        Locations.create_recruit_events(region_dict, self.config, self.player)
        Locations.create_flag_events(region_dict, self.config, self.player)

        # Create victory location
        menu_region = region_dict[self.origin_region_name].ap_region
        victory_loc = Location(self.player, "Victory", None, menu_region)
        victory_loc.place_locked_item(
            Item("Victory", ItemClassification.progression, None, self.player))
        victory_loc.access_rule = Locations.create_victory_rule(self.player, self.rdi_settings)
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
        Generate the randomized ROM and create the patch file
        """
        # Get all items placed in this game world and write
        # the player and item data back to the RDI config
        self._modify_rom_treasures()

        out_rom = randomizer.get_ctrom_from_config(
            self.ct_rom, self.rdi_settings, self.config)

        multiworld.write_player_validation_data(out_rom, self.hashed_name)

        basename = self.multiworld.get_out_file_name_base(self.player)
        output_path = os.path.join(output_directory, f"{basename}.sfc")

        with open(output_path, "wb") as file:
            _ = file.write(out_rom.getbuffer())

        patch = CTRDIDeltaPatch(
            os.path.splitext(output_path)[0] +
            CTRDIDeltaPatch.patch_file_ending,
            player=self.player,
            player_name=self.multiworld.player_name[self.player],
            patched_path=output_path)

        patch.write()  # pyright: ignore[reportUnknownMemberType]
        os.unlink(output_path)

    def _convert_setting_value(self, flag_name: str, spec):
        """
        Convert a value for use in an RDI settings dictionary
        """
        value = getattr(self.options, flag_name)  # pyright: ignore[reportAny]
        if isinstance(value, Choice):
            value = value.name_lookup[value.value]
        elif isinstance(value, Toggle):
            value = value.value == 1
        elif isinstance(value, Range):
            value = value.value
            if spec.type_fn is not int:  # pyright: ignore[reportUnknownMemberType]
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
        for loc in Locations.locs_to_skip:
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
            tid = Locations.get_tid_from_address(loc.address)

            if is_local:
                # Replace the reward here with whatever AP chose.
                # TODO: Char levels
                if Items.is_tech_level_reward(loc.item.code):
                    char_id = Items.convert_to_char_id(loc.item.code)
                    self.config.treasure_assignment[tid] = tty.TechLevelReward(char_id)
                else:

                    if Items.is_ds_item_reward(loc.item.code):
                        # Convert from the DS item to the base item it replaced
                        item_id = ItemID(self.ds_replacements[loc.item.code] - Items.ITEM_ID_BASE)
                    else:
                        item_id = Items.item_name_to_rdi_type[loc.item.name]

                        # Replace progressive items with their base item and let
                        # the ROM side handle the upgrade.
                        if item_id in Items.progressive_items:
                            item_id = Items.progressive_items[item_id]

                    self.config.treasure_assignment[tid] = item_id
            else:
                # Replace reward here with the AP treasure type
                item_name = ctstrings.pre_process_string(loc.item.name)
                player_name = ctstrings.pre_process_string(self.multiworld.player_name[loc.item.player])
                self.config.treasure_assignment[tid] = tty.APReward(item_name, player_name)

    @staticmethod
    def get_rom_path() -> str:
        """
        Get the path to the Chrono Trigger ROM
        """
        file_name = CTRDIWorld.settings.rom_file  # pyright: ignore[reportAny]

        if not os.path.exists(file_name):  # pyright: ignore[reportAny]
            # TODO: Refine error text
            raise ValueError("No Chrono Trigger ROM specified")

        return file_name  # pyright: ignore[reportAny]

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
                raise Exception(
                    "Supplied base ROM does not match the known MD5 hash")

            CTRDIWorld.get_base_rom_bytes.base_rom_bytes = base_rom_bytes  # pyright: ignore[reportFunctionMemberAccess]

        return base_rom_bytes
