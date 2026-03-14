import itertools
from collections import Counter
from typing import NamedTuple, TYPE_CHECKING, ClassVar, Dict
from enum import IntEnum
from .regions import Regions

if TYPE_CHECKING:
    from . import NeonWhiteWorld, nw_base_id
else:
    NeonWhiteWorld = object

neonwhite_cards: set[str] = {
    "Purify",
    "Elevate",
    "Godspeed",
    "Stomp",
    "Fireball",
    "Dominion"
}

# For ease of programming, order of items and their IDs is:
# nw_base_id -> nw_base_id + level_count: level IDs
# final_level_id + 1 -> final_level_id + 1 + (card count * 2): card fires and discards in alternating order
# final_card_id + 1 -> final_card_id + 3: Katana and Book of Life (fire and discard only, respectively)

def create_items(start_level:str) -> dict[str, int]:
    new_items: dict[str, int]
    itemid_iterator: int = nw_base_id
    for chapter in Regions.neonwhite_regions:
        for level in Regions.neonwhite_regions[chapter]:
            if level == start_level: continue # Skip the level we start on
            new_items["{0} - {1}".format(chapter, level)] = itemid_iterator
            itemid_iterator += 1
    for card in neonwhite_cards:
        new_items["{0} - Fire".format(card)] = itemid_iterator
        itemid_iterator += 1
        new_items["{0} - Discard".format(card)] = itemid_iterator
        itemid_iterator += 1
    new_items["Katana"] = itemid_iterator
    itemid_iterator += 1
    new_items["Book of Life"] = itemid_iterator
    itemid_iterator += 1