from __future__ import annotations

from ._progression import PROG
from BaseClasses import Location

from worlds.AutoWorld import World

LOCATION_NAME_TO_ID: dict[str, int] = {
  # "stage1": 2,
  # "stage2": 3,
  # "stage3": 4,
  # "stage4": 5,
  # "stage5": 6,
  # "stage6": 7,
  # "stage7": 8,
  # "stage8": 9,
  # "stage9": 10,
  # "stage10": 11,
  # "stage11": 12,
}


_id_counter = 1
for thing in PROG:
  if "receive" in thing:
    for itemInfo in thing["receive"]:
      if itemInfo.startswith(
        (
          "level:",
          "star:",
          "achievement:",
        )
      ):
        # itemName = itemInfo.split("#")[0]
        itemName = f"{thing['room']} - {itemInfo}"
        if itemName not in LOCATION_NAME_TO_ID:
          LOCATION_NAME_TO_ID[itemName] = _id_counter
          _id_counter += 1





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
  from .items import Vex2Item

  hub_region = world.get_region("hub")
  for thing in PROG:
    for itemInfo in thing["receive"]:
      if itemInfo.startswith(("flag:",)):
        event_name = itemInfo

        _ = hub_region.add_event(
          location_name=f"{thing['room']} - {event_name}",
          item_name=event_name,
          location_type=Vex2Location,
          item_type=Vex2Item,
        )



