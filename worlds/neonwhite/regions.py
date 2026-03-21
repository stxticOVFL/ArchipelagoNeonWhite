from BaseClasses import Region, MultiWorld
from .locations import NWLocation, neon_white_get_locations, neon_white_levels_checks, neon_white_levels_normal, neon_white_levels_giftless, neon_white_levels_sidequests
from .options import NeonWhiteOptions
import itertools

def create_regions(player: int, world: MultiWorld, options: NeonWhiteOptions):
    # 121 levels split into 11 chapters of 11 levels, differing from the base game
    chapters_list = [
        "Chapter 1",
        "Chapter 2",
        "Chapter 3",
        "Chapter 4",
        "Chapter 5",
        "Chapter 6",
        "Chapter 7",
        "Chapter 8",
        "Chapter 9",
        "Chapter 10",
        "Chapter 11"
    ]

    heaven_regions: list[Region] = [Region("Central Heaven", player, world, None)]


    neon_white_locations = neon_white_get_locations()

    # Create regions and add locations
    for chapter in chapters_list:
        heaven_regions.append(Region(chapter, player, world, chapter))

    for level in neon_white_levels_normal:
        check_region = Region(level, player, world, None)
        for check in neon_white_levels_checks:
            check_name = level + " " + check
            new_location = NWLocation(player, check_name, neon_white_locations[check_name], None)
            check_region.locations.append(new_location)
        heaven_regions.append(check_region)

    for level in itertools.chain(neon_white_levels_giftless, neon_white_levels_sidequests):
        check_region = Region(level, player, world, None)
        check_name = level + " Completion"
        new_location = NWLocation(player, check_name, neon_white_locations[check_name], None)
        check_region.locations.append(new_location)
        heaven_regions.append(check_region)

    world.regions += heaven_regions