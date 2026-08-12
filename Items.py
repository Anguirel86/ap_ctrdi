"""
Item package to handle functions and logic related to
items and item placement in RDI.
"""
import logging

import ctrando.treasures.treasuretypes as tty
from ctrando.common import randostate
from ctrando.common.ctenums import CharID, ItemID
from ctrando.entranceshuffler import entrancefiller

from BaseClasses import Item, ItemClassification

from .Locations import locs_to_skip

# TODO: Pick a real item ID offset
"""Offset to give CTRDI items a unique item range in AP"""
ITEM_ID_BASE = 50_350_000

rdi_logger = logging.getLogger("RDI")

def _build_item_mappings() -> dict[str, int]:
    """
    Build the item and location name-to-ID mappings.
    Also adds 7 character items and their associated tech level items
    """
    item_name_to_id = {str(item): ITEM_ID_BASE + item for item in ItemID}

    # Add 7 character items and tech level items
    char_names = ["Crono", "Marle", "Lucca", "Robo", "Frog", "Ayla", "Magus"]
    tech_level_names = [f"{char_names[i]}_tech_level" for i in range(7)]

    # Add character items
    for i, name in enumerate(char_names):
        item_name_to_id[name] = ITEM_ID_BASE + 0x100 + i

    # Add tech level items
    for i, name in enumerate(tech_level_names):
        item_name_to_id[name] = ITEM_ID_BASE + 0x110 + i

    return item_name_to_id

item_name_to_id = _build_item_mappings()
id_to_item_name = {v: k for k, v in item_name_to_id.items()}
item_name_to_rdi_type: dict[str, ItemID] = {str(x): x for x in ItemID}

# Map upgraded progressive items to their base items.
# We only send base items to the game and it sorts out the rest
progressive_items: dict[int, ItemID] = {
    ItemID.PENDANT_CHARGE: ItemID.PENDANT,
    ItemID.MASAMUNE_2: ItemID.MASAMUNE_1,
    ItemID.PRISMSHARD: ItemID.RAINBOW_SHELL,
    ItemID.CLONE: ItemID.C_TRIGGER,
    ItemID.RACE_LOG: ItemID.BIKE_KEY,
}

def is_tech_level_reward(item_id: int) -> bool:
    """
    Check if an item is a tech level reward
    """
    return (item_id >= ITEM_ID_BASE + 0x110) and (item_id < ITEM_ID_BASE + 0x117)

def convert_to_char_id(item_id: int) -> CharID:
    """
    Convert a tech level reward to a character ID
    """
    char_id = item_id - (ITEM_ID_BASE + 0x110)
    char_id_list = list(CharID)
    return char_id_list[char_id]

def create_items(config: randostate.ConfigState, player: int) -> list[Item]:
    """
    Return a list of all possible items
    """
    items = []
    for loc, value in config.treasure_assignment.items():

        if loc in locs_to_skip:
            # Skip trading post since we can't track that
            continue

        if isinstance(value, tty.Gold):
            # TODO: Handle gold rewards
            #       I'm not sure it's possible to send arbitrary numbers
            #       for gold rewards, so maybe leave gold chests local?
            pass
        elif isinstance(value, tty.TechLevelReward):
            character = value.char_id
            item_name = f"{character!s}_tech_level"
            item_id = item_name_to_id[item_name]
            ap_item = Item(item_name, ItemClassification.useful, item_id, player)
            items.append(ap_item)
        #TODO: Character rewards
        else:
            items.append(create_ap_item(value, player))  # pyright: ignore[reportArgumentType]

    return items


def create_ap_item(item: ItemID, player: int) -> Item:
    """
    Create an AP item from a CTRDI ItemID
    """
    # TODO: Handle item classification for additional key items
    if item in entrancefiller.get_forced_key_items() or item == ItemID.JETSOFTIME:
        classification = ItemClassification.progression
    else:
        classification = ItemClassification.filler
    # TODO: Additional classifications? Useful?

    item_code = ITEM_ID_BASE + item
    return Item(str(item), classification, item_code, player)
