import logging
from dataclasses import dataclass
from typing import override

import ctrando.common.memory
from ctrando.common.ctenums import ItemID, TreasureID
from ctrando.common.memory import Flags
from ctrando.treasures import treasuretypes

from NetUtils import ClientStatus
from SNIClient import SNIContext, snes_buffered_write, snes_flush_writes, snes_read
from worlds.AutoSNIClient import SNIClient

snes_logger = logging.getLogger("SNES")

ITEM_ID_BASE = 50_350_000
MAX_IN_GAME_ITEM_ID = 0xFF

# SNI memory mapping constants
ROM_START = 0x000000
WRAM_START = 0xF50000
WRAM_SIZE = 0x20000
SRAM_START = 0xE00000

# RDI constants
# NOTE: Addresses are in SNES addressing, not SNI addressing
# TODO: Update JoT values with RDI values
#       Received item count needs to be 2 bytes
EVENT_BLOCK_SIZE = 0x200
EVENT_BASE_ADDR = 0x7F0000
TREASURE_BASE_ADDR = 0x7F0001
RECEIVED_ITEM_ADDR = 0x7F0039
RECEIVED_ITEM_CNT = 0x7F003B
VICTORY_ADDR = 0x00  # TODO: Get real victory flag ADDR
VICTORY_FLAG = 0x01  # TODO: Get real victory flag bit

LOCATION_ADDR = 0xF50100  # Already in SNI address space

# ROM/player/slot validation
VALIDATION_ADDR = ROM_START + 0x3F8C03
VALIDATION_SIZE = 0x20

INVALID_TRACKING_LOCS = [0x00, 0x1B1]
MAX_MAP_ID = 0x1FF


@dataclass
class CheckCounter:
    """
    Dataclass to handle checks that are implemented as
    counters rather than standard memory flags
    """
    address: int
    count: int

@dataclass
class InventoryData:
    """
    Data class to store item ID and inventory index for items to be delivered.
    """
    item_id: int
    idx: int


"""
Dictionary of script based treasure locations to their respective
memory flag or counter data.
"""
_script_locations: dict[TreasureID, Flags | CheckCounter] = {
    # Northern Ruins event chests
    TreasureID.NORTHERN_RUINS_BASEMENT_600: Flags.NORTHERN_RUINS_BASEMENT_CHEST_600_OBTAINED,
    TreasureID.NORTHERN_RUINS_BASEMENT_1000: Flags.NORTHERN_RUINS_BASEMENT_CHEST_1000_OBTAINED,
    TreasureID.NORTHERN_RUINS_ANTECHAMBER_LEFT_600: Flags.NORTHERN_RUINS_ANTECHAMBER_CHEST_600_OBTAINED,
    TreasureID.NORTHERN_RUINS_ANTECHAMBER_LEFT_1000: Flags.NORTHERN_RUINS_ANTECHAMBER_CHEST_1000_OBTAINED,

    # Sealed chests
    TreasureID.NORTHERN_RUINS_ANTECHAMBER_SEALED_600: Flags.NORTHERN_RUINS_ANTECHAMBER_SEALED_600_OBTAINED,
    TreasureID.NORTHERN_RUINS_ANTECHAMBER_SEALED_1000: Flags.NORTHERN_RUINS_ANTECHAMBER_SEALED_1000_OBTAINED,
    TreasureID.NORTHERN_RUINS_BACK_LEFT_SEALED_600: Flags.NORTHERN_RUINS_BACK_LEFT_SEALED_600_OBTAINED,
    TreasureID.NORTHERN_RUINS_BACK_LEFT_SEALED_1000: Flags.NORTHERN_RUINS_BACK_LEFT_SEALED_1000_OBTAINED,
    TreasureID.NORTHERN_RUINS_BACK_RIGHT_SEALED_600: Flags.NORTHERN_RUINS_BACK_RIGHT_SEALED_600_OBTAINED,
    TreasureID.NORTHERN_RUINS_BACK_RIGHT_SEALED_1000: Flags.NORTHERN_RUINS_BACK_RIGHT_SEALED_1000_OBTAINED,
    TreasureID.TRUCE_INN_SEALED_600: Flags.TRUCE_INN_SEALED_600_OBTAINED,
    TreasureID.TRUCE_INN_SEALED_1000: Flags.TRUCE_INN_SEALED_1000_OBTAINED,
    TreasureID.PYRAMID_LEFT: Flags.PYRAMID_LEFT_CHEST,
    TreasureID.PYRAMID_RIGHT: Flags.PYRAMID_RIGHT_CHEST,
    TreasureID.PORRE_ELDER_SEALED_1: Flags.PORRE_ELDER_SEALED_1_OBTAINED,
    TreasureID.PORRE_ELDER_SEALED_2: Flags.PORRE_ELDER_SEALED_2_OBTAINED,
    TreasureID.PORRE_MAYOR_SEALED_1: Flags.PORRE_MAYOR_SEALED_1_OBTAINED,
    TreasureID.PORRE_MAYOR_SEALED_2: Flags.PORRE_MAYOR_SEALED_2_OBTAINED,
    TreasureID.GUARDIA_CASTLE_SEALED_600: Flags.GUARDIA_CASTLE_SEALED_600_OBTAINED,
    TreasureID.GUARDIA_CASTLE_SEALED_1000: Flags.GUARDIA_CASTLE_SEALED_1000_OBTAINED,
    TreasureID.GUARDIA_FOREST_SEALED_600: Flags.GUARDIA_FOREST_SEALED_600_OBTAINED,
    TreasureID.GUARDIA_FOREST_SEALED_1000: Flags.GUARDIA_FOREST_DEAD_END_SEALED_CHEST,
    TreasureID.HECKRAN_SEALED_1: Flags.HECKRAN_SEALED_OBTAINED,
    TreasureID.HECKRAN_SEALED_2: Flags.HECKRAN_SEALED_OBTAINED,
    TreasureID.MAGIC_CAVE_SEALED: Flags.MAGIC_CAVE_SEALED_CHEST,

    # Standard key item locations
    TreasureID.REPTITE_LAIR_KEY: Flags.NIZBEL_DEFEATED,
    TreasureID.MELCHIOR_RAINBOW_SHELL: Flags.MELCHIOR_TREASURY_FREE_ITEM_GIVEN,
    TreasureID.MELCHIOR_SUNSTONE_RAINBOW: Flags.MELCHIOR_TREASURY_SUNSTONE_ITEM_GIVEN,
    TreasureID.MELCHIOR_SUNSTONE_SPECS: Flags.MELCHIOR_TREASURY_SUNSTONE_ITEM_GIVEN,
    TreasureID.FROGS_BURROW_LEFT: Flags.OBTAINED_BURROW_LEFT_ITEM,
    TreasureID.MT_WOE_KEY: Flags.MT_WOE_BOSS_DEFEATED,
    TreasureID.FIONA_KEY: Flags.OBTAINED_GREEN_DREAM_ITEM,
    TreasureID.ARRIS_DOME_DOAN_KEY: Flags.OBTAINED_DOAN_ITEM,
    TreasureID.SUN_PALACE_KEY: Flags.SUN_PALACE_ITEM_OBTAINED,
    TreasureID.GENO_DOME_BOSS_1: Flags.GENO_DOME_ATROPOS_DEFEATED,
    TreasureID.GENO_DOME_BOSS_2: Flags.GENO_DOME_MOTHER_BRAIN_DEFEATED,
    TreasureID.GIANTS_CLAW_KEY: Flags.OBTAINED_GIANTS_CLAW_KEY,
    TreasureID.KINGS_TRIAL_KEY: Flags.KINGS_TRIAL_COMPLETE,
    TreasureID.ZENAN_BRIDGE_CHEF: Flags.CHEF_GIVES_JERKY,
    TreasureID.ZENAN_BRIDGE_CHEF_TAB: Flags.CHEF_GIVES_JERKY,
    TreasureID.ZENAN_BRIDGE_CAPTAIN: Flags.ZENAN_CAPTAIN_ITEM,
    TreasureID.SNAIL_STOP_KEY: Flags.OBTAINED_SNAIL_STOP_ITEM,
    TreasureID.LAZY_CARPENTER: Flags.CHORAS_1000_RECEIVED_TOOLS,
    TreasureID.TABAN_GIFT_VEST: Flags.TABAN_VEST_GIVEN,
    TreasureID.DENADORO_MTS_KEY: Flags.OBTAINED_DENADORO_KEY,

    # Other script treasures
    TreasureID.TABAN_GIFT_HELM: Flags.TABAN_HELM_GIVEN,
    TreasureID.TABAN_GIFT_SUIT: Flags.TABAN_SUIT_GIVEN,
    TreasureID.JERKY_GIFT: Flags.PORRE_JERKY_ITEM_OBTAINED,
    TreasureID.DENADORO_ROCK: Flags.OBTAINED_GOLD_ROCK,
    TreasureID.LARUBA_ROCK: Flags.RECEIVED_SILVER_ROCK,
    TreasureID.KAJAR_ROCK: Flags.OBTAINED_BLACK_ROCK,
    TreasureID.BEKKLER_KEY: Flags.HAS_BEKKLER_ITEM,
    TreasureID.CYRUS_GRAVE_KEY: Flags.MASAMUNE_UPGRADED,
    TreasureID.SUN_KEEP_2300: Flags.MOONSTONE_COLLECTED_2300,
    TreasureID.ARRIS_DOME_FOOD_LOCKER_KEY: Flags.OBTAINED_ARRIS_FOOD_ITEM,
    TreasureID.LUCCA_WONDERSHOT: Flags.LUCCA_MAKING_WONDERSHOT,
    TreasureID.TABAN_SUNSHADES: Flags.WONDERSHOT_SUNSHADES_RECEIVED,
    TreasureID.TATA_REWARD: Flags.OBTAINED_TATA_ITEM,
    TreasureID.TOMA_REWARD: Flags.OBTAINED_TOMA_ITEM,
    TreasureID.MELCHIOR_FORGE_MASA: Flags.HAS_FORGED_MASAMUNE,
    TreasureID.EOT_GASPAR_REWARD: Flags.HAS_GASPAR_ITEM,
    TreasureID.FAIR_PENDANT: Flags.FAIR_PENDANT_PICKED_UP,
    TreasureID.HUNTING_RANGE_NU_REWARD: Flags.HUNTING_RANGE_NU_REWARD,
    TreasureID.ZEAL_MAMMON_MACHINE: Flags.HAS_USED_MAMMON_MACHINE,
    TreasureID.MAGUS_CASTLE_FOUR_KIDS: Flags.MAGUS_CASTLE_GHOST_KIDS_CHEST,
    TreasureID.MAGUS_CASTLE_SLASH_SWORD_FLOOR: Flags.MAGUS_CASTLE_SLASH_SWORD_TREASURE,
    TreasureID.GUARDIA_PRISON_LUNCH_BAG: Flags.RECEIVED_PRISON_CELL_GIFT,
    TreasureID.DORINO_BROMIDE_MAGIC_TAB: Flags.DORINO_BROMIDE_MAGIC_TAB,
    TreasureID.GUARDIA_FOREST_POWER_TAB_600: Flags.OBTAINED_GUARDIA_FOREST_600_TAB,
    TreasureID.GUARDIA_FOREST_POWER_TAB_1000: Flags.OBTAINED_GUARDIA_FOREST_1000_TAB,
    TreasureID.MANORIA_CONFINEMENT_POWER_TAB: Flags.MANORIA_CONFINEMENT_POWER_TAB,
    TreasureID.PORRE_MARKET_600_POWER_TAB: Flags.PORRE_MARKET_600_TAB,
    TreasureID.DENADORO_MTS_SPEED_TAB: Flags.DENADORO_MTS_SPEED_TAB,
    TreasureID.TOMAS_GRAVE_SPEED_TAB: Flags.WEST_CAPE_SPEED_TAB,
    TreasureID.GIANTS_CLAW_CAVERNS_POWER_TAB: Flags.GIANTS_CLAW_CAVERNS_POWER_TAB,
    TreasureID.GIANTS_CLAW_ENTRANCE_POWER_TAB: Flags.GIANTS_CLAW_ENTRANCE_POWER_TAB,
    TreasureID.GIANTS_CLAW_TRAPS_POWER_TAB: Flags.GIANTS_CLAW_TRAPS_POWER_TAB,
    TreasureID.SUN_KEEP_600_POWER_TAB: Flags.SUN_KEEP_600_POWER_TAB,
    TreasureID.MEDINA_ELDER_SPEED_TAB: Flags.MEDINA_ELDER_SPEED_TAB,
    TreasureID.MEDINA_ELDER_MAGIC_TAB: Flags.MEDINA_ELDER_MAGIC_TAB,
    TreasureID.MAGUS_CASTLE_FLEA_MAGIC_TAB: Flags.MAGUS_CASTLE_FLEA_MAGIC_TAB,
    TreasureID.MAGUS_CASTLE_DUNGEONS_MAGIC_TAB: Flags.MAGUS_CASTLE_DUNGEONS_MAGIC_TAB,
    TreasureID.TRANN_DOME_SEALED_MAGIC_TAB: Flags.TRANN_DOME_SEALED_MAGIC_TAB,
    TreasureID.ARRIS_DOME_SEALED_POWER_TAB: Flags.ARRIS_DOME_SEALED_POWER_TAB,
    TreasureID.DEATH_PEAK_POWER_TAB: Flags.DEATH_PEAK_POWER_TAB,
    TreasureID.BLACKBIRD_DUCTS_MAGIC_TAB: Flags.BLACKBIRD_DUCTS_MAGIC_TAB,
    TreasureID.KEEPERS_DOME_MAGIC_TAB: Flags.OBTAINED_KEEPERS_DOME_MAGIC_TAB,
    TreasureID.GENO_DOME_ATROPOS_MAGIC_TAB: Flags.GENO_DOME_ATROPOS_MAGIC_TAB,
    TreasureID.GENO_DOME_CORRIDOR_POWER_TAB: Flags.GENO_DOME_CORRIDOR_POWER_TAB,
    TreasureID.GENO_DOME_LABS_MAGIC_TAB: Flags.GENO_DOME_LABS_MAGIC_TAB,
    TreasureID.GENO_DOME_LABS_SPEED_TAB: Flags.GENO_DOME_LABS_SPEED_TAB,
    TreasureID.ENHASA_NU_BATTLE_MAGIC_TAB: Flags.ENHASA_NU_BATTLE,
    TreasureID.ENHASA_NU_BATTLE_SPEED_TAB: Flags.ENHASA_NU_BATTLE,
    TreasureID.KAJAR_SPEED_TAB: Flags.KAJAR_MAGIC_LAB_SPEED_TAB,
    TreasureID.KAJAR_NU_SCRATCH_MAGIC_TAB: Flags.NU_SCRATCH_MAGIC_TAB,
    TreasureID.LAST_VILLAGE_NU_SHOP_MAGIC_TAB: Flags.LAST_VILLAGE_NU_SHOP_MAGIC_TAB,
    TreasureID.SUNKEN_DESERT_POWER_TAB: Flags.SUNKEN_DESERT_POWER_TAB,
    TreasureID.MOUNTAINS_RE_NICE_MAGIC_TAB: Flags.MOUNTAINS_RE_NICE_MAGIC_TAB,
    TreasureID.BEAST_NEST_POWER_TAB: Flags.BEAST_NEST_POWER_TAB,
    TreasureID.MT_WOE_MAGIC_TAB: Flags.MT_WOE_MAGIC_TAB,
    TreasureID.OCEAN_PALACE_ELEVATOR_MAGIC_TAB: Flags.OCEAN_PALACE_ELEVATOR_MAGIC_TAB,
    TreasureID.OZZIES_FORT_GUILLOTINES_TAB: Flags.OZZIES_FORT_GUILLOTINES_TAB,
    TreasureID.PROTO_DOME_PORTAL_TAB: Flags.PROTO_DOME_PORTAL_POWER_TAB,
    TreasureID.NORTHERN_RUINS_HEROS_GRAVE_MAGIC_TAB: Flags.CYRUS_GRAVE_MAGIC_TAB,
    TreasureID.NORTHERN_RUINS_LANDING_POWER_TAB: Flags.NORTHERN_RUINS_LANDING_POWER_TAB,
    TreasureID.CRONOS_MOM: Flags.MOM_GAVE_MONEY,
    TreasureID.TRUCE_MAYOR_2F_OLD_MAN: CheckCounter(
        ctrando.common.memory.Memory.TRUCE_MAYOR_2F_GOLD_NPC_COUNTER, 2),
    TreasureID.IOKA_SWEETWATER_TONIC: Flags.OBTAINED_SWEETWATER_HUT_TONICS,
    TreasureID.DORINO_INN_POWERMEAL: Flags.OBTAINED_DORINO_INN_POWERMEAL,
    TreasureID.YAKRA_KEY_CHEST: Flags.RESCUE_CHANCELLOR_1000,
    TreasureID.COURTROOM_YAKRA_KEY: Flags.OBTAINED_YAKRA_KEY,
    TreasureID.JOHNNY_RACE_POWER_TAB: Flags.OBTAINED_JOHNNY_RACE_POWER_TAB
}

# Map upgraded progressive items to their base items.
# We only send base items to the game and it sorts out the rest
_progressive_items: dict[int, int] = {
    ItemID.PENDANT_CHARGE: ItemID.PENDANT,
    ItemID.MASAMUNE_2: ItemID.MASAMUNE_1,
    ItemID.PRISMSHARD: ItemID.RAINBOW_SHELL,
    ItemID.CLONE: ItemID.C_TRIGGER,
    ItemID.RACE_LOG: ItemID.BIKE_KEY,
}


class CTRDIClient(SNIClient):
    """
    Game client for Chrono Trigger Rando-Dalton Imperial
    """

    game = "Chrono Trigger Rando-Dalton Imperial"

    def __init__(self):
        super().__init__()
        self._loc_name_to_id = {str(loc): ITEM_ID_BASE + loc for loc in TreasureID}

    @staticmethod
    def _to_sni(addr: int) -> int:
        """
        Convert a SNES address to the SNI address space.
        """
        return (addr - 0x7E0000) + WRAM_START

    @staticmethod
    def _is_chest_collected(event_data, chest_index: int) -> bool:
        """
        Check if the chest at the given index has been collected
        """
        chest_data_start = TREASURE_BASE_ADDR - EVENT_BASE_ADDR
        byte_offset = chest_index // 8
        bit = 1 << (chest_index % 8)

        return (event_data[chest_data_start + byte_offset] & bit) > 0

    @staticmethod
    def _is_script_treasure_collected(event_data, loc: TreasureID) -> bool:
        """
        Check if a script based treasure has been collected
        """
        if loc not in _script_locations.keys():
            raise Exception(f"Unknown location: {loc!s}")

        check_data = _script_locations[loc]
        offset = check_data.address - EVENT_BASE_ADDR
        if isinstance(check_data, Flags):
            # Standard memory flag
            return event_data[offset] & check_data.bit

        if isinstance(check_data, CheckCounter):
            # Counter type check
            return event_data[offset] >= check_data.count

        raise Exception(f"Unknown check type for {check_data!s}")

    def _can_track(
            self,
            event_data: bytes | None,
            map_data: bytes | None) -> bool:
        """
        Check if the game is in a valid state for tracking.
        Tracking isn't valid on some maps or during certain cutscenes.
        """

        if map_data is None or event_data is None:
            # Error during read?
            return False

        # Using a time gate triggers a cutscene that overwrites event memory.
        # Don't track events when the event memory is messed up.
        # During gate travel, the first 4 bytes of event data are always set
        # to a predictable pattern, so don't track anything if we see that.
        if event_data[0:4] == b"@ABC":
            return False

        # Don't track on invalid maps like the title screen
        map_id = int.from_bytes(map_data, "little")
        if map_id in INVALID_TRACKING_LOCS:
            return False

        # This is a slightly naive check to make sure the game has valid
        # data loaded and isn't just junk from the system turning on.
        #
        # This tries to fix an issue where the game auto-completes on connect
        # due to junk data in memory on flashcarts.
        if map_id > MAX_MAP_ID:
            return False

        return True

    def _track_locations(
            self,
            ctx: SNIContext,
            event_data: bytes) -> list[int]:
        """
        Track which locations the player has collected.
        """
        new_locations: list[int] = []
        for loc, treasure in treasuretypes.get_base_treasure_dict().items():
            loc_id = self._loc_name_to_id[str(loc)]
            if loc_id not in ctx.checked_locations and loc_id not in new_locations:
                if isinstance(treasure, treasuretypes.ChestTreasure):
                    if self._is_chest_collected(event_data, treasure.chest_index):
                        new_locations.append(loc_id)
                else:
                    # Script based treasures
                    if self._is_script_treasure_collected(event_data, loc):
                        new_locations.append(loc_id)

        return new_locations


    @classmethod
    async def _get_next_item_to_deliver(cls, ctx: SNIContext) -> tuple[bool, int]:
        """
        Check if we have any items awaiting delivery and if so, return
        the (AP) ID of that item.
        """
        item_cnt_buf = await snes_read(
            ctx, cls._to_sni(RECEIVED_ITEM_CNT), 2)
        if item_cnt_buf is None:
            # Read failed
            return False, 0

        item_cnt = int.from_bytes(item_cnt_buf, "little")
        num_items_received = len(ctx.items_received)
        if num_items_received <= item_cnt:
            # No items to deliver
            return False, item_cnt - num_items_received

        return True, ctx.items_received[item_cnt].item


    @classmethod
    async def _game_ready_for_delivery(cls, ctx: SNIContext) -> bool:
        """
        Check the delivery buffer address to see if the game
        is ready for another item to be delivered.
        """
        delivery_buf = await snes_read(
            ctx, cls._to_sni(RECEIVED_ITEM_ADDR), 2)
        if delivery_buf is None:
            return False

        if delivery_buf[0] != 0 or delivery_buf[1] != 0:
            # There's already an item in the delivery buffer
            return False

        # Delivery buffer is clear, we are good to send.
        return True

    @classmethod
    def _convert_item_to_game_format(cls, local_item_id: int) -> int:
        """
        Convert the item ID into the format the rando recognizes for item delivery.

        0x80nn - Character type item
        0x40nn - Tech type item
        0x20nn - Normal type item
        0x00nn - Ignored/no-op

        # TODO: Clean up the magic numbers here
        #       Maybe add conversion functions in an Items module?
        """
        # Normal item
        if local_item_id <= MAX_IN_GAME_ITEM_ID:
            return (local_item_id | 0x2000)

        # Character
        if local_item_id >= 0x100 and local_item_id < 0x110:
            return (local_item_id | 0x8000)

        # Tech level
        if local_item_id >= 0x110 and local_item_id < 0x120:
            return (local_item_id | 0x4000)

        raise Exception(f"Unknown item ID {local_item_id}")

    @classmethod
    async def _try_deliver_next_item(cls, ctx: SNIContext):
        """
        Deliver the next item if there are any available.

        Check the game's item counter against the client's number of
        received items and see if we have any items awaiting delivery.
        If so, then deliver the next one.
        """

        # Check the item delivery buffer. If it is not empty, then
        # the game is still busy delivering the previous item.
        game_ready = await cls._game_ready_for_delivery(ctx)
        if not game_ready:
            return

        # Check if we have any items awaiting delivery.
        # If so, we also get the index of the next item
        items_available, ap_item_id = await cls._get_next_item_to_deliver(ctx)
        if not items_available:
            return

        # Convert from AP item IDs to local CT item IDs
        game_item_id = ap_item_id - ITEM_ID_BASE

        # Check if this is a progressive item. We only send the base version to the game
        # and it sorts out the upgrades.
        if game_item_id in _progressive_items:
            game_item_id = _progressive_items[game_item_id]

        # Convert the item to an ID format the game's delivery code will recognize
        game_item_id = cls._convert_item_to_game_format(game_item_id)

        # We have items to deliver and the game is ready to receive them
        snes_buffered_write(
            ctx,
            cls._to_sni(RECEIVED_ITEM_ADDR),
            game_item_id.to_bytes(2, byteorder="little"))
        await snes_flush_writes(ctx)

    async def _handle_victory_condition(self, ctx: SNIContext, event_data: bytes):
        """
        Check if the player has achieved the goal.
        """
        offset = VICTORY_ADDR - EVENT_BASE_ADDR
        victory = (event_data[offset] & VICTORY_FLAG) > 0

        if victory and not ctx.finished_game:
            # Notify the server that the player beat the game
            ctx.finished_game = True
            await ctx.send_msgs(
                [{"cmd": "StatusUpdate", "status": ClientStatus.CLIENT_GOAL}])

    @override
    async def validate_rom(self, ctx: SNIContext) -> bool:

        data = await snes_read(ctx, VALIDATION_ADDR, VALIDATION_SIZE)
        if data is None or data[0:5] != b"APRDI":
            return False

        # Name should be a 8 byte hash of the player's settings name
        # TODO: Include seed info in validation so ROMs can't be reused?
        name = data[5:13]

        ctx.game = self.game
        ctx.items_handling = 0b001
        ctx.rom = name
        ctx.allow_collect = True

        return True

    @override
    async def game_watcher(self, ctx: SNIContext) -> None:

        if not ctx.allow_collect or ctx.server is None or ctx.slot is None:
            # Client isn't fully connected yet
            return

        # Read the map and event data needed for subsequent checks
        map_data = await snes_read(ctx, LOCATION_ADDR, 2)
        event_addr = self._to_sni(EVENT_BASE_ADDR)
        event_data = await snes_read(ctx, event_addr, EVENT_BLOCK_SIZE)

        if event_data is None:
            return

        # Check if the game is in a valid state for tracking then
        # handle new locations and item delivery.
        if self._can_track(event_data, map_data):
            new_locations = self._track_locations(ctx, event_data)
            await self._try_deliver_next_item(ctx)

            if len(new_locations) > 0:
                # Send newly checked locations to the server
                await ctx.send_msgs(
                    [{"cmd": "LocationChecks", "locations": new_locations}])

            await self._handle_victory_condition(ctx, event_data)

    @override
    async def deathlink_kill_player(self, ctx: SNIContext) -> None:
        """
        Not implmented for RDI
        """
        pass
