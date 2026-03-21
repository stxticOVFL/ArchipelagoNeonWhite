# Locations are specific points that you would obtain an item at.
import itertools
from enum import IntFlag, auto, IntEnum
import csv

from BaseClasses import Location


class NWLocation(Location):
    game: str = "Neon White"


neon_white_levels_normal = [
    "Movement",
    "Pummel",
    "Gunner",
    "Cascade",
    "Elevate",
    "Bounce",
    "Purify",
    "Climb",
    "Fasttrack",
    "Glass Port",
    "Take Flight",
    "Godspeed",
    "Dasher",
    "Thrasher",
    "Outstretched",
    "Smackdown",
    "Catwalk",
    "Fastlane",
    "Distinguish",
    "Dancer",
    "Guardian",
    "Stomp",
    "Jumper",
    "Dash Tower",
    "Descent",
    "Driller",
    "Canals",
    "Sprint",
    "Mountain",
    "Superkinetic",
    "Arrival",
    "Forgotten City",
    "Fireball",
    "Ringer",
    "Cleaner",
    "Warehouse",
    "Boom",
    "Streets",
    "Steps",
    "Demolition",
    "Arcs",
    "Apartment",
    "Hanging Gardens",
    "Tangled",
    "Waterworks",
    "Killswitch",
    "Falling",
    "Shocker",
    "Bouquet",
    "Prepare",
    "Triptrack",
    "Race",
    "Bubble",
    "Shield",
    "Overlook",
    "Pop",
    "Minefield",
    "Mimic",
    "Trigger",
    "Greenhouse",
    "Sweep",
    "Fuse",
    "Heaven's Edge",
    "Zipline",
    "Swing",
    "Chute",
    "Crash",
    "Ascent",
    "Straightaway",
    "Firecracker",
    "Streak",
    "Mirror",
    "Escalation",
    "Bolt",
    "Godstreak",
    "Plunge",
    "Mayhem",
    "Barrage",
    "Estate",
    "Trapwire",
    "Ricochet",
    "Fortress",
    "Holy Ground",
    "Spree",
    "Breakthrough",
    "Glide",
    "Closer",
    "Hike",
    "Switch",
    "Access",
    "Congregation",
    "Sequence",
    "Marathon",
]

neon_white_levels_giftless = [
    "The Clocktower",
    "The Third Temple",
    "Sacrifice",
    "Absolution"
]

neon_white_levels_sidequests = [  # No gifts either
    "Elevate Traversal I",
    "Elevate Traversal II",
    "Purify Traversal",
    "Godspeed Traversal",
    "Stomp Traversal",
    "Fireball Traversal",
    "Dominion Traversal",
    "Book of Life Traversal",
    "Doghouse",
    "Choker",
    "Chain",
    "Hellevator",
    "Razor",
    "All Seeing Eye",
    "Resident Saw I",
    "Resident Saw II",
    "Sunset Flip Powerbomb",
    "Balloon Mountain",
    "Climbing Gym",
    "Fisherman Suplex",
    "STF",
    "Arena",
    "Attitude Adjustment",
    "Rocket"
]

neon_white_levels_checks = [
    "Completion",
    "Gift"
]


def neon_white_get_locations() -> dict[str, int]:
    locations_dict: dict[str, int] = {}
    level_id = 500
    for level in neon_white_levels_sidequests:
        locations_dict[level + " Completion"] = level_id
        level_id += 1
        locations_dict[level + " Gift"] = level_id
        level_id += 1
    for level in itertools.chain(neon_white_levels_giftless, neon_white_levels_sidequests):
        locations_dict[level + " Completion"] = level_id
        level_id += 1

    return locations_dict


checks_in_sets_lvl = {
                         lvl: {
                             lvl + " " + check for check in neon_white_levels_checks
                         } for lvl in neon_white_levels_normal
                     } | {
                         lvl: {
                             lvl + " Completion"
                         } for lvl in itertools.chain(neon_white_levels_giftless, neon_white_levels_sidequests)
                     }