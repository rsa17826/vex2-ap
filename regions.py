from __future__ import annotations

from rule_builder.rules import Has, Rule

from worlds.AutoWorld import World

from . import game_data as data
from .locations import LOCATION_NAME_TO_ID

from BaseClasses import Region, Entrance


def reqs_to_rule(reqs: list[list[str]] | None) -> Rule | None:
  """Turns an OR-of-AND requirement list (same format used throughout the
  data files) into a Rule. None/empty means "always satisfied", so callers
  should only call world.set_rule() when this returns non-None."""
  if not reqs or any(len(option) == 0 for option in reqs):
    return None

  rule: Rule | None = None
  for option in reqs:
    sub_rule: Rule | None = None
    for item in option:
      temprule = Has(item)
      sub_rule = temprule if sub_rule is None else (sub_rule & temprule)

    assert sub_rule is not None
    rule = sub_rule if rule is None else (rule | sub_rule)

  return rule


def create_and_connect_regions(world: World) -> None:
  for region_name in data.REGIONS:
    region = Region(region_name, world.player, world.multiworld)
    world.multiworld.regions.append(region)

  for conn in data.CONNECTIONS:
    from_region = world.get_region(conn["from_region"])
    to_region = world.get_region(conn["to_region"])
    entrance_name = conn.get("name") or f"{conn['from_region']} -> {conn['to_region']}"

    entrance = Entrance(world.player, entrance_name, from_region)
    from_region.exits.append(entrance)
    entrance.connect(to_region)

