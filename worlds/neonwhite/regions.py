# Regions are areas in your game that you travel to.
from typing import TYPE_CHECKING

class Regions:
    neonwhite_regions: dict[str, list[str]] = {
        "Rebirth": {
            "Movement",
            "Pummel",
            "Gunner",
            "Cascade",
            "Elevate",
            "Bounce",
            "Purify",
            "Climb",
            "Fasttrack",
            "Glass Port"
        },
        "Killer Inside": {
            "Take Flight",
            "Godspeed",
            "Dasher",
            "Thrasher",
            "Outstretched",
            "Smackdown",
            "Catwalk",
            "Fastlane",
            "Distinguish",
            "Dancer"
        },
        "Only Shallow": {
            "Guardian",
            "Stomp",
            "Jumper",
            "Dash Tower",
            "Descent",
            "Driller",
            "Canals",
            "Sprint",
            "Mountain",
            "Superkinetic"
        },
        "The Old City": {
            "Arrival",
            "Forgotten City",
            "The Clocktower"
        },
        "The Burn that Cures": {
            "Fireball",
            "Ringer",
            "Cleaner",
            "Warehouse",
            "Boom",
            "Streets",
            "Steps",
            "Demolition",
            "Arcs",
            "Apartment"
        },
        "Covenant": {
            "Hanging Gardens",
            "Tangled",
            "Waterworks",
            "Killswitch",
            "Falling",
            "Shocker",
            "Bouquet",
            "Prepare",
            "Triptrack",
            "Race"
        },
        "Reckoning": {
            "Bubble",
            "Shield",
            "Overlook",
            "Pop",
            "Minefield",
            "Mimic",
            "Trigger",
            "Greenhouse",
            "Sweep",
            "Fuse"
        },
        "Benediction": {
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
        },
        "Apocrypha": {
            "Escalation",
            "Bolt",
            "Godstreak",
            "Plunge",
            "Mayhem",
            "Barrage",
            "Estate",
            "Trapwire",
            "Ricochet",
            "Fortress"
        },
        "The Third Temple": {
            "Holy Ground",
            "The Third Temple"
        },
        "Thousand Pound Butterfly": {
            "Spree",
            "Breakthrough",
            "Glide",
            "Closer",
            "Hike",
            "Switch",
            "Access",
            "Congregation",
            "Sequence",
            "Marathon"
        },
        "Hand of God": {
            "Sacrifice",
            "Absolution"
        },
        "Neon Red": {
            "Elevate Traversal I",
            "Elevate Traversal II",
            "Purify Traversal",
            "Godspeed Traversal",
            "Stomp Traversal",
            "Fireball Traversal",
            "Dominion Traversal",
            "Book of Life Traversal"
        },
        "Neon Violet": {
            "Doghouse",
            "Choker",
            "Chain",
            "Hellevator",
            "Razor",
            "All Seeing Eye",
            "Resident Saw I",
            "Resident Saw II"
        },
        "Neon Yellow": {
            "Sunset Flip Powerbomb",
            "Balloon Mountain",
            "Climbing Gym",
            "Fisherman Suplex",
            "STF",
            "Arena",
            "Attitude Adjustment",
            "Rocket"
        }
    }