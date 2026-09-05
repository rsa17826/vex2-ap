from __future__ import annotations

from BaseClasses import Item, ItemClassification
from worlds.AutoWorld import World

from . import game_data as data
from ._progression import PROG

ITEM_NAME_TO_ID: dict[str, int] = {}
DEFAULT_ITEM_CLASSIFICATIONS: dict[str, ItemClassification] = {}

# Maps (room, receive-name) -> forced item name.
# e.g. {("hub", "level:stage0"): "move:walljump"} forces move:walljump to be
# placed at the "hub - level:stage0" location instead of whatever the normal
# shuffle would have put there. Populated by external tooling (rank_starting_items.sh)
# via direct edits to this dict, or by hand for manual testing.
FORCED_ITEMS: dict[tuple[str, str], str] = {}

_id_counter = 99999
for filler in data.FILLER_ITEMS:
  DEFAULT_ITEM_CLASSIFICATIONS[filler] = ItemClassification.trap if filler.startswith("trap:") else ItemClassification.filler
  ITEM_NAME_TO_ID[filler] = _id_counter
  _id_counter -= 1


ITEM_COUNTS: dict[str, int] = {}
_id_counter = 1


def addItem(itemInfo: str):
  global _id_counter
  ITEM_COUNTS[itemInfo] = ITEM_COUNTS.get(itemInfo, 0) + 1
  if itemInfo not in ITEM_NAME_TO_ID:
    if itemInfo.startswith(data.POOL_PROGRESSION_PREFIXES):
      DEFAULT_ITEM_CLASSIFICATIONS[itemInfo] = ItemClassification.progression
      ITEM_NAME_TO_ID[itemInfo] = _id_counter
      _id_counter += 1
    elif itemInfo.startswith(data.NON_POOL_PREFIXES):
      return
    else:
      print(itemInfo, "not used")



for item in data.CORE_ITEMS:
  addItem(item)


for thing in PROG:
  if "receive" in thing:
    for itemInfo in thing["receive"]:
      addItem(itemInfo)



# print(ITEM_NAME_TO_ID, "ITEM_NAME_TO_ID")


class Vex2Item(Item):
  game: str = "Vex2"


def get_random_filler_item_name(world: World) -> str:
  weights = [getattr(world.options, trap.split(":")[1]) for trap in data.FILLER_ITEMS if hasattr(world.options, trap.split(":")[1])]
  if not weights or sum(weights) == 0:
    return "trap:nothing"

  return world.random.choices(data.FILLER_ITEMS, weights=weights, k=1)[0]


def create_item_with_correct_classification(world: World, name: str) -> Vex2Item:
  return Vex2Item(name, DEFAULT_ITEM_CLASSIFICATIONS[name], ITEM_NAME_TO_ID[name], world.player)


def place_forced_items(world: World) -> dict[str, int]:
  """
  Locks each item configured in FORCED_ITEMS onto its target location,
  bypassing the normal shuffle for that location.

  Returns a dict of {item_name: number_placed_this_way}, so the caller can
  subtract those counts from what still needs to go in the general pool
  (otherwise the forced item would also get created a second time and either
  overfill the pool or duplicate a progression item).
  """
  placed_counts: dict[str, int] = {}

  for (room, receive_name), forced_item_name in FORCED_ITEMS.items():
    location_name = f"{room} - {receive_name}"
    location = world.get_location(location_name)

    if location.item is not None:
      # Already filled (e.g. by an earlier forced-item entry or an event) -- skip.
      continue

    if forced_item_name not in ITEM_NAME_TO_ID:
      raise ValueError(f"FORCED_ITEMS: unknown item '{forced_item_name}' for {location_name}")

    forced_item = create_item_with_correct_classification(world, forced_item_name)
    location.place_locked_item(forced_item)
    placed_counts[forced_item_name] = placed_counts.get(forced_item_name, 0) + 1

  return placed_counts


def create_all_items(world: World) -> None:
  forced_placed_counts = place_forced_items(world)

  itempool: list[Item] = []
  for k in ITEM_NAME_TO_ID.keys():
    if k.startswith(("trap:", "filler:", "star:")):
      continue

    count = ITEM_COUNTS.get(k, 1) - forced_placed_counts.get(k, 0)
    if count < 0:
      count = 0

    itempool.extend(world.create_item(k) for _ in range(count))

  number_of_items = len(itempool)
  number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
  needed_number_of_filler_items = number_of_unfilled_locations - number_of_items

  itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]
  world.multiworld.itempool += itempool
