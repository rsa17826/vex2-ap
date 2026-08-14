from collections.abc import Mapping
from typing import Any, ClassVar, cast, override

from Options import PerGameCommonOptions

from worlds.AutoWorld import WebWorld, World

from . import items, locations, regions, rules, web_world
from . import options as Vex2_options


class Vex2World(World):
  """
  TODO -
  """

  topology_present = True
  # The docstring should contain a description of the game, to be displayed on the WebHost.

  # You must override the "game" field to say the name of the game.
  game: ClassVar[str] = "Vex2"

  # The WebWorld is a definition class that governs how this world will be displayed on the website.
  web: ClassVar[WebWorld] = web_world.Vex2WebWorld()

  # This is how we associate the options defined in our options.py with our world.
  # (Note: options.py has been imported as "Vex2_options" at the top of this file to avoid a name conflict)
  options_dataclass: ClassVar[type[PerGameCommonOptions]] = cast(type[PerGameCommonOptions], Vex2_options.Vex2Options)
  options: Vex2_options.Vex2Options
  er_pairings: ClassVar[list[tuple[str, str]]] = []
  # Our world class must have a static location_name_to_id and item_name_to_id defined.
  # We define these in regions.py and items.py respectively, so we just set them here.
  location_name_to_id: ClassVar[dict[str, int]] = locations.LOCATION_NAME_TO_ID
  item_name_to_id: ClassVar[dict[str, int]] = items.ITEM_NAME_TO_ID

  # There is always one region that the generator starts from & assumes you can always go back to.
  # This defaults to "Menu", but you can change it by overriding origin_region_name.
  origin_region_name: str = "hub"

  # Our world class must have certain functions ("steps") that get called during generation.
  # The main ones are: create_regions, set_rules, create_items.
  # For better structure and readability, we put each of these in their own file.
  @override
  def create_regions(self) -> None:
    regions.create_and_connect_regions(self)
    locations.create_all_locations(self)

  @override
  def set_rules(self) -> None:
    rules.set_all_rules(self)

  @override
  def create_items(self) -> None:
    items.create_all_items(self)

  # Our world class must also have a create_item function that can create any one of our items by name at any time.
  # We also put this in a different file, the same one that create_items is in.
  @override
  def create_item(self, name: str) -> items.Vex2Item:
    return items.create_item_with_correct_classification(self, name)

  # For features such as item links and panic-method start inventory, AP may ask your world to create extra filler.
  # The way it does this is by calling get_filler_item_name.
  # For this purpose, your world *must* have at least one infinitely repeatable item (usually filler).
  # You must override this function and return this infinitely repeatable item's name.
  # In our case, we defined a function called get_random_filler_item_name for this purpose in our items.py.
  @override
  def get_filler_item_name(self) -> str:
    return items.get_random_filler_item_name(self)

  # There may be data that the game client will need to modify the behavior of the game.
  # This is what slot_data exists for. Upon every client connection, the slot's slot_data is sent to the client.
  # slot_data is just a dictionary using basic types, that will be converted to json when sent to the client.
  @override
  def fill_slot_data(self) -> Mapping[str, Any]:
    from .items import ITEM_NAME_TO_ID

    return {
      **self.options.as_dict(*Vex2_options.option_presets["main"].keys()),
      "roomData": getattr(self, "_mq_table_js", []),
      "AP_ITEM_IDS": {v: k for k, v in ITEM_NAME_TO_ID.items()},
      "AP_LOCATION_IDS": {loc.name: loc.address for loc in self.multiworld.get_locations(self.player) if loc.address is not None},
    }

