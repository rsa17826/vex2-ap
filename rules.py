from __future__ import annotations

from functools import reduce

from rule_builder.rules import Has, Rule, True_
from worlds.AutoWorld import World

from ._progression import PROG


def set_all_rules(world: World) -> None:
  set_all_entrance_rules(world)
  set_all_location_rules(world)
  set_completion_condition(world)


def set_all_entrance_rules(_world: World) -> None:
  pass


from .locations import LOCATION_NAME_TO_ID


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
        temprule = Has(item)
        sub_rule = temprule if sub_rule is None else (sub_rule & temprule)

      if sub_rule is not None:
        allConditions.append(sub_rule)


    if allConditions:
      rule = reduce(lambda a, s: a | s, allConditions)

      # Determine all target location names for this room/node
      loc_names: list[str] = []

      # 1. Regular location for this room (if it exists)
      if room in LOCATION_NAME_TO_ID:
        loc_names.append(room)

      # 2. Any event locations created in this room
      for itemInfo in node["receive"]:
        if itemInfo.startswith("flag:"):
          loc_names.append(f"{room} - {itemInfo}")


      for loc_name in loc_names:
        location = world.get_location(loc_name)
        world.set_rule(location, rule)




def set_completion_condition(world: World) -> None:
  rule: Rule[World] = True_()
  if world.options.all_stages_complete:
    for i in range(1, 11, 1):
      rule &= Has("flag:beat stage" + str(i))


  world.set_completion_rule(rule)
