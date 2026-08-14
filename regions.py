from __future__ import annotations

from rule_builder.rules import Has, Rule

from worlds.AutoWorld import World

from .locations import LOCATION_NAME_TO_ID


def _reqs_to_rule(world: World, reqs: list[list[str]]) -> Rule | None:
  if any(len(option) == 0 for option in reqs):
    return None

  rule: Rule | None = None
  for option in reqs:
    sub_rule: Rule | None = None
    for item in option:
      temprule = Has(item)
      if sub_rule is None:
        sub_rule = temprule
      else:
        sub_rule = sub_rule & temprule


    assert sub_rule is not None
    rule = sub_rule if rule is None else (rule | sub_rule)

  return rule


from BaseClasses import Region


def create_and_connect_regions(world: World) -> None:
  print(LOCATION_NAME_TO_ID, "LOCATION_NAME_TO_ID")
  for loc in LOCATION_NAME_TO_ID.keys():
    world.multiworld.regions.append(Region(loc, world.player, world.multiworld))

