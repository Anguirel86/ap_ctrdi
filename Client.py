import logging
import typing
from collections import Counter
from dataclasses import dataclass
from typing import Tuple, override

import ctrando.common.memory
from ctrando.common.ctenums import TreasureID as TID
from ctrando.common.memory import Flags
from ctrando.treasures import treasuretypes

from NetUtils import ClientStatus, NetworkItem
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
RECEIVED_ITEM_ADDR = 0x7E287A  # TODO: Update this - JoT value
RECEIVED_ITEM_CNT = 0x7E287C  # TODO: Update this - JoT value
VICTORY_ADDR = 0x00  # TODO: Get real victory flag ADDR
VICTORY_FLAG = 0x01  # TODO: Get real victory flag bit

INVENTORY_ITEMS_ADDR = 0x7E2400
INVENTORY_QTY_ADDR = 0x7E2500
INVENTORY_DATA_SIZE = 0x200

ITEM_DELIVERY_FLAGS_ADDR = 0  # TODO: Update this - JoT value
ITEM_AVAILABLE_BIT = 0x01
GAME_READY_BIT = 0x02
LOCATION_ADDR = 0xF50100  # Already in SNI address space

# ROM/player/slot validation
VALIDATION_ADDR = ROM_START + 0x3F8C03  # TODO: Update this - JoT value
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
_script_locations: dict[TID, Flags | CheckCounter] = {
    # Northern Ruins event chests
    TID.NORTHERN_RUINS_BASEMENT_600: Flags.NORTHERN_RUINS_BASEMENT_CHEST_600_OBTAINED,
    TID.NORTHERN_RUINS_BASEMENT_1000: Flags.NORTHERN_RUINS_BASEMENT_CHEST_1000_OBTAINED,
    TID.NORTHERN_RUINS_ANTECHAMBER_LEFT_600: Flags.NORTHERN_RUINS_ANTECHAMBER_CHEST_600_OBTAINED,
    TID.NORTHERN_RUINS_ANTECHAMBER_LEFT_1000: Flags.NORTHERN_RUINS_ANTECHAMBER_CHEST_1000_OBTAINED,

    # Sealed chests
    TID.NORTHERN_RUINS_ANTECHAMBER_SEALED_600: Flags.NORTHERN_RUINS_ANTECHAMBER_SEALED_600_OBTAINED,
    TID.NORTHERN_RUINS_ANTECHAMBER_SEALED_1000: Flags.NORTHERN_RUINS_ANTECHAMBER_SEALED_1000_OBTAINED,
    TID.NORTHERN_RUINS_BACK_LEFT_SEALED_600: Flags.NORTHERN_RUINS_BACK_LEFT_SEALED_600_OBTAINED,
    TID.NORTHERN_RUINS_BACK_LEFT_SEALED_1000: Flags.NORTHERN_RUINS_BACK_LEFT_SEALED_1000_OBTAINED,
    TID.NORTHERN_RUINS_BACK_RIGHT_SEALED_600: Flags.NORTHERN_RUINS_BACK_RIGHT_SEALED_600_OBTAINED,
    TID.NORTHERN_RUINS_BACK_RIGHT_SEALED_1000: Flags.NORTHERN_RUINS_BACK_RIGHT_SEALED_1000_OBTAINED,
    TID.TRUCE_INN_SEALED_600: Flags.TRUCE_INN_SEALED_600_OBTAINED,
    TID.TRUCE_INN_SEALED_1000: Flags.TRUCE_INN_SEALED_1000_OBTAINED,
    TID.PYRAMID_LEFT: Flags.PYRAMID_LEFT_CHEST,
    TID.PYRAMID_RIGHT: Flags.PYRAMID_RIGHT_CHEST,
    TID.PORRE_ELDER_SEALED_1: Flags.PORRE_ELDER_SEALED_1_OBTAINED,
    TID.PORRE_ELDER_SEALED_2: Flags.PORRE_ELDER_SEALED_2_OBTAINED,
    TID.PORRE_MAYOR_SEALED_1: Flags.PORRE_MAYOR_SEALED_1_OBTAINED,
    TID.PORRE_MAYOR_SEALED_2: Flags.PORRE_MAYOR_SEALED_2_OBTAINED,
    TID.GUARDIA_CASTLE_SEALED_600: Flags.GUARDIA_CASTLE_SEALED_600_OBTAINED,
    TID.GUARDIA_CASTLE_SEALED_1000: Flags.GUARDIA_CASTLE_SEALED_1000_OBTAINED,
    TID.GUARDIA_FOREST_SEALED_600: Flags.GUARDIA_FOREST_SEALED_600_OBTAINED,
    TID.GUARDIA_FOREST_SEALED_1000: Flags.GUARDIA_FOREST_DEAD_END_SEALED_CHEST,
    TID.HECKRAN_SEALED_1: Flags.HECKRAN_SEALED_OBTAINED,
    TID.HECKRAN_SEALED_2: Flags.HECKRAN_SEALED_OBTAINED,
    TID.MAGIC_CAVE_SEALED: Flags.MAGIC_CAVE_SEALED_CHEST,

    # Standard key item locations
    TID.REPTITE_LAIR_KEY: Flags.NIZBEL_DEFEATED,
    TID.MELCHIOR_RAINBOW_SHELL: Flags.MELCHIOR_TREASURY_FREE_ITEM_GIVEN,
    TID.MELCHIOR_SUNSTONE_RAINBOW: Flags.MELCHIOR_TREASURY_SUNSTONE_ITEM_GIVEN,
    TID.MELCHIOR_SUNSTONE_SPECS: Flags.MELCHIOR_TREASURY_SUNSTONE_ITEM_GIVEN,
    TID.FROGS_BURROW_LEFT: Flags.OBTAINED_BURROW_LEFT_ITEM,
    TID.MT_WOE_KEY: Flags.MT_WOE_BOSS_DEFEATED,
    TID.FIONA_KEY: Flags.OBTAINED_GREEN_DREAM_ITEM,
    TID.ARRIS_DOME_DOAN_KEY: Flags.OBTAINED_DOAN_ITEM,
    TID.SUN_PALACE_KEY: Flags.SUN_PALACE_ITEM_OBTAINED,
    TID.GENO_DOME_BOSS_1: Flags.GENO_DOME_ATROPOS_DEFEATED,
    TID.GENO_DOME_BOSS_2: Flags.GENO_DOME_MOTHER_BRAIN_DEFEATED,
    TID.GIANTS_CLAW_KEY: Flags.OBTAINED_GIANTS_CLAW_KEY,
    TID.KINGS_TRIAL_KEY: Flags.KINGS_TRIAL_COMPLETE,
    TID.ZENAN_BRIDGE_CHEF: Flags.CHEF_GIVES_JERKY,
    TID.ZENAN_BRIDGE_CHEF_TAB: Flags.CHEF_GIVES_JERKY,
    TID.ZENAN_BRIDGE_CAPTAIN: Flags.ZENAN_CAPTAIN_ITEM,
    TID.SNAIL_STOP_KEY: Flags.OBTAINED_SNAIL_STOP_ITEM,
    TID.LAZY_CARPENTER: Flags.CHORAS_1000_RECEIVED_TOOLS,
    TID.TABAN_GIFT_VEST: Flags.TABAN_VEST_GIVEN,
    TID.DENADORO_MTS_KEY: Flags.OBTAINED_DENADORO_KEY,

    # Other script treasures
    TID.TABAN_GIFT_HELM: Flags.TABAN_HELM_GIVEN,
    TID.TABAN_GIFT_SUIT: Flags.TABAN_SUIT_GIVEN,
    TID.JERKY_GIFT: Flags.PORRE_JERKY_ITEM_OBTAINED,
    TID.DENADORO_ROCK: Flags.OBTAINED_GOLD_ROCK,
    TID.LARUBA_ROCK: Flags.RECEIVED_SILVER_ROCK,
    TID.KAJAR_ROCK: Flags.OBTAINED_BLACK_ROCK,
    TID.BEKKLER_KEY: Flags.HAS_BEKKLER_ITEM,
    TID.CYRUS_GRAVE_KEY: Flags.MASAMUNE_UPGRADED,
    TID.SUN_KEEP_2300: Flags.MOONSTONE_COLLECTED_2300,
    TID.ARRIS_DOME_FOOD_LOCKER_KEY: Flags.OBTAINED_ARRIS_FOOD_ITEM,
    TID.LUCCA_WONDERSHOT: Flags.LUCCA_MAKING_WONDERSHOT,
    TID.TABAN_SUNSHADES: Flags.WONDERSHOT_SUNSHADES_RECEIVED,
    TID.TATA_REWARD: Flags.OBTAINED_TATA_ITEM,
    TID.TOMA_REWARD: Flags.OBTAINED_TOMA_ITEM,
    TID.MELCHIOR_FORGE_MASA: Flags.HAS_FORGED_MASAMUNE,
    TID.EOT_GASPAR_REWARD: Flags.HAS_GASPAR_ITEM,
    TID.FAIR_PENDANT: Flags.FAIR_PENDANT_PICKED_UP,
    TID.HUNTING_RANGE_NU_REWARD: Flags.HUNTING_RANGE_NU_REWARD,
    TID.ZEAL_MAMMON_MACHINE: Flags.HAS_USED_MAMMON_MACHINE,
    TID.MAGUS_CASTLE_FOUR_KIDS: Flags.MAGUS_CASTLE_GHOST_KIDS_CHEST,
    TID.MAGUS_CASTLE_SLASH_SWORD_FLOOR: Flags.MAGUS_CASTLE_SLASH_SWORD_TREASURE,
    TID.GUARDIA_PRISON_LUNCH_BAG: Flags.RECEIVED_PRISON_CELL_GIFT,
    TID.DORINO_BROMIDE_MAGIC_TAB: Flags.DORINO_BROMIDE_MAGIC_TAB,
    TID.GUARDIA_FOREST_POWER_TAB_600: Flags.OBTAINED_GUARDIA_FOREST_600_TAB,
    TID.GUARDIA_FOREST_POWER_TAB_1000: Flags.OBTAINED_GUARDIA_FOREST_1000_TAB,
    TID.MANORIA_CONFINEMENT_POWER_TAB: Flags.MANORIA_CONFINEMENT_POWER_TAB,
    TID.PORRE_MARKET_600_POWER_TAB: Flags.PORRE_MARKET_600_TAB,
    TID.DENADORO_MTS_SPEED_TAB: Flags.DENADORO_MTS_SPEED_TAB,
    TID.TOMAS_GRAVE_SPEED_TAB: Flags.WEST_CAPE_SPEED_TAB,
    TID.GIANTS_CLAW_CAVERNS_POWER_TAB: Flags.GIANTS_CLAW_CAVERNS_POWER_TAB,
    TID.GIANTS_CLAW_ENTRANCE_POWER_TAB: Flags.GIANTS_CLAW_ENTRANCE_POWER_TAB,
    TID.GIANTS_CLAW_TRAPS_POWER_TAB: Flags.GIANTS_CLAW_TRAPS_POWER_TAB,
    TID.SUN_KEEP_600_POWER_TAB: Flags.SUN_KEEP_600_POWER_TAB,
    TID.MEDINA_ELDER_SPEED_TAB: Flags.MEDINA_ELDER_SPEED_TAB,
    TID.MEDINA_ELDER_MAGIC_TAB: Flags.MEDINA_ELDER_MAGIC_TAB,
    TID.MAGUS_CASTLE_FLEA_MAGIC_TAB: Flags.MAGUS_CASTLE_FLEA_MAGIC_TAB,
    TID.MAGUS_CASTLE_DUNGEONS_MAGIC_TAB: Flags.MAGUS_CASTLE_DUNGEONS_MAGIC_TAB,
    TID.TRANN_DOME_SEALED_MAGIC_TAB: Flags.TRANN_DOME_SEALED_MAGIC_TAB,
    TID.ARRIS_DOME_SEALED_POWER_TAB: Flags.ARRIS_DOME_SEALED_POWER_TAB,
    TID.DEATH_PEAK_POWER_TAB: Flags.DEATH_PEAK_POWER_TAB,
    TID.BLACKBIRD_DUCTS_MAGIC_TAB: Flags.BLACKBIRD_DUCTS_MAGIC_TAB,
    TID.KEEPERS_DOME_MAGIC_TAB: Flags.OBTAINED_KEEPERS_DOME_MAGIC_TAB,
    TID.GENO_DOME_ATROPOS_MAGIC_TAB: Flags.GENO_DOME_ATROPOS_MAGIC_TAB,
    TID.GENO_DOME_CORRIDOR_POWER_TAB: Flags.GENO_DOME_CORRIDOR_POWER_TAB,
    TID.GENO_DOME_LABS_MAGIC_TAB: Flags.GENO_DOME_LABS_MAGIC_TAB,
    TID.GENO_DOME_LABS_SPEED_TAB: Flags.GENO_DOME_LABS_SPEED_TAB,
    TID.ENHASA_NU_BATTLE_MAGIC_TAB: Flags.ENHASA_NU_BATTLE,
    TID.ENHASA_NU_BATTLE_SPEED_TAB: Flags.ENHASA_NU_BATTLE,
    TID.KAJAR_SPEED_TAB: Flags.KAJAR_MAGIC_LAB_SPEED_TAB,
    TID.KAJAR_NU_SCRATCH_MAGIC_TAB: Flags.NU_SCRATCH_MAGIC_TAB,
    TID.LAST_VILLAGE_NU_SHOP_MAGIC_TAB: Flags.LAST_VILLAGE_NU_SHOP_MAGIC_TAB,
    TID.SUNKEN_DESERT_POWER_TAB: Flags.SUNKEN_DESERT_POWER_TAB,
    TID.MOUNTAINS_RE_NICE_MAGIC_TAB: Flags.MOUNTAINS_RE_NICE_MAGIC_TAB,
    TID.BEAST_NEST_POWER_TAB: Flags.BEAST_NEST_POWER_TAB,
    TID.MT_WOE_MAGIC_TAB: Flags.MT_WOE_MAGIC_TAB,
    TID.OCEAN_PALACE_ELEVATOR_MAGIC_TAB: Flags.OCEAN_PALACE_ELEVATOR_MAGIC_TAB,
    TID.OZZIES_FORT_GUILLOTINES_TAB: Flags.OZZIES_FORT_GUILLOTINES_TAB,
    TID.PROTO_DOME_PORTAL_TAB: Flags.PROTO_DOME_PORTAL_POWER_TAB,
    TID.NORTHERN_RUINS_HEROS_GRAVE_MAGIC_TAB: Flags.CYRUS_GRAVE_MAGIC_TAB,
    TID.NORTHERN_RUINS_LANDING_POWER_TAB: Flags.NORTHERN_RUINS_LANDING_POWER_TAB,
    TID.CRONOS_MOM: Flags.MOM_GAVE_MONEY,
    TID.TRUCE_MAYOR_2F_OLD_MAN: CheckCounter(
        ctrando.common.memory.Memory.TRUCE_MAYOR_2F_GOLD_NPC_COUNTER, 2),
    TID.IOKA_SWEETWATER_TONIC: Flags.OBTAINED_SWEETWATER_HUT_TONICS,
    TID.DORINO_INN_POWERMEAL: Flags.OBTAINED_DORINO_INN_POWERMEAL,
    TID.YAKRA_KEY_CHEST: Flags.RESCUE_CHANCELLOR_1000,
    TID.COURTROOM_YAKRA_KEY: Flags.OBTAINED_YAKRA_KEY,
    TID.JOHNNY_RACE_POWER_TAB: Flags.OBTAINED_JOHNNY_RACE_POWER_TAB
}


class CTRDIClient(SNIClient):
    """
    Game client for Chrono Trigger Rando-Dalton Imperial
    """

    game = "Chrono Trigger Rando-Dalton Imperial"

    def __init__(self):
        super().__init__()
        self._loc_name_to_id = {str(loc): ITEM_ID_BASE + loc for loc in TID}

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
    def _is_script_treasure_collected(event_data, loc: TID) -> bool:
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
        elif isinstance(check_data, CheckCounter):
            # Counter type check
            return event_data[offset] >= check_data.count
        else:
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

    @staticmethod
    def _get_item_counts_to_deliver(ctx: SNIContext, start_idx: int) -> Counter[int]:
        """
        Get a Counter containing the IDs of items to be delivered.
        """
        return Counter([x.item - ITEM_ID_BASE for x in ctx.items_received[start_idx:]])

    @classmethod
    async def _items_awaiting_delivery(cls, ctx: SNIContext) -> tuple[bool, int]:
        """
        Fetch the number of items that have already been delivered.
        This is stored in the game's memory.
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

        return True, item_cnt

    @classmethod
    async def _deliver_items(cls, ctx:SNIContext, start_idx: int) -> bool:
        """
        Handle the actual item delivery.

        Write items directly into player inventory.
        TODO: Character and tech level rewards
        """
        # Read the current inventory state (items and quantity in one buffer)
        inventory_buf = await snes_read(
            ctx, cls._to_sni(INVENTORY_ITEMS_ADDR), INVENTORY_DATA_SIZE)
        if inventory_buf is None:
            return False

        # inventory_buf  contains both item ID and quantity information
        # Get slices for each type of data
        # Only 0xF2 slots are used in each section, the rest are unused
        inventory_ids = list(inventory_buf[:0xF2])
        inventory_qty = list(inventory_buf[0x100:0xF2])

        # Get a counter of the item IDs to be delivered.
        counts_to_deliver = cls._get_item_counts_to_deliver(ctx, start_idx)

        # Keep a list of inventory indexes that we update.
        # Once we've updated out local copy of the inventory we can
        # write back the updated fields to game RAM.
        modified_inventory_idx_set = set()

        for item_id, count in counts_to_deliver.items():
            if item_id <= MAX_IN_GAME_ITEM_ID:
                # Normal game item
                if item_id in inventory_ids:
                    # Player already has one, so add to existing count
                    idx = inventory_ids.index(item_id)
                    inventory_qty[idx] = min(inventory_qty[idx] + count, 99)
                    modified_inventory_idx_set.add(idx)
                else:
                    # The player doesn't have this item yet
                    # Add an entry to both the inventory ID and quantity sections
                    # Inventory is not guaranteed to be sorted or contiguous.
                    # Find the next empty slot and add the item there.
                    new_item_idx = inventory_ids.index(0)
                    inventory_ids[new_item_idx] = item_id
                    inventory_qty[new_item_idx] = min(count, 99)
                    modified_inventory_idx_set.add(new_item_idx)
            else:
                # Character, tech level, or other reward
                ...

        # The local inventory copy should be fully updated.  Now write just
        # the changed item idxs back to the game RAM.
        for idx in modified_inventory_idx_set:
            snes_buffered_write(ctx, cls._to_sni(INVENTORY_ITEMS_ADDR + idx), bytes([inventory_ids[idx]]))
            snes_buffered_write(ctx, cls._to_sni(INVENTORY_QTY_ADDR + idx), bytes([inventory_qty[idx]]))

        await snes_flush_writes(ctx)

        return True

    @classmethod
    async def _handle_item_delivery(cls, ctx: SNIContext):
        """
        Handle the item delivery process.

        Item delivery is a multi-step process where:
            1. The client sets a flag in game RAM to signify items are ready for delivery
            2. The game sets a bit to acknowledge it is ready to receive items
              a. This pauses game execution to facilitate atomic item delivery
            3. The client directly writes items to game RAM
              a. Inventory items are directly written to inventory
              b. Characters and tech levels are written into buffers for the game to handle
            4. Client updates item delivery counters
            5. Client clears the items_available flag
            6. The game clears its flag and continues executing
        """
        flags_buf = await snes_read(
            ctx, cls._to_sni(ITEM_DELIVERY_FLAGS_ADDR), 1)
        if flags_buf is None:
            return

        # Check delivery status bit in the game
        items_available_bit = (flags_buf[0] & ITEM_AVAILABLE_BIT) > 0
        game_ready_bit = (flags_buf[0] & GAME_READY_BIT) > 0

        items_available, item_cnt = await cls._items_awaiting_delivery(ctx)
        #if not items_available:
        #    # No items to deliver
        #    # TODO: Check if the game bit is set but we don't actually think
        #    #       we need to delivery items.
        #    #       This means we are out of sync.  Maybe we can recover?
        #    return

        if items_available and not items_available_bit:
            # Set the item available flag
            # This lets the game know we're ready to deliver items
            new_flags_val = flags_buf[0] | ITEM_AVAILABLE_BIT
            snes_buffered_write(ctx, cls._to_sni(ITEM_DELIVERY_FLAGS_ADDR), bytes([new_flags_val]))
            await snes_flush_writes(ctx)
            return

        if not game_ready_bit:
            # Wait for game to signal ready
            return

        # The game is ready to receive items.
        # Send over everything awaiting delivery
        delivery_successful = await cls._deliver_items(ctx, item_cnt)

        if delivery_successful:
            # Write back the total number of delivered items to the game RAM
            # Stored as a 16 bit integer
            total_delivered = len(ctx.items_received)
            snes_buffered_write(ctx, cls._to_sni(RECEIVED_ITEM_CNT), total_delivered.to_bytes(2, byteorder="little"))

            # Clear the item available bit
            new_flags = flags_buf[0] & (~ITEM_AVAILABLE_BIT)
            snes_buffered_write(ctx, cls._to_sni(ITEM_DELIVERY_FLAGS_ADDR), bytes(new_flags))

            # Flush writes to finalize item delivery
            await snes_flush_writes(ctx)


    async def _handle_victory_condition(
            self, ctx: SNIContext, event_data: bytes):
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
        if data is None:
            return False

        # TODO: Actual slot validation
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
            await self._handle_item_delivery(ctx)

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
