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


def addItem(itemInfo: str):
  global _id_counter
  ITEM_COUNTS[itemInfo] = ITEM_COUNTS.get(itemInfo, 0) + 1
  if itemInfo not in ITEM_NAME_TO_ID:
    if itemInfo.startswith(("level:", "move:")):
      DEFAULT_ITEM_CLASSIFICATIONS[itemInfo] = ItemClassification.progression
      ITEM_NAME_TO_ID[itemInfo] = _id_counter
      _id_counter += 1
    elif itemInfo.startswith(("flag:", "star:", "achievement:")):
      return
    else:
      print(itemInfo, "not used")



for item in (
  "move:bounce",
  "move:cannon",
  "move:kick",
  "move:lever",
  "move:polejump",
  "move:portal",
  "move:pulley",
  "move:slide",
  "move:swim",
  "move:walljump",
):
  addItem(item)


for thing in PROG:
  if "receive" in thing:
    for itemInfo in thing["receive"]:
      addItem(itemInfo)



print(ITEM_NAME_TO_ID, "ITEM_NAME_TO_ID")


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
    if k.startswith(("trap:", "filler:", "star:")):
      continue

    count = ITEM_COUNTS.get(k, 1)
    itempool.extend(world.create_item(k) for _ in range(count))

  number_of_items = len(itempool)
  number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
  needed_number_of_filler_items = number_of_unfilled_locations - number_of_items

  itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]
  world.multiworld.itempool += itempool
