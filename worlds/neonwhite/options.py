from Options import Choice, DeathLink, DefaultOnToggle, StartInventoryPool, PerGameCommonOptions
from dataclasses import dataclass

class Difficulty(Choice):
    """
    How extreme the tricks required to complete the intended path are.
    Easy covers any intended vanilla path or relatively simple tricks to figure out for a casual player.
    Normal encompasses tricks that might need thinking out of the box or above average technical skill.
    Hard includes difficult tricks that are hard to perform or require deep technical knowledge of the game.
    Brutal adds absurd tricks that are borderline nonsense to understand and/or extremely demanding to perform.
    """
    display_name = "Difficulty"
    option_easy = 1
    option_normal = 2
    option_hard = 3
    option_brutal = 4
    default = 1

class MedalCap(Choice):
    """
    The highest medal to count for checks.
    Higher settings will result in more checks if Progressive Checks is enabled.
    """
    display_name = "Medal Cap"
    option_bronze = 1
    option_silver = 2
    option_gold = 3
    option_platinum = 4
    option_dev = 5
    default = 3

class ProgressiveChecks(DefaultOnToggle):
    """
    If every medal up to the medal cap should count for checks, or if only 1 check occurs for achieving the cap medal.
    If off, the number of checks will not change with changes to the medal cap.
    """
    display_name = "Progressive Checks"

class Traps(DefaultOnToggle):
    """
    Whether negative effects on the Neon White world are added to the item pool.
    """
    display_name = "Traps"

class NeonWhiteDeathLink(DeathLink):
    __doc__ = (DeathLink.__doc__ + "\n\n    You can disable this or set it to give yourself a trap effect when " +
               "another player dies in the in-game mod options.")


@dataclass
class NeonWhiteOptions(PerGameCommonOptions):
    start_inventory_from_pool: StartInventoryPool
    death_link: NeonWhiteDeathLink
    bad_effects: Traps
    progressive_checks: ProgressiveChecks
    medal_cap: MedalCap
    difficulty: Difficulty