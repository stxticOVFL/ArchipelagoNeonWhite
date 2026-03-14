# Locations are specific points that you would obtain an item at.
from enum import IntEnum
from typing import NamedTuple

from BaseClasses import Location

class LocationType(IntEnum):
    Bronze = 0,
    Silver = 1,
    Gold = 2,
    Platinum = 3,
    Developer = 4,
    Gift = 5,
    Sidequest = 6