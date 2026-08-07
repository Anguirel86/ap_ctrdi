"""
Locations package to handle location and logic related functions
"""

from collections.abc import Callable
from dataclasses import dataclass

import ctrando.treasures.treasuretypes as tty
from ctrando.arguments import arguments
from ctrando.bosses.bosstypes import BossSpotID
from ctrando.common import memory, randostate
from ctrando.common.ctenums import ItemID, RecruitID, TreasureID
from ctrando.entranceshuffler.locregions import LocRegion
from ctrando.entranceshuffler.owregions import OWRegion
from ctrando.entranceshuffler.regionmap import ExitConnector, RegionConnector
from ctrando.logic import logictypes

from BaseClasses import CollectionState, Item, ItemClassification, Location, MultiWorld, Region

"""Offset to give CTRDI locations a unique item range in AP"""
LOC_ID_BASE = 50_350_000


# NOTE: Trading post locations are not included for now since they can't be tracked.
#       If/when flags get added for them we can add them back.
locs_to_skip: list[TreasureID] = [
    TreasureID.TRADING_POST_PETAL_FANG_BASE,
    TreasureID.TRADING_POST_PETAL_FANG_UPGRADE,
    TreasureID.TRADING_POST_PETAL_FANG_UPGRADE,
    TreasureID.TRADING_POST_PETAL_HORN_BASE,
    TreasureID.TRADING_POST_PETAL_HORN_UPGRADE,
    TreasureID.TRADING_POST_PETAL_FEATHER_BASE,
    TreasureID.TRADING_POST_PETAL_FEATHER_UPGRADE,
    TreasureID.TRADING_POST_FANG_HORN_BASE,
    TreasureID.TRADING_POST_FANG_HORN_UPGRADE,
    TreasureID.TRADING_POST_FANG_FEATHER_BASE,
    TreasureID.TRADING_POST_FANG_FEATHER_UPGRADE,
    TreasureID.TRADING_POST_HORN_FEATHER_BASE,
    TreasureID.TRADING_POST_HORN_FEATHER_UPGRADE,
    TreasureID.TRADING_POST_SPECIAL,
]

@dataclass
class RegionData:
    """Store corresponding RDI and AP region definitions"""
    rdi_region: LocRegion | OWRegion
    ap_region: Region

location_name_to_id = {str(loc): LOC_ID_BASE + loc for loc in TreasureID}
loc_id_to_tid = {x + LOC_ID_BASE: x for x in TreasureID}

def get_tid_from_address(addr: int) -> TreasureID:
    """
    Get the RDI treasure ID from a location address.
    """
    return loc_id_to_tid[addr]

def create_victory_rule(player: int, rdi_settings: arguments.Settings) -> Callable[[CollectionState], bool]:
    """
    Create a victory rule for this game.
    Victory occurs when the player has completed the required objectives
    and collected the right items/characters to reach and defeat Lavos.
    """

    def victory_rule(state: CollectionState) -> bool:
        # Get objective count
        obj_tokens = ["Objective 1", "Objective 2",
                      "Objective 3", "Objective 4",
                      "Objective 5", "Objective 6",
                      "Objective 7", "Objective 8"]

        num_objs_complete = 0
        for obj in obj_tokens:
            if state.has(obj, player):
                num_objs_complete = num_objs_complete + 1

        # Objective based access
        algetty_portal_open = num_objs_complete >= rdi_settings.objective_options.num_algetty_portal_objectives
        omen_open = num_objs_complete >= rdi_settings.objective_options.num_omen_objectives
        bucket_open = num_objs_complete >= rdi_settings.objective_options.num_bucket_objectives
        timegauge_1999_open = num_objs_complete >= rdi_settings.objective_options.num_timegauge_objectives

        # Location access
        has_eot = state.has(
            str(memory.Flags.HAS_EOT_TIMEGAUGE_ACCESS), player)

        # Build up the access rules to lavos
        # End of Time -> Bucket
        if has_eot and bucket_open:
            return True

        # Hard Lavos
        # TODO: Do we actually want to include this in logic?
        #       I think this is actually an option
        #ocean_palace_access = state.has(
        #    str(objty.QuestID.ZEAL_PALACE_THRONE), player)
        #ruby_knife = state.has(str(ItemID.RUBY_KNIFE), player)
        #if ocean_palace_access and ruby_knife:
        #    return True

        # Crash Epoch into lavos in 1999
        has_flight = state.has(
            str(logictypes.ScriptReward.FLIGHT), player)
        if has_flight and timegauge_1999_open:
            return True

        # Black Omen
        if has_flight and algetty_portal_open and omen_open:
            return True

        return False

    return victory_rule

def create_flag_events(
    region_dict: dict[str, RegionData],
    config: randostate.ConfigState,
    player: int
):
    """
    Create event items/locations for script and memory flag rewards.
    These are used internally by the logic rules to gate access by some
    in-game event rather than holding an item or character.

    Ignore shop rewards
    """
    for loc_region in config.region_map.loc_region_dict.values():
        reward_list = \
            list(loc_region.reward_spots) + loc_region.region_rewards
        for reward in reward_list:
            if isinstance(reward, logictypes.ScriptReward) or \
                    isinstance(reward, logictypes.StrangeReward) or \
                    isinstance(reward, memory.Flags) or \
                    isinstance(reward, BossSpotID) or \
                    isinstance(reward, ItemID):

                create_event_loc_item_pair(
                    str(reward), region_dict[loc_region.name].ap_region, player)

def create_recruit_events(
    region_dict: dict[str, RegionData],
    config: randostate.ConfigState,
    player: int
):
    """
    Create event locations and event items for character recruitment.
    """
    for loc_region in config.region_map.loc_region_dict.values():
        for reward in loc_region.reward_spots:
            if isinstance(reward, RecruitID):
                # Found a recruit spot
                for character in config.recruit_dict[reward]:
                    char_name = str(character)
                    ap_region = region_dict[loc_region.name].ap_region
                    create_event_loc_item_pair(
                        char_name, ap_region, player)

def create_locations_for_regions(
    region_dict: dict[str, RegionData],
    config: randostate.ConfigState,
    rdi_settings: arguments.Settings,
    player: int):
    """
    Create corresponding locations for each RDI location and
    attach them to the appropriate regions.
    """
    progression_spots = list(rdi_settings.logic_options.forced_spots) + \
                        list(rdi_settings.logic_options.incentive_spots)
    excluded_spots = rdi_settings.logic_options.excluded_spots

    def non_progression(item):
        return item.classification in [ItemClassification.filler,
                                       ItemClassification.useful,
                                       ItemClassification.trap]

    def junk_only(item):
        return item.classification in [ItemClassification.filler,
                                       ItemClassification.trap]

    for region_data in region_dict.values():
        if not isinstance(region_data.rdi_region, LocRegion):
            continue

        for loc in region_data.rdi_region.reward_spots:
            if isinstance(loc, TreasureID):
                if loc in locs_to_skip:
                    continue

                if isinstance(config.treasure_assignment[loc], tty.Gold):
                    continue

                location = Location(
                    player, str(loc), location_name_to_id[str(loc)], region_data.ap_region)
                region_data.ap_region.locations.append(location)
                location.access_rule = lambda state: True

                if len(progression_spots) > 0:
                    # If there are no progressio spots then the user wants full
                    # chronosanity mode minus the excluded spots
                    # If there are progression spots specified then we need to
                    # set up the item rules accordingly
                    if loc not in progression_spots and loc not in excluded_spots:
                        # limit item classification for non-forced and non-incentive spots
                        location.item_rule = non_progression

                if loc in excluded_spots:
                    # Limit exluded spots to only filler items and traps
                    # These are usually missable locations so don't put anything good there
                    location.item_rule = junk_only


def create_region_map(
    config: randostate.ConfigState,
    multiworld: MultiWorld,
    player: int) -> dict[str, RegionData]:
    """
    Create a corresponding AP Region definition for every RDI region
    and wire up the exits
    """
    region_dict: dict[str, RegionData] = {}

    for name in config.region_map.name_connector_dict.keys():
        if name in config.region_map.ow_region_dict:
            rdi_region = config.region_map.ow_region_dict[name]
        elif name in config.region_map.loc_region_dict:
            rdi_region = config.region_map.loc_region_dict[name]
        else:
            raise Exception(f"Region not found: {name}")

        ap_region = Region(name, player, multiworld)
        region_dict[name] = RegionData(
            rdi_region=rdi_region, ap_region=ap_region)

    # Now that all regions are created, connect them up
    # based on the exit layout in the rando config
    for connectors in config.region_map.name_connector_dict.values():

        for connector in connectors:
            from_region = region_dict[connector.from_region_name]
            to_region = region_dict[connector.to_region_name]

            # Create the exit and set up its rule
            exit_name = f"{connector.link_name}-{connector.from_region_name}-{connector.to_region_name}"
            exit_obj = from_region.ap_region.create_exit(exit_name)
            access_rule = create_access_rule(connector, player)
            exit_obj.access_rule = access_rule
            exit_obj.connect(to_region.ap_region)

    return region_dict

def create_access_rule(
    connector: RegionConnector | ExitConnector,
    player: int
) -> Callable[[CollectionState], bool]:
    """
    Get an AP access rule from a RDI connector object
    """
    # Trivial case, always available
    # An list containint an empty list of single access rules
    if not connector.rule.get_access_rule()[0]:
        return lambda state: True

    # Convert the RDI rule to an AP rule
    def can_access(state: CollectionState) -> bool:

        for single_rule in connector.rule.get_access_rule():

            satisfies_rule = True
            for item in single_rule:
                count = single_rule.count(item)
                if not state.has(str(item), player, count):
                    # At least one condition of this rule isn't met
                    satisfies_rule = False

            if satisfies_rule:
                return True

        return False

    return can_access

def create_event_loc_item_pair(name: str, region: Region, player: int):
    """
    Create an event location with a locked event item
    """
    item = Item(name,
                ItemClassification.progression,
                None,
                player)

    loc_name = f"{region.name}-{name}"
    loc = Location(player, loc_name, None, region)
    loc.place_locked_item(item)
    region.locations.append(loc)
