from __future__ import annotations

from functools import reduce

from rule_builder.rules import Has, Rule, True_

from worlds.AutoWorld import World

from ._progression import PROG
from .locations import LOCATION_NAME_TO_ID


def set_all_rules(world: World) -> None:
  set_all_entrance_rules(world)
  set_all_location_rules(world)
  set_completion_condition(world)


def set_all_entrance_rules(world: World) -> None:
  for i in range(0, 11, 1):
    entrance = world.get_entrance(f"Hub to stage{i}")
    world.set_rule(entrance, Has(f"level:stage{i}"))


def set_all_location_rules(world: World) -> None:
  for node in PROG:
    room = node["room"]
    requires = node.get("requires", [])

    if any(len(_and) == 0 for _and in requires):
      continue

    allConditions: list[Rule[World]] = []
    for _and in requires:
      clean_items: list[str] = list(_and)

      sub_rule: Rule | None = None
      for item in clean_items:
        if item.startswith("flag:starCanBeGot"):
          temprule = Has("flag:starCanBeGot", int(item.split("#")[1]))
        else:
          temprule = Has(item)

        sub_rule = temprule if sub_rule is None else (sub_rule & temprule)

      if sub_rule is not None:
        allConditions.append(sub_rule)


    if allConditions:
      rule = reduce(lambda a, s: a | s, allConditions)

      # Only match locations that belong to THIS node's own receive items
      # (not every location that merely shares the same room name - other
      # nodes for the same room have their own, different requirements).
      for itemInfo in node["receive"]:
        if itemInfo.startswith(("level:", "star:", "achievement:", "flag:")):
          loc_name = f"{room} - {itemInfo}"
          if loc_name in LOCATION_NAME_TO_ID or itemInfo.startswith("flag:"):
            location = world.get_location(loc_name)
            world.set_rule(location, rule)






def set_completion_condition(world: World) -> None:
  rule: Rule[World] = True_()
  if world.options.all_stages_complete:
    for i in range(0, 11, 1):
      rule &= Has("flag:beat stage" + str(i))


  world.set_completion_rule(rule)
