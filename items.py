from __future__ import annotations

from BaseClasses import Item, ItemClassification
from worlds.AutoWorld import World

from ._progression import PROG

ITEM_NAME_TO_ID: dict[str, int] = {}
DEFAULT_ITEM_CLASSIFICATIONS: dict[str, ItemClassification] = {}

_id_counter = 99999
fillers = ("trap:nothing",)
for filler in fillers:
  DEFAULT_ITEM_CLASSIFICATIONS[filler] = ItemClassification.trap if filler.startswith("trap:") else ItemClassification.filler
  ITEM_NAME_TO_ID[filler] = _id_counter
  _id_counter -= 1


ITEM_COUNTS: dict[str, int] = {}
_id_counter = 1

for thing in PROG:
  if "receive" in thing:
    for itemInfo in thing["receive"]:
      itemName = itemInfo
      ITEM_COUNTS[itemName] = ITEM_COUNTS.get(itemName, 0) + 1
      if itemName not in ITEM_NAME_TO_ID:
        if itemInfo.startswith(("level:",)):
          DEFAULT_ITEM_CLASSIFICATIONS[itemName] = ItemClassification.progression
          ITEM_NAME_TO_ID[itemName] = _id_counter
          _id_counter += 1
        elif itemInfo.startswith(("flag:",)):
          continue
        else:
          print(itemName, "not used")





class Vex2Item(Item):
  game: str = "Vex2"


def get_random_filler_item_name(world: World) -> str:
  weights = [getattr(world.options, trap.split(":")[1]) for trap in fillers if hasattr(world.options, trap.split(":")[1])]
  if not weights or sum(weights) == 0:
    return "trap:nothing"

  return world.random.choices(fillers, weights=weights, k=1)[0]


def create_item_with_correct_classification(world: World, name: str) -> Vex2Item:
  return Vex2Item(name, DEFAULT_ITEM_CLASSIFICATIONS[name], ITEM_NAME_TO_ID[name], world.player)


def create_all_items(world: World) -> None:
  itempool: list[Item] = []
  for k in ITEM_NAME_TO_ID.keys():
    if k.startswith(("trap:", "filler:")):
      continue

    count = ITEM_COUNTS.get(k, 1)
    itempool.extend(world.create_item(k) for _ in range(count))

  number_of_items = len(itempool)
  number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
  needed_number_of_filler_items = number_of_unfilled_locations - number_of_items

  itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]
  world.multiworld.itempool += itempool
