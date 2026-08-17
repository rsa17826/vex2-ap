from dataclasses import dataclass, make_dataclass
from typing import cast

from Options import OptionGroup, PerGameCommonOptions, Toggle

from .game_data import OPTIONS

option_presets: dict[str, dict[str, bool | int]] = {
  "main": {},
}


option_classes = {}
option_groups: list[OptionGroup] = []
dataclass_fields = []


def pas(s: str) -> str:
  return "".join(x[0].upper() + x[1:] for x in s.split("_"))


for group_name, opt in OPTIONS.items():
  arr = []
  for snake_name, doc, val in opt:
    class_name = pas(snake_name)
    option_presets["main"][snake_name] = val

    cls = type(
      class_name,
      (Toggle,),
      {
        "__doc__": doc,
        "display_name": class_name,
        "default": cast(bool, option_presets["main"][snake_name]),
      },
    )

    option_classes[class_name] = cls
    dataclass_fields.append((snake_name, cls))
    arr.append(cls)

  option_groups.append(OptionGroup(group_name, arr))

Vex2Options = make_dataclass("Vex2Options", dataclass_fields, bases=(PerGameCommonOptions,))
