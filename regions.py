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
  world.multiworld.regions.append(Region("hub", world.player, world.multiworld))
  for i in range(0, 11, 1):
    world.multiworld.regions.append(Region(f"stage{i}", world.player, world.multiworld))

