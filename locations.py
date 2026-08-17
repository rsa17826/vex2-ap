from __future__ import annotations

from . import game_data as data
from ._progression import PROG
from BaseClasses import Location

from worlds.AutoWorld import World

LOCATION_NAME_TO_ID: dict[str, int] = {}

_id_counter = 1
for thing in PROG:
  if "receive" in thing:
    for itemInfo in thing["receive"]:
      if itemInfo.startswith(data.LOCATION_ITEM_PREFIXES):
        itemName = f"{thing['room']} - {itemInfo}"
        if itemName not in LOCATION_NAME_TO_ID:
          LOCATION_NAME_TO_ID[itemName] = _id_counter
          _id_counter += 1

# NOTE: game_data.EVENTS entries are logic events, not real shuffled
# locations, so they are intentionally NOT added to LOCATION_NAME_TO_ID here
# -- see create_events() below, which uses add_event() the same way
# _progression.py "flag:"-prefixed receives do.


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
      world.get_region(locationName.split(" - ", 1)[0]),
    )
    world.get_region(locationName.split(" - ", 1)[0]).locations.append(location)


def create_events(world: World) -> None:
  from .items import Vex2Item

  # Standalone events declared directly in game_data.py (game-topology
  # specific, but expressed generically -- the engine just walks the list).
  for event in data.EVENTS:
    location_name = event["location_name"]
    if not location_name.startswith(event["room"]):
      location_name = f"{event['room']} - {location_name}"

    _ = world.get_region(event["room"]).add_event(
      location_name=location_name,
      item_name=event["item_name"],
      location_type=Vex2Location,
      item_type=Vex2Item,
    )

  # Events derived from _progression.py "receive" entries flagged as
  # event-only (e.g. "flag:" prefixed items).
  for thing in PROG:
    for itemInfo in thing["receive"]:
      if itemInfo.startswith(data.EVENT_ITEM_PREFIXES):
        event_name = itemInfo

        _ = world.get_region(thing["room"]).add_event(
          location_name=f"{thing['room']} - {event_name}",
          item_name=event_name,
          location_type=Vex2Location,
          item_type=Vex2Item,
        )
