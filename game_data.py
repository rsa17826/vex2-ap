"""
Generic per-game data file.

Nothing in here is a built-in "engine" concept -- REGIONS/CONNECTIONS/EVENTS
below describe an arbitrary directed graph of regions, however this
particular game happens to be shaped (a hub with 11 stages, in this case).
A different game with a totally different topology (a linear world, a big
open map, a branching tree, whatever) would just populate these same three
structures differently -- the engine code (locations.py, regions.py,
rules.py, items.py, world.py) never needs to know or care about "stages" or
"hubs" as concepts.

To port these scripts to a different game, this file and `_progression.py`
(the progression/logic node list) are the only things you should need to
edit or replace.

This file runs `validate_config()` at import time. If the same fact is
represented in more than one place and those places disagree (e.g. a
connection references a region that was never declared, or an item required
somewhere is never actually granted anywhere), generation fails loudly with
`DataConsistencyError` instead of silently producing a broken/incorrect
multiworld.
"""

from __future__ import annotations

from typing import NotRequired, TypedDict

from ._progression import PROG


# ---------------------------------------------------------------------------
# Region graph
# ---------------------------------------------------------------------------

# The region the player starts in / can always return to.
ORIGIN_REGION: str = "hub"

# Every region that exists in the world. This is the full node set of the
# graph -- CONNECTIONS below are the edges.
REGIONS: list[str] = ["hub"] + [f"stage{i}" for i in range(11)]


class Connection(TypedDict):
  from_region: str
  to_region: str
  name: NotRequired[str] # entrance name; defaults to "{from_region} -> {to_region}"
  # OR-of-AND requirement groups, same format as _progression.py's "requires".
  # None / [] / [[]] all mean "always open".
  requires: NotRequired[list[list[str]]]


# The directed edges of the region graph. Any topology is fine here: a
# straight line, a hub-and-spoke (as below), a branching tree, a fully
# connected mesh, one-way shortcuts, etc.
CONNECTIONS: list[Connection] = [
  {
    "from_region": "hub",
    "to_region": f"stage{i}",
    "name": f"Hub to stage{i}",
    "requires": [[f"level:stage{i}"]],
  }
  for i in range(11)
]


class EventDef(TypedDict):
  room: str
  location_name: str
  item_name: str
  # OR-of-AND requirement groups. None / [] / [[]] means "always available".
  requires: NotRequired[list[list[str]] | None]


# Standalone logic events that aren't derived from a _progression.py node's
# "receive" list (e.g. per-star "can this star be gotten at all" checks used
# purely for logic gating elsewhere). If a game doesn't need any of these,
# this can just be an empty list.
EVENTS: list[EventDef] = [
  {
    "room": f"stage{stage_index}",
    "location_name": f"stage{stage_index} - star {star_index} can be got",
    "item_name": "flag:starCanBeGot",
    "requires": None,
  }
  for stage_index, star_count in enumerate([1, 3, 2, 2, 1, 2, 3, 1, 2, 3, 6])
  for star_index in range(star_count)
]


# ---------------------------------------------------------------------------
# Item categorization
# ---------------------------------------------------------------------------
# Purely a matter of *string prefix convention* for this game's item/receive
# names -- the engine only ever asks "does this name start with a prefix in
# category X", it never hardcodes what the prefixes themselves are.

# Prefixes for items that get placed as real, shuffled locations.
LOCATION_ITEM_PREFIXES: tuple[str, ...] = ("level:", "star:", "achievement:")

# Prefixes for items that are logic-only events (not real placed locations).
EVENT_ITEM_PREFIXES: tuple[str, ...] = ("flag:",)

# Prefixes for items that go in the real AP item pool as progression items.
POOL_PROGRESSION_PREFIXES: tuple[str, ...] = ("level:", "move:")

# Prefixes for items that are never created as real pool items (they're
# events/locations only, handled elsewhere in the item pool step).
NON_POOL_PREFIXES: tuple[str, ...] = ("flag:", "star:", "achievement:")

# Items that always exist in the item pool regardless of whether they're
# granted by any _progression.py node's "receive" list (e.g. abilities the
# player starts able to find copies of that aren't gated behind a specific
# progression node). Previously called "moves" for this particular game --
# there's nothing move-specific about the mechanism itself.
# NOTE used for all items that are only added in the ap and not origionaly in the game as if not granted in game they wont be in any receives
CORE_ITEMS: tuple[str, ...] = (
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
)

# Filler / trap items. Anything starting with "trap:" is classified as a
# trap, everything else here is classified as ordinary filler.
FILLER_ITEMS: tuple[str, ...] = ("trap:nothing",)

# Some _progression.py "receive" prefixes have a matching standalone
# location declared in EVENTS (e.g. receiving "star:2" should also apply
# that node's rule to the "can this star be got at all" event location).
# Maps receive-prefix -> a format string for the linked event's location
# name, using {room} and {index} (the part of the receive item after the
# prefix, e.g. "2" from "star:2") as placeholders. Purely data -- the engine
# just does template.format(room=..., index=...) and looks the location up.
LINKED_EVENT_TEMPLATES: dict[str, str] = {
  "star:": "{room} - star {index} can be got",
}


# ---------------------------------------------------------------------------
# Completion condition
# ---------------------------------------------------------------------------

# Name of the boolean world option that, when True, gates completion behind
# COMPLETION_REQUIRED_ITEMS. Set to None if completion should never be
# gated by an option (rule is then just always-True).
COMPLETION_OPTION_NAME: str | None = "all_stages_complete"

# Items (ANDed together) required for completion when COMPLETION_OPTION_NAME
# is set and that option is enabled.
COMPLETION_REQUIRED_ITEMS: list[str] = [f"flag:beat stage{i}" for i in range(11)]


# ---------------------------------------------------------------------------
# Early-check weighting (used by generate_early / weight_early_checks option)
# ---------------------------------------------------------------------------

# Locations that get an early, weighted-random item forced onto them.
EARLY_CHECK_LOCATIONS: list[tuple[str, str]] = [
  ("hub", "level:stage0"),
  ("hub", "achievement:30:MICROWAVE"),
]

# (item_name, weight) pairs -- kept together as tuples so the item list and
# its weights can never silently drift out of sync in length/order.
EARLY_CHECK_POOL: list[tuple[str, float]] = [
  ("level:stage10", 64.71),
  ("level:stage1", 11.98),
  ("move:cannon", 1.81),
  ("level:stage5", 1.80),
  ("move:lever", 1.38),
  ("move:portal", 1.30),
  ("level:stage4", 1.30),
  ("move:bounce", 1.28),
  ("move:swim", 1.23),
  ("level:stage9", 1.22),
  ("move:slide", 1.14),
  ("level:stage2", 1.14),
  ("move:walljump", 1.12),
  ("level:stage8", 1.12),
  ("move:pulley", 1.11),
  ("level:stage7", 1.10),
  ("level:stage6", 1.09),
  ("level:stage0", 1.09),
  ("move:polejump", 1.05),
  ("level:stage3", 1.04),
  ("move:kick", 0.97),
]


OPTIONS = {
  "Gameplay": (("all_stages_complete", "game won when all levels have been beaten", True),),
  "?": (
    (
      "weight_early_checks",
      "makes some early checks more likely to have items that unlock more\ncan get gen failures from ~29.2% to ~6.3% (tested over 1000 gens)\npresumably only useful for singleplayer",
      True,
    ),
  ),
  "Win Condition": (
    ("all_achievements", "game only won when all achievement checks obtained", False),
    (
      "death_link",
      "Links your fate to other players in the multiworld.\nWhen enabled, if you die, everyone else on Death Link dies too. If they die, you die. Use with caution!",
      True,
    ),
  ),
}

EXTRA_SLOT_DATA: dict[str, int | float | str] = {}

# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------


class DataConsistencyError(Exception):
  """Raised when the data files disagree with each other about a fact that
  MUST match everywhere it's represented, instead of allowing generation to
  potentially proceed with incorrect/incomplete data."""


def _all_requires_items(requires: list[list[str]] | None) -> set[str]:
  if not requires:
    return set()

  return {item for group in requires for item in group}


def validate_config() -> None:
  errors: list[str] = []
  region_set = set(REGIONS)

  # --- Region graph internal consistency ---
  if ORIGIN_REGION not in region_set:
    errors.append(f"ORIGIN_REGION '{ORIGIN_REGION}' is not declared in REGIONS.")

  for conn in CONNECTIONS:
    for key in ("from_region", "to_region"):
      if conn[key] not in region_set:
        errors.append(f"CONNECTIONS entry {conn} references region '{conn[key]}' not declared in REGIONS.")



  for event in EVENTS:
    if event["room"] not in region_set:
      errors.append(f"EVENTS entry {event} references room '{event['room']}' not declared in REGIONS.")


  seen_event_locations: set[str] = set()
  for event in EVENTS:
    key = f"{event['room']} - {event['location_name']}" if not event["location_name"].startswith(event["room"]) else event["location_name"]
    if event["location_name"] in seen_event_locations:
      errors.append(f"EVENTS declares duplicate location_name '{event['location_name']}'.")

    seen_event_locations.add(event["location_name"])

  # --- _progression.py rooms must be declared regions ---
  for node in PROG:
    if node["room"] not in region_set:
      errors.append(f"_progression.py references unknown room '{node['room']}' not declared in REGIONS.")


  # --- Build the universe of items that are actually ever granted ---
  granted_items: set[str] = set(CORE_ITEMS)
  for node in PROG:
    granted_items.update(node.get("receive", []))

  for event in EVENTS:
    granted_items.add(event["item_name"])

  # --- Every item referenced in a requirement (progression or connection)
  #     must actually be granted somewhere, or it can never be satisfied. ---
  referenced_items: set[str] = set()
  for node in PROG:
    for group in node.get("requires", []):
      referenced_items.update(group)


  for conn in CONNECTIONS:
    referenced_items.update(_all_requires_items(conn.get("requires")))

  for event in EVENTS:
    referenced_items.update(_all_requires_items(event.get("requires")))

  # flag:starCanBeGot#N style items reference the base event item with a
  # "#N" suffix -- strip that before checking membership.
  def _base_name(item: str) -> str:
    return item.split("#", 1)[0]

  ungranted = {item for item in referenced_items if _base_name(item) not in granted_items}
  if ungranted:
    errors.append(
      f"""The following items are required somewhere (in _progression.py
      'requires', a CONNECTIONS requirement, or an EVENTS requirement) but
      are never granted by any _progression.py 'receive', CORE_ITEMS, or
      EVENTS item_name: {sorted(ungranted)}"""
    )

  # --- CORE_ITEMS should not overlap items already granted via PROG receive
  #     under a location/event prefix, since that would double-declare it. ---

  # --- EARLY_CHECK_LOCATIONS must correspond to a real (room, receive) pair. ---
  all_receive_pairs = {(node["room"], item) for node in PROG for item in node.get("receive", [])}
  for room, receive_name in EARLY_CHECK_LOCATIONS:
    if (room, receive_name) not in all_receive_pairs:
      errors.append(f"EARLY_CHECK_LOCATIONS entry ('{room}', '{receive_name}') does not match any (room, receive) pair declared in _progression.py.")


  # --- EARLY_CHECK_POOL items must be real, known items. ---
  early_pool_names = {name for name, _weight in EARLY_CHECK_POOL}
  unknown_pool_items = early_pool_names - granted_items
  if unknown_pool_items:
    errors.append(f"EARLY_CHECK_POOL references unknown item(s): {sorted(unknown_pool_items)}")

  seen: set[str] = set()
  dupes: set[str] = set()
  for name, _weight in EARLY_CHECK_POOL:
    if name in seen:
      dupes.add(name)

    seen.add(name)

  if dupes:
    errors.append(f"EARLY_CHECK_POOL contains duplicate item name(s): {sorted(dupes)}")

  # --- LINKED_EVENT_TEMPLATES must resolve to real EVENTS-declared locations
  #     for every matching receive item in _progression.py. ---
  declared_event_locations = {event["location_name"] for event in EVENTS}
  for node in PROG:
    room = node["room"]
    for itemInfo in node.get("receive", []):
      for prefix, template in LINKED_EVENT_TEMPLATES.items():
        if itemInfo.startswith(prefix):
          index = itemInfo.split(":", 1)[1]
          expected_location = template.format(room=room, index=index)
          if expected_location not in declared_event_locations:
            errors.append(
              f"""_progression.py receive item '{itemInfo}' in room '{room}'
              expects a linked event location '{expected_location}' via
              LINKED_EVENT_TEMPLATES, but no such location is declared in EVENTS."""
            )





  # --- Completion items must actually be granted somewhere. ---
  missing_completion_items = set(COMPLETION_REQUIRED_ITEMS) - granted_items
  if missing_completion_items:
    errors.append(f"COMPLETION_REQUIRED_ITEMS references item(s) never granted anywhere: {sorted(missing_completion_items)}")

  if errors:
    raise DataConsistencyError("Data file consistency check failed -- refusing to generate with potentially incorrect data:\n- " + "\n- ".join(errors))


validate_config()
