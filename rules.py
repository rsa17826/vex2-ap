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


def set_all_location_rules(world: World) -> None:
  for node in PROG:
    if "receive" not in node:
      continue

    for itemInfo in node["receive"]:
      loc_names: list[str] = [f"{itemInfo}"]
      requires = node.get("requires", [])

      if any(len(_and) == 0 for _and in requires):
        continue

      allConditions: list[Rule[World]] = []
      for _and in requires:
        clean_items: list[str] = [token for token in _and]

        sub_rule: Rule | None = None
        for item in clean_items:
          temprule = Has(item)
          sub_rule = temprule if sub_rule is None else (sub_rule & temprule)

        if sub_rule is not None:
          allConditions.append(sub_rule)


      if allConditions:
        rule = reduce(lambda a, s: a | s, allConditions)
        for loc_name in loc_names:
          location = world.get_location(loc_name)
          world.set_rule(location, rule)





def set_completion_condition(world: World) -> None:
  rule: Rule[World] = True_()
  if world.options.all_stages_complete:
    for i in range(1, 11, 1):
      rule &= Has("flag:beat stage" + str(i))


  world.set_completion_rule(rule)
