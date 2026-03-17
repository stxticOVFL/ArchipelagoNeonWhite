# Locations are specific points that you would obtain an item at.
from enum import IntFlag, auto, IntEnum
import csv

class Difficulty(IntEnum):
    Easy = 0
    Normal = 1
    Hard = 2
    Brutal = 3


class LevelRequirements(IntFlag):
    FistOnly = 0
    Katana = auto()
    PurifyFire = auto()
    PurifyDiscard = auto()
    ElevateFire = auto()
    ElevateDiscard = auto()
    GodspeedFire = auto()
    GodspeedDiscard = auto()
    StompFire = auto()
    StompDiscard = auto()
    FireballFire = auto()
    FireballDiscard = auto()
    DominionFire = auto()
    DominionDiscard = auto()
    BookOfLife = auto()

# This only represents a single difficulty
class LevelRequirementSet:
    # String is the level name, list is 0..5, in order: dev,ace,gold,bronze,silver,gift
    requirements = dict[str, list[set[LevelRequirements]]]()

    def __init__(self, levels: list[str]):
        for level in levels:
            new_list = self.requirements[level] = list[set[LevelRequirements]]()
            new_list.append(set[LevelRequirements]())
            new_list.append(set[LevelRequirements]())
            new_list.append(set[LevelRequirements]())
            new_list.append(set[LevelRequirements]())
            new_list.append(set[LevelRequirements]())
            new_list.append(set[LevelRequirements]())

def string_to_level_req_flag(level:str) -> LevelRequirements:
    match level:
        case "Kf": return LevelRequirements.Katana
        case "Pf": return LevelRequirements.PurifyFire
        case "Pd": return LevelRequirements.PurifyDiscard
        case "Ef": return LevelRequirements.ElevateFire
        case "Ed": return LevelRequirements.ElevateDiscard
        case "Gf": return LevelRequirements.GodspeedFire
        case "Gd": return LevelRequirements.GodspeedDiscard
        case "Sf": return LevelRequirements.StompFire
        case "Sd": return LevelRequirements.StompDiscard
        case "Ff": return LevelRequirements.FireballFire
        case "Fd": return LevelRequirements.FireballDiscard
        case "Df": return LevelRequirements.DominionFire
        case "Dd": return LevelRequirements.DominionDiscard
        case "Bd": return LevelRequirements.BookOfLife
        case _:
            # Unexpected symbol/fist only
            return LevelRequirements.FistOnly
def import_csv_to_data(diff: Difficulty) -> LevelRequirementSet:
    # See archipelago requirements sheet for formatting
    file = open('./nw_cr.csv')
    csv_reader = csv.reader(file)
    csv_iter = iter(csv_reader)
    # Grab names, cells are merged and encompass the 4 difficulties so only take every multiple of 4
    level_names: list[str] = next(csv_iter)[0::4]
    new_requirements = LevelRequirementSet(level_names) # Return value that will be filled
    diff_idx = 0 # 0 == Dev, 1 == Ace, ... 5 == Gift
    for row in csv_iter:
        for i in range(0, len(level_names)):
            level_name = level_names[i]
            # First copy any requirements from the medal above (unless it's the gift row)
            # Doesn't matter if there's mixed combos, that's dealt with (e.g. Ef and Ef+Ed can exist together)
            if diff_idx != 5:
                for j in range(0, diff_idx):
                    new_requirements.requirements[level_name][diff_idx] |= new_requirements.requirements[level_name][j]
            # Copy requirements from all easier difficulties
            # Requirements are checked as a "can beat x with these weapons?" so this works
            for j in range(0, diff + 1):
                cell = row[(i * 4) + j]
                # F means fist completable, no requirements
                if cell == "F": new_requirements.requirements[level_name][diff_idx].add(LevelRequirements.FistOnly)
                else:
                    for solution in cell.split('|'):
                        requirements_aggregate = LevelRequirements(LevelRequirements.FistOnly)
                        for requirement in solution.split(","):
                            requirements_aggregate |= string_to_level_req_flag(requirement)
                        if requirements_aggregate != LevelRequirements.FistOnly:
                            new_requirements.requirements[level_name][diff_idx].add(requirements_aggregate)
        diff_idx = diff_idx + 1
    return new_requirements