from __future__ import annotations

from BaseClasses import Location
from worlds.AutoWorld import World

LOCATION_NAME_TO_ID: dict[str, int] = {
  "hub": 1,
  "stage1": 2,
  "stage2": 3,
  "stage3": 4,
  "stage4": 5,
  "stage5": 6,
  "stage6": 7,
  "stage7": 8,
  "stage8": 9,
  "stage9": 10,
  "stage10": 11,
  "stage11": 12,
}


class Vex2Location(Location):
  game: str = "Vex2"


def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
  return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}


def create_all_locations(world: World) -> None:
  create_regular_locations(world)
  create_events(world)


def create_regular_locations(world: World) -> None:
  hub_region = world.get_region("hub")
  for locationName, location_id in LOCATION_NAME_TO_ID.items():
    location = Vex2Location(
      world.player,
      locationName,
      location_id,
      hub_region,
    )
    hub_region.locations.append(location)


def create_events(world: World) -> None:
  return
