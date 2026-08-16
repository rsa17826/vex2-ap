# @regex "(?!move:(?:kick|pulley|portal|cannon|walk|jump|walljump|swim|lever|bounce|slide|polejump|poledrop)")move:[^\n-"]+"
# @errgroup 1
# @info asd
# @endregex

# @regex wall jump
# @replace walljump
# @endregex
a = {
  "": {
    "move:walljump",
    "move:lever",
    "move:bounce",
    "move:slide",
    "move:polejump",
    "move:poledrop",
    "move:swim",
  },
  #
  #
  # NOTE all lv 3 can be fully done without hitting any checkpoints - add check for doing this
  "3-win": [],
  #
  "4-0": [
    [
      "move:swim",
    ],
  ],
  "4-win": [
    [
      "move:swim",
      "move:slide",
      "move:walljump",
    ],
  ],
  #
  "5-0": [
    [
      "move:walljump",
      "move:cannon",
    ],
  ],
  "5-1": [
    [
      "move:cannon",
      "move:lever",
      "move:walljump",
    ],
  ],
  "5-win": [
    [
      "move:cannon",
      "move:portal",
      "move:polejump",
      "move:walljump",
    ],
    [
      "move:cannon",
      "move:lever",
      "move:walljump",
    ],
  ],
  #
  "6-0": [
    [
      "move:walljump",
      "move:swim",
      "move:cannon",
      "move:portal",
      "move:pulley",
    ],
  ],
  "6-1": [
    [
      "move:walljump",
      "move:pulley",
      "move:swim",
    ],
  ],
  "6-2": [
    [
      "move:walljump",
      "move:pulley",
      "move:portal",
      "move:swim",
      "move:cannon",
    ],
  ],
  "6-win": [
    [
      "move:portal",
      "move:walljump",
      "move:pulley",
      "move:swim",
      "move:cannon",
    ],
  ],
  #
  "7-0": [
    [
      "move:kick",
      "move:walljump",
      "move:cannon",
    ],
  ],
  "7-win": [
    [
      "move:kick",
      "move:cannon",
      "move:walljump",
      "move:polejump",
    ],
  ],
  #
  "8-0": [
    [
      "move:lever",
      "move:walljump",
      "move:bounce",
    ],
  ],
  "8-1": [
    [
      "move:lever",
      "move:walljump",
      "move:bounce",
    ],
  ],
  "8-win": [
    [
      "move:lever",
      "move:walljump",
      "move:bounce",
      "move:swim",
      "move:kick",
    ],
  ],
  #
  "9-0": [
    [
      "move:swim",
      "move:slide",
      "move:walljump",
    ],
  ],
  "9-1": [
    [
      "move:slide",
      "move:polejump",
      "move:walljump",
    ],
  ],
  "9-2": [
    [
      "move:slide",
      "move:walljump",
    ],
  ],
  "9-win": [
    [
      "move:slide",
      "move:walljump",
      "move:pulley",
    ],
  ],
  #
  "10-0": [
    [],
  ],
  "10-1": [
    [],
  ],
  "10-2": [
    [
      "move:walljump",
      "move:bounce",
      "move:pulley",
    ],
  ],
  "10-3": [
    [
      "move:cannon",
      "move:swim",
      "move:bounce",
      "move:walljump",
    ],
  ],
  "10-4": [
    [
      # "move:walljump",
    ],
  ],
  "10-5": [
    [
      "move:bounce",
      "move:pulley",
      "move:walljump",
      "move:portal",
    ],
    [
      "move:cannon",
      "move:bounce",
      "move:swim",
      "move:portal",
      "move:walljump",
    ],
    [
      "move:portal",
    ],
  ],
  "10-win": [
    [
      "move:bounce",
      "move:pulley",
      "move:walljump",
      "move:portal",
    ],
    [
      "move:cannon",
      "move:bounce",
      "move:swim",
      "move:portal",
      "move:walljump",
    ],
    [
      "move:portal",
    ],
  ],
}
