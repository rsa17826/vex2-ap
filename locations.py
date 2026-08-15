from __future__ import annotations

from ._progression import PROG
from BaseClasses import Location

from worlds.AutoWorld import World

LOCATION_NAME_TO_ID: dict[str, int] = {}

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
  for locationName, location_id in LOCATION_NAME_TO_ID.items():
    location = Vex2Location(
      world.player,
      locationName,
      location_id,
      world.get_region(thing["room"]),
    )
    world.get_region(thing["room"]).locations.append(location)


def create_events(world: World) -> None:
  from .items import Vex2Item

  starcount = [1, 3, 2, 2, 1, 2, 3, 1, 2, 3, 6]
  for room in range(0, 11, 1):
    for i in range(0, starcount[room] - 1, 1):
      print(room, i)
      _ = world.get_region("hub").add_event(
        location_name=f"{room} - star#{i}",
        item_name="flag:starCanBeGot",
        location_type=Vex2Location,
        item_type=Vex2Item,
      )


  for thing in PROG:
    for itemInfo in thing["receive"]:
      if itemInfo.startswith(("flag:",)):
        event_name = itemInfo

        _ = world.get_region(thing["room"]).add_event(
          location_name=f"{thing['room']} - {event_name}",
          item_name=event_name,
          location_type=Vex2Location,
          item_type=Vex2Item,
        )



