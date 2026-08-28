import sys, json, os

os.chdir("/home/nyix/projects/Archipelago")
sys.path.insert(0, os.getcwd())

from worlds.AutoWorldRegister import AutoWorldRegister
from BaseClasses import MultiWorld
from rule_builder.rules import Rule

GAME = "Vex 2" # your apworld's game name


def serialize_rule(rule):
  if rule is None:
    return None

  if not isinstance(rule, Rule):
    return _serialize_value(rule)

  out = {"type": type(rule).__name__}
  for k, v in vars(rule).items():
    if k.startswith("_"):
      continue

    out[k] = _serialize_value(v)

  return out


def _serialize_value(v):
  if isinstance(v, Rule):
    return serialize_rule(v)

  if isinstance(v, (list, tuple, set, frozenset)):
    return [_serialize_value(x) for x in v]

  if isinstance(v, dict):
    return {str(k): _serialize_value(x) for k, x in v.items()}

  if isinstance(v, (str, int, float, bool)) or v is None:
    return v

  if hasattr(v, "name"): # enums / ItemClassification etc
    return v.name

  return str(v)


def build_world():
  world_type = AutoWorldRegister.world_types[GAME]
  multiworld = MultiWorld(1)
  multiworld.game[1] = GAME
  multiworld.player_name[1] = "Tracker"
  # set default options for player 1 - adjust to your options class
  from Options import Toggle

  for opt_key, opt_cls in world_type.options_dataclass.type_hints.items():
    multiworld.set_options

  world = world_type(multiworld, 1)
  world.generate_early()
  world.create_regions()
  world.create_items()
  world.set_rules()
  return multiworld, world


def dump(multiworld, world):
  data = {"game": GAME, "regions": {}, "locations": {}, "entrances": {}}

  for region in multiworld.get_regions(1):
    data["regions"][region.name] = {
      "exits": [e.name for e in region.exits],
      "locations": [l.name for l in region.locations],
    }
    for entrance in region.exits:
      data["entrances"][entrance.name] = {
        "connects_to": entrance.connected_region.name if entrance.connected_region else None,
        "rule": serialize_rule(getattr(entrance, "_rule_obj", None) or entrance.access_rule),
      }


  for loc in multiworld.get_locations(1):
    data["locations"][loc.name] = {
      "region": loc.parent_region.name if loc.parent_region else None,
      "rule": serialize_rule(getattr(loc, "_rule_obj", None) or loc.access_rule),
    }

  return data


if __name__ == "__main__":
  multiworld, world = build_world()
  data = dump(multiworld, world)
  with open("tracker_rules.json", "w") as f:
    json.dump(data, f, indent=2)

  print("wrote tracker_rules.json")
