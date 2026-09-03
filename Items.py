"""
Item package to handle functions and logic related to
items and item placement in RDI.
"""
import logging

import ctrando.treasures.treasuretypes as tty
from ctrando.arguments.gearrandooptions import DSItem
from ctrando.common import randostate
from ctrando.common.ctenums import CharID, ItemID
from ctrando.entranceshuffler import entrancefiller

from BaseClasses import CollectionState, Item, ItemClassification

from .Locations import locs_to_skip

"""Offset to give CTRDI items a unique item range in AP"""
ITEM_ID_BASE = 50_350_000

rdi_logger = logging.getLogger("RDI")

_char_names = ["Crono", "Marle", "Lucca", "Robo", "Frog", "Ayla", "Magus"]

# Mapping of DS items to their in-game names.
# DS items randomly replace normal items based on certain settings
# but are not defined in the normal ItemID enum.
ds_item_to_name: dict[DSItem, str] = {
    DSItem.DREAMSEEKER: "DreamSeekr",
    DSItem.VENUS_BOW: "Venus Bow",
    DSItem.TURBOSHOT: "Turboshot",
    DSItem.SPELLSLINGER: "Spellslngr",
    DSItem.DRAGON_ARM: "Dragon Arm",
    DSItem.APOCALYPSE_ARM: "Apocal.Arm",
    DSItem.DINOBLADE: "Dino Blade",
    DSItem.JUDGEMENT_SCYTHE: "JudgeScyth",
    DSItem.DREAMREAPER: "Dreamreapr",
    DSItem.REPTITE_DRESS: "Rept Dress",
    DSItem.DRAGON_ARMOR: "Drgn Armor",
    DSItem.REGAL_PLATE: "RegalPlate",
    DSItem.REGAL_GOWN: "Regal Gown",
    DSItem.SHADOWPLUME_ROBE: "ShadowRobe",
    DSItem.ELEMENTAL_AEGIS: "Elem Aegis",
    DSItem.SAURIAN_LEATHERS: "SaurLeathr",
    DSItem.DRAGONHEAD: "DragonHead",
    DSItem.REPTITE_TIARA: "Rept.Tiara",
    DSItem.MASTERS_CROWN: "MastrCrown",
    DSItem.ANGELS_TIARA: "AngelTiara",
    DSItem.CHAMPIONS_BADGE: "ChampBadge",
    # These are already part of the normal item ID pool
    # DSItem.VALOR_CREST: "ValorCrest",
    # DSItem.DRAGONS_TEAR: "DragonTear",
}

name_to_ds_item: dict[str, DSItem] = {
    name: enum for enum, name in ds_item_to_name.items()
}

# Mapping of items to their progressive counterparts
progressive_items_map: dict[str, str] = {
    str(ItemID.PENDANT): "Progressive Pendant",
    str(ItemID.PENDANT_CHARGE): "Progressive Pendant",
    str(ItemID.MASAMUNE_1): "Progressive Masamune",
    str(ItemID.MASAMUNE_2): "Progressive Masamune",
    str(ItemID.PRISMSHARD): "Progressive Rainbow Shell/Prism Shard",
    str(ItemID.RAINBOW_SHELL): "Progressive Rainbow Shell/Prism Shard",
    str(ItemID.C_TRIGGER): "Progressive C.Trigger/Clone",
    str(ItemID.CLONE): "Progressive C.Trigger/Clone",
    str(ItemID.BIKE_KEY): "Progressive Bike Key/Race Log",
    str(ItemID.RACE_LOG): "Progressive Bike Key/Race Log",
}

# Map upgraded progressive items to their base items.
# We only send base items to the game and it sorts out the rest
progressive_item_upgrades: dict[int, ItemID] = {
    ItemID.PENDANT_CHARGE: ItemID.PENDANT,
    ItemID.MASAMUNE_2: ItemID.MASAMUNE_1,
    ItemID.PRISMSHARD: ItemID.RAINBOW_SHELL,
    ItemID.CLONE: ItemID.C_TRIGGER,
    ItemID.RACE_LOG: ItemID.BIKE_KEY,
}

_MAX_NORMAL_ITEM_ID = 0xFF
_DS_ITEM_BASE = 0x100
_CHAR_ITEM_BASE = 0x120
_TECH_LEVEL_ITEM_BASE = 0x130
_OTHER_ITEM_BASE = 0x140
_PROGRESSIVE_ITEM_BASE = 0x150

def _build_item_mappings() -> dict[str, int]:
    """
    Build the item name-to-ID mappings.
    """
    # Basic item mapping
    item_name_to_id = {str(item): ITEM_ID_BASE + item for item in ItemID}

    # Add DS items
    for i, item in enumerate(ds_item_to_name.keys()):
        item_name_to_id[ds_item_to_name[item]] = ITEM_ID_BASE + _DS_ITEM_BASE + i

    # Add character items
    for i, name in enumerate(_char_names):
        item_name_to_id[name] = ITEM_ID_BASE + _CHAR_ITEM_BASE + i

    # Add tech level items
    tech_level_names = [f"{_char_names[i]}_tech_level" for i in range(7)]
    for i, name in enumerate(tech_level_names):
        item_name_to_id[name] = ITEM_ID_BASE + _TECH_LEVEL_ITEM_BASE + i

    # Add items to represent progressive items
    for i, item in enumerate(progressive_item_upgrades.keys()):
        name = progressive_items_map[str(item)]
        item_name_to_id[name] = ITEM_ID_BASE + _PROGRESSIVE_ITEM_BASE + i

    return item_name_to_id

item_name_to_id = _build_item_mappings()
id_to_item_name = {v: k for k, v in item_name_to_id.items()}
item_name_to_rdi_type: dict[str, ItemID] = {str(x): x for x in ItemID}

def is_normal_item_reward(item_id: int) -> bool:
    """
    Check if this is a normal game item
    """
    return item_id <= (_MAX_NORMAL_ITEM_ID + ITEM_ID_BASE)

def is_tech_level_reward(item_id: int) -> bool:
    """
    Check if an item is a tech level reward
    """
    base_id = ITEM_ID_BASE + _TECH_LEVEL_ITEM_BASE
    end_id = base_id + len(_char_names)
    return (item_id >= base_id) and (item_id < end_id)

def is_char_reward(item_id: int) -> bool:
    """
    Check if an item is a character reward
    """
    base_id = ITEM_ID_BASE + _CHAR_ITEM_BASE
    end_id = base_id + len(_char_names)
    return (item_id >= base_id) and (item_id < end_id)

def is_ds_item_reward(item_id: int) -> bool:
    """
    Check if an item is a DS item reward
    """
    base_id = ITEM_ID_BASE + _DS_ITEM_BASE
    end_id = base_id + len(DSItem)
    return (item_id >= base_id) and (item_id < end_id)

def is_progressive_item_reward(item_id: int) -> bool:
    """
    Check if this is a special progressive item placeholder
    """
    base_id = ITEM_ID_BASE + _PROGRESSIVE_ITEM_BASE
    end_id = base_id + len(progressive_item_upgrades.keys())
    return (item_id >= base_id) and (item_id < end_id)

def get_base_progressive_item(item_id: int) -> ItemID:
    """
    Given a progressive item placeholder, get the base item.
    """
    item_name = id_to_item_name[item_id]
    if item_name == "Progressive Pendant":
        return ItemID.PENDANT
    if item_name == "Progressive Masamune":
        return ItemID.MASAMUNE_1
    if item_name == "Progressive Rainbow Shell/Prism Shard":
        return ItemID.RAINBOW_SHELL
    if item_name == "Progressive C.Trigger/Clone":
        return ItemID.C_TRIGGER
    if item_name == "Progressive Bike Key/Race Log":
        return ItemID.BIKE_KEY
    raise Exception(f"Invalid progressive item: {item_name}")

def convert_to_char_id(item_id: int) -> CharID:
    """
    Convert a tech level or character reward to a character ID
    associated with this reward item.
    """
    if is_char_reward(item_id):
        char_id = item_id - (ITEM_ID_BASE + _CHAR_ITEM_BASE)
    elif is_tech_level_reward(item_id):
        char_id = item_id - (ITEM_ID_BASE + _TECH_LEVEL_ITEM_BASE)
    else:
        raise Exception(f"Cannot convert item id {item_id} to a character id")

    char_id_list = list(CharID)
    return char_id_list[char_id]

def get_ds_replacement_map(config: randostate.ConfigState) -> dict[int, int]:
    """
    Create a dictionary mapping DS items to the base items that they replace
    """
    ds_map: dict[int, int] = {}

    good_armors = [
        ItemID.RUBY_ARMOR, ItemID.RED_MAIL, ItemID.BLACK_MAIL,
        ItemID.BLUE_MAIL, ItemID.WHITE_MAIL,
    ]
    good_helms = [
        ItemID.RBOW_HELM, ItemID.DARK_HELM, ItemID.MERMAIDCAP,
        ItemID.SIGHT_CAP, ItemID.MEMORY_CAP, ItemID.TIME_HAT
    ]

    def check_item(item: ItemID, ds_item: DSItem):
        """ Check if a single item has been replaced with a DS version"""
        ds_item_name = ds_item_to_name[ds_item]
        if config.item_db[item].get_name_as_str(True) == ds_item_name:
            # Map the AP item id of the DS item to the base item it is replacing
            ds_map[item_name_to_id[ds_item_name]] = int(item) + ITEM_ID_BASE

    def check_item_list(items: list[ItemID], ds_items: list[DSItem]):
        """Check if a list of items has been replaced with one of a list of DS versions"""
        for item in items:
            for ds_item in ds_items:
                check_item(item, ds_item)

    # Weapons
    check_item(ItemID.RAINBOW, DSItem.DREAMSEEKER)
    check_item(ItemID.VALKERYE, DSItem.VENUS_BOW)
    check_item(ItemID.WONDERSHOT, DSItem.SPELLSLINGER)
    check_item(ItemID.WONDERSHOT, DSItem.TURBOSHOT)
    check_item(ItemID.CRISIS_ARM, DSItem.APOCALYPSE_ARM)
    check_item(ItemID.CRISIS_ARM, DSItem.DRAGON_ARM)
    check_item(ItemID.DOOMSICKLE, DSItem.JUDGEMENT_SCYTHE)
    check_item(ItemID.DOOMSICKLE, DSItem.DREAMREAPER)
    check_item(ItemID.DEMON_HIT, DSItem.DINOBLADE)

    # Armors
    check_item(ItemID.GLOOM_CAPE, DSItem.SHADOWPLUME_ROBE)
    check_item(ItemID.MOON_ARMOR, DSItem.REGAL_PLATE)
    check_item(ItemID.PRISMDRESS, DSItem.REGAL_GOWN)
    check_item(ItemID.NOVA_ARMOR, DSItem.DRAGON_ARMOR)
    check_item(ItemID.ZODIACCAPE, DSItem.REPTITE_DRESS)
    check_item(ItemID.TABAN_SUIT, DSItem.ELEMENTAL_AEGIS)
    # Saurian Leathers can replace one of several armors
    check_item_list(good_armors, [DSItem.SAURIAN_LEATHERS])

    # Helmets
    check_item(ItemID.PRISM_HELM, DSItem.MASTERS_CROWN)
    check_item(ItemID.HASTE_HELM, DSItem.ANGELS_TIARA)
    # These helmets randomly replace another good helmet
    check_item_list(good_helms, [DSItem.DRAGONHEAD, DSItem.REPTITE_TIARA])

    # Accessories
    check_item(ItemID.HERO_MEDAL, DSItem.CHAMPIONS_BADGE)
    # NOTE: Valor Crest and Dragon's Tear don't replace existing items.
    #       Valor Crest takes over the unused Relic ID (0xB8)
    #       Dragon's Tear takes over the unused Seraph Song ID (0xB9)

    return ds_map

def create_items(config: randostate.ConfigState, player: int, ds_replacements: dict[int, int]) -> list[Item]:
    """
    Return a list of all possible items
    """

    # ds_replacements maps DS items to the items they replace.  We need the
    # inverse of that here so that we can initially create the DS items based
    # on the items thaat they are replacing.
    ds_replacements_inv: dict[int, int] = {v: k for k, v in ds_replacements.items()}

    items: list[Item] = []
    for loc, value in config.treasure_assignment.items():

        if loc in locs_to_skip:
            # Skip trading post since we can't track that
            continue

        if isinstance(value, tty.Gold):
            # TODO: Handle gold rewards
            #       I'm not sure it's possible to send arbitrary numbers
            #       for gold rewards, so leave gold chests local for now
            pass
        elif isinstance(value, tty.TechLevelReward):
            character = value.char_id
            item_name = f"{character!s}_tech_level"
            item_id = item_name_to_id[item_name]
            ap_item = Item(item_name, ItemClassification.useful, item_id, player)
            items.append(ap_item)
        #TODO: Character rewards
        elif isinstance(value, ItemID):
            ap_id = value + ITEM_ID_BASE
            if ap_id in ds_replacements_inv:
                # If the item is part of the DS replacement list, then we need to create the
                # new DS item instead of the base item.
                # Mark DS items as useful since they are high tier
                ds_item_id = ds_replacements_inv[ap_id]
                ds_item_name = id_to_item_name[ds_item_id]
                item_class = ItemClassification.useful
                if ds_item_name == ds_item_to_name[DSItem.CHAMPIONS_BADGE]:
                    item_class = ItemClassification.progression
                items.append(Item(ds_item_name, item_class, ds_item_id, player))
            elif str(value) in progressive_items_map:
                # This is a progressive item. Add the special progressive item version
                # instead of the base game version.
                item_name = progressive_items_map[str(value)]
                item_code = item_name_to_id[item_name]
                item_class = ItemClassification.progression
                items.append(Item(item_name, item_class, item_code, player))
            else:
                # Normal item
                items.append(create_ap_item(value, player))
        else:
            raise Exception("unknown type while creating APItems")

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

def collect_item(state: CollectionState, item: Item, remove: bool=False) -> str | None:
    """
    collect_item handles the override from the AutoWorld class.
    It assists with proper progressive item handling.
    """

    def handle_progressive_item(prog1: ItemID, prog2: ItemID) -> str | None:
        # NOTE: I'm not entirely sure what the remove arg is for, but I'm
        #       basically just doing what ALttP does.
        if state.has(str(prog2), item.player):
            # Currently at stage 2
            return str(prog2) if remove else None

        if state.has(str(prog1), item.player):
            # Currently at stage 1
            return str(prog1) if remove else str(prog2)

        # Currently none obtained
        return None if remove else str(prog1)

    item_name = item.name
    if item_name == "Progressive Pendant":
        return handle_progressive_item(ItemID.PENDANT, ItemID.PENDANT_CHARGE)
    if item_name == "Progressive Masamune":
        return handle_progressive_item(ItemID.MASAMUNE_1, ItemID.MASAMUNE_2)
    if item_name == "Progressive Rainbow Shell/Prism Shard":
        return handle_progressive_item(ItemID.RAINBOW_SHELL, ItemID.PRISMSHARD)
    if item_name == "Progressive C.Trigger/Clone":
        return handle_progressive_item(ItemID.C_TRIGGER, ItemID.CLONE)
    if item_name == "Progressive Bike Key/Race Log":
        return handle_progressive_item(ItemID.BIKE_KEY, ItemID.RACE_LOG)
    if item.advancement:
        return item.name
    return None
