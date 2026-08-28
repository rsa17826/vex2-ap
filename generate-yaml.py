#!/usr/bin/env python3

import sys
from pathlib import Path

import yaml

ARCHIPELAGO = Path("~/projects/Archipelago").expanduser()
WORLDS_DIR = ARCHIPELAGO / "worlds"


def yaml_value(value):
  """Convert Archipelago option defaults into YAML-safe values."""
  if isinstance(value, (set, frozenset)):
    return sorted(yaml_value(v) for v in value)

  if isinstance(value, dict):
    return {yaml_value(k): yaml_value(v) for k, v in value.items()}

  if isinstance(value, (list, tuple)):
    return [yaml_value(v) for v in value]

  # Most Archipelago option defaults are ints, strings, bools, etc.
  # If an option contains an Enum-like value, use its value.
  if hasattr(value, "value"):
    return yaml_value(value.value)

  return value


def main():
  if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <world-directory>", file=sys.stderr)
    sys.exit(1)

  name = sys.argv[1]
  world_dir = (WORLDS_DIR / name).resolve()

  if not world_dir.is_dir():
    print(f"World not found: {world_dir}", file=sys.stderr)
    sys.exit(1)

  # Make the Archipelago checkout importable regardless of cwd.
  sys.path.insert(0, str(ARCHIPELAGO))

  try:
    from worlds import AutoWorldRegister

  except Exception as e:
    print(f"Could not load Archipelago worlds: {e}", file=sys.stderr)
    sys.exit(1)

  # Find the registered world whose Python module lives in the
  # directory supplied on the command line.
  world_type = None

  for _game, candidate in AutoWorldRegister.world_types.items():
    candidate_file = getattr(candidate, "__file__", None)

    if candidate_file is None:
      continue

    candidate_dir = Path(candidate_file).resolve().parent

    if candidate_dir == world_dir:
      world_type = candidate
      break


  if world_type is None:
    print(
      f"Could not find a registered world loaded from {world_dir}",
      file=sys.stderr,
    )
    sys.exit(1)

  options = world_type.options_dataclass

  defaults = {}

  for option_name, option in options.type_hints.items():
    defaults[option_name] = yaml_value(option.default)

  output = {
    "name": "Player",
    "game": world_type.game,
    world_type.game: defaults,
  }

  yaml.safe_dump(
    output,
    sys.stdout,
    sort_keys=False,
    default_flow_style=False,
    allow_unicode=True,
  )


if __name__ == "__main__":
  main()
