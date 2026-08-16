from dataclasses import dataclass
from typing import ClassVar, cast

from Options import OptionDict, OptionGroup, PerGameCommonOptions, Range, Toggle

# In this file, we define the options the player can pick.
# The most common types of options are Toggle, Range and Choice.

# Options will be in the game's template yaml.
# They will be represented by checkboxes, sliders etc. on the game's options page on the website.
# (Note: Options can also be made invisible from either of these places by overriding Option.visibility.
#  Vex2 doesn't have an example of this, but this can be used for secret / hidden / advanced options.)

# For further reading on options, you can also read the Options API Document:
# https://github.com/ArchipelagoMW/Archipelago/blob/main/docs/options%20api.md
option_presets: dict[str, dict[str, bool | int]] = {
  "main": {
    "all_stages_complete": True,
    "death_link": True,
    "all_achievements": False,
  },
}


# The first type of Option we'll discuss is the Toggle.
# A toggle is an option that can either be on or off. This will be represented by a checkbox on the website.
# The default for a toggle is "off".
# If you want a toggle to be on by default, you can use the "DefaultOnToggle" class instead of the "Toggle" class.
class AllStagesComplete(Toggle):
  """
  all_stages_complete
  """

  display_name: str = "AllStagesComplete"
  default: bool = cast(bool, option_presets["main"]["all_stages_complete"])

class AllAchievements(Toggle):
  """
  all_achievements
  """

  display_name: str = "AllAchievements"
  default: bool = cast(bool, option_presets["main"]["all_achievements"])


class DeathLink(Toggle):
  """
  Links your fate to other players in the multiworld.
  When enabled, if you die, everyone else on Death Link dies too. If they die, you die. Use with caution!
  """

  display_name: str = "DeathLink"
  default: bool = cast(bool, option_presets["main"]["death_link"])


# We must now define a dataclass inheriting from PerGameCommonOptions that we put all our options in.
# This is in the format "option_name_in_snake_case: OptionClassName".
@dataclass
class Vex2Options(PerGameCommonOptions):
  death_link: DeathLink
  all_stages_complete: AllStagesComplete


option_groups: list[OptionGroup] = [
  OptionGroup(
    "Gameplay",
    [
      DeathLink,
    ],
  ),
  OptionGroup(
    "Win Condition",
    [
      AllStagesComplete,
      AllAchievements,
    ],
  ),
]
