"""
Item package to handle functions and logic related to
items and item placement in RDI.
"""
import typing

import ctrando.treasures.treasuretypes as tty
from ctrando.common import randostate
from ctrando.common.ctenums import ItemID
from ctrando.entranceshuffler import entrancefiller

from BaseClasses import Item, ItemClassification

from .Locations import locs_to_skip

# TODO: Pick a real item ID offset
"""Offset to give CTRDI items a unique item range in AP"""
ITEM_ID_BASE = 50_350_000

def _build_item_mappings() -> dict[str, int]:
    """
    Build the item and location name-to-ID mappings.
    Also adds 7 character items and their associated tech level items
    """
    item_name_to_id = {str(item): ITEM_ID_BASE + item for item in ItemID}

    # Add 7 character items and tech level items
    char_names = ["Crono", "Marle", "Lucca", "Robo", "Frog", "Ayla", "Magus"]
    tech_level_names = [f"tech_level_{i}" for i in range(7)]

    # Add character items
    for i, name in enumerate(char_names):
        item_name_to_id[name] = ITEM_ID_BASE + 0x100 + i

    # Add tech level items
    for i, name in enumerate(tech_level_names):
        item_name_to_id[name] = ITEM_ID_BASE + 0x110 + i

    return item_name_to_id

item_name_to_id = _build_item_mappings()
item_name_to_rdi_type: dict[str, ItemID] = {str(x): x for x in ItemID}

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
    if item in entrancefiller.get_forced_key_items():
        classification = ItemClassification.progression
    else:
        classification = ItemClassification.filler
    # TODO: Additional classifications? Useful?

    item_code = ITEM_ID_BASE + item
    return Item(str(item), classification, item_code, player)
