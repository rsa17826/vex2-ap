from __future__ import annotations

from functools import reduce

from rule_builder.rules import Has, Rule, True_

from worlds.AutoWorld import World

from . import game_data as data
from ._progression import PROG
from .locations import LOCATION_NAME_TO_ID
from .regions import reqs_to_rule


def set_all_rules(world: World) -> None:
  set_all_entrance_rules(world)
  set_all_location_rules(world)
  set_completion_condition(world)


def set_all_entrance_rules(world: World) -> None:
  for conn in data.CONNECTIONS:
    rule = reqs_to_rule(conn.get("requires"))
    if rule is None:
      continue

    entrance_name = conn.get("name") or f"{conn['from_region']} -> {conn['to_region']}"
    entrance = world.get_entrance(entrance_name)
    world.set_rule(entrance, rule)


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

      for itemInfo in node["receive"]:
        if itemInfo.startswith(data.LOCATION_ITEM_PREFIXES + data.EVENT_ITEM_PREFIXES):
          loc_name = f"{room} - {itemInfo}"
          location = world.get_location(loc_name)
          world.set_rule(location, rule)

        for prefix, template in data.LINKED_EVENT_TEMPLATES.items():
          if itemInfo.startswith(prefix):
            index = itemInfo.split(":", 1)[1]
            event_name = template.format(room=room, index=index)
            event_location = world.get_location(event_name)
            world.set_rule(event_location, rule)






def set_completion_condition(world: World) -> None:
  rule: Rule[World] = True_()

  option_name = data.COMPLETION_OPTION_NAME
  if option_name is not None and getattr(world.options, option_name):
    for item in data.COMPLETION_REQUIRED_ITEMS:
      rule &= Has(item)


  world.set_completion_rule(rule)
