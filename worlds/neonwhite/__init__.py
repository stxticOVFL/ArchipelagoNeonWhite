from BaseClasses import Item, Tutorial
from worlds.AutoWorld import WebWorld, World
from typing import Dict, Any
from . import events, items, locations, regions, rules
from .options import NeonWhiteOptions

nw_base_id = 7307000

class NeonWhiteWeb(WebWorld):
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Neon White integration for Archipelago multiworld games.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Badhamknibbs"]
    )]
    #theme = "partyTime"
    bug_report_page = "https://github.com/Badhamknibbs/ArchipelagoNeonWhite/issues"


# Keeping World slim so that it's easier to comprehend
class NeonWhiteWorld(World):
    """
    Neon White is a speedrunning FPS puzzle platformer made by freaks for freaks.
    Rush through a series of levels making smart use of your restricted cards to clear heaven of demons.
    """

    game = "Neon White"
    options: NeonWhiteOptions
    options_dataclass = NeonWhiteOptions

    item_name_to_id = items.create_items()
    location_name_to_id = locations.location_name_to_id

    item_name_groups = items.item_name_groups
    location_name_groups = locations.location_name_groups

    web = NeonWhiteWeb()

    def generate_early(self) -> None:
        if not self.player_name.isascii():
            raise Exception("Neon White yaml's slot name has invalid character(s).")

    # Returned items will be sent over to the client
    def fill_slot_data(self) -> Dict[str, Any]:
        return self.options.as_dict("death_link", "victory_condition", "path_option", "hidden_chests",
                                    "pedestal_checks", "orbs_as_checks", "bosses_as_checks", "extra_orbs", "shop_price")

    def create_regions(self) -> None:
        regions.create_all_regions_and_connections(self)

    def create_item(self, name: str) -> Item:
        return items.create_item(self.player, name)

    def create_items(self) -> None:
        items.create_all_items(self)

    def set_rules(self) -> None:
        rules.create_all_rules(self)

    def get_filler_item_name(self) -> str:
        return self.random.choice(items.filler_items)
