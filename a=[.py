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
  "0-0": [
    [
      "move:walljump",
      "move:bounce",
      "move:slide",
    ],
  ],
  "0-win": [
    [
      "move:walljump",
      "move:bounce",
      "move:slide",
    ],
  ],
  #
  "1-0": [
    [
    ],
  ],
  "1-1": [
    [
      "move:walljump",
    ],
  ],
  "1-2": [
    [
      "move:walljump",
      "move:lever",
      "move:bounce",
    ],
  ],
  "1-win": [
    [
      "move:walljump",
      "move:lever",
    ],
  ],
  #
  "2-0": [
    [
      "move:walljump",
      "move:swim",
      "move:bounce",
    ],
  ],
  "2-1": [
    [
      "move:walljump",
      "move:swim",
    ],
  ],
  "2-win": [
    [
      "move:walljump",
      "move:swim",
      "move:bounce",
    ],
  ],
  # NOTE all lv 3 can be fully done without hitting any checkpoints - add check for doing this
  "3-0": [
    [
      "move:lever",
      "move:polejump",
    ],
    [
      "move:lever",
      "move:walljump",
    ],
  ],
  "3-1": [
    [
      "move:lever",
      "move:cannon",
      "move:polejump",
    ],
    [
      "move:lever",
      "move:cannon",
      "move:walljump",
    ],
  ],
  "3-win": [
    [
      "move:lever",
      "move:walljump",
      "move:cannon",
    ],
  ],
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
    [
    ],
  ],
  "10-1": [
    [
    ],
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
    ],
  ],
  "10-4": [
    [
      "move:walljump",
    ],
  ],
  "10-5": [
    [
      "WIN",
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
    ],
    [
      "move:portal",
    ],
  ],
}
