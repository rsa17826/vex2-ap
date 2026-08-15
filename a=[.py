# @regex "(?!move:(?:kick|pulley|portal|cannon|walk|jump|walljump|swim|lever|bounce|slide|polejump|poledrop)")move:[^\n-"]+"
# @errgroup 1
# @info asd
# @endregex

# @regex wall jump
# @replace walljump
# @endregex
a = {
  "": {
    "move:walk",
    "move:jump",
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
      "move:walk",
      "move:jump",
      "move:walljump",
      "move:bounce",
      "move:slide",
    ],
  ],
  "0-win": [
    [
      "move:walk",
      "move:jump",
      "move:walljump",
      "move:bounce",
      "move:slide",
    ],
  ],
  #
  "1-0": [
    [
      "move:walk",
      "move:jump",
    ],
  ],
  "1-1": [
    [
      "move:walk",
      "move:jump",
      "move:walljump",
    ],
  ],
  "1-2": [
    [
      "move:walk",
      "move:jump",
      "move:walljump",
      "move:lever",
    ],
  ],
  "1-win": [
    [
      "move:walk",
      "move:jump",
      "move:walljump",
      "move:lever",
    ],
  ],
  #
  "2-0": [
    [
      "move:walk",
      "move:jump",
      "move:walljump",
      "move:swim",
      "move:bounce",
    ],
  ],
  "2-1": [
    [
      "move:walk",
      "move:jump",
      "move:walljump",
      "move:swim",
    ],
  ],
  "2-win": [
    [
      "move:walk",
      "move:jump",
      "move:walljump",
      "move:swim",
      "move:bounce",
    ],
  ],
  # NOTE all lv 3 can be fully done without hitting any checkpoints - add check for doing this
  "3-0": [
    [
      "move:walk",
      "move:jump",
      "move:lever",
      "move:polejump",
    ],
    [
      "move:walk",
      "move:jump",
      "move:lever",
      "move:walljump",
    ],
  ],
  "3-1": [
    [
      "move:walk",
      "move:jump",
      "move:lever",
      "move:polejump",
    ],
    [
      "move:walk",
      "move:jump",
      "move:lever",
      "move:walljump",
    ],
  ],
  "3-win": [
    [
      "move:walk",
      "move:jump",
      "move:lever",
      "move:walljump",
    ],
  ],
  #
  "4-0": [
    [
      "move:walk",
      "move:jump",
      "move:swim",
    ],
  ],
  "4-win": [
    [
      "move:walk",
      "move:jump",
      "move:swim",
      "move:slide",
      "move:walljump",
    ],
  ],
  #
  "5-0": [
    [
      "move:walk",
      "move:jump",
      "move:walljump",
      "move:cannon",
      "move:walljump",
    ],
  ],
  "5-1": [
    [
      "move:walk",
      "move:jump",
      "move:cannon",
      "move:lever",
      "move:walljump",
    ],
  ],
  "5-win": [
    [
      "move:walk",
      "move:jump",
      "move:cannon",
      "move:portal",
      "move:polejump",
      "move:walljump",
    ],
    [
      "move:walk",
      "move:jump",
      "move:cannon",
      "move:lever",
      "move:walljump",
    ],
  ],
  #
  "6-0": [
    [
      "move:walk",
      "move:jump",
      "move:walljump",
      "move:swim",
      "move:cannon",
    ],
  ],
  "6-1": [
    [
      "move:walk",
      "move:jump",
      "move:walljump",
      "move:swim",
    ],
  ],
  "6-2": [
    [
      "move:walk",
      "move:jump",
      "move:walljump",
      "move:swim",
      "move:cannon",
    ],
  ],
  "6-win": [
    [
      "move:walk",
      "move:jump",
      "move:walljump",
      "move:swim",
      "move:cannon",
    ],
  ],
  #
  "7-0": [
    [
      "move:walk",
      "move:jump",
      "move:kick",
      "move:walljump",
    ],
  ],
  "7-win": [
    [
      "move:walk",
      "move:jump",
      "move:kick",
      "move:walljump",
      "move:polejump",
    ],
  ],
  #
  "8-0": [
    [
      "move:walk",
      "move:jump",
      "move:lever",
      "move:walljump",
      "move:bounce",
    ],
  ],
  "8-1": [
    [
      "move:walk",
      "move:jump",
      "move:lever",
      "move:walljump",
      "move:bounce",
    ],
  ],
  "8-win": [
    [
      "move:walk",
      "move:jump",
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
      "move:walk",
      "move:jump",
      "move:swim",
      "move:slide",
      "move:walljump",
    ],
  ],
  "9-1": [
    [
      "move:walk",
      "move:jump",
      "move:slide",
      "move:walljump",
      "move:polejump",
    ],
  ],
  "9-2": [
    [
      "move:walk",
      "move:jump",
      "move:slide",
      "move:walljump",
    ],
  ],
  "9-win": [
    [
      "move:walk",
      "move:jump",
      "move:slide",
      "move:walljump",
    ],
  ],
  #
  "10-0": [
    [
      "move:walk",
      "move:jump",
    ],
  ],
  "10-1": [
    [
      "move:walk",
      "move:jump",
    ],
  ],
  "10-2": [
    [
      "move:walk",
      "move:jump",
      "move:walljump",
      "move:bounce",
      "move:pulley",
    ],
  ],
  "10-3": [
    [
      "move:walk",
      "move:jump",
      "move:cannon",
      "move:swim",
    ],
  ],
  "10-4": [
    [
      "move:walk",
      "move:jump",
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
      "move:walk",
      "move:jump",
      "move:bounce",
      "move:pulley",
      "move:walljump",
      "move:portal",
    ],
    [
      "move:walk",
      "move:jump",
      "move:cannon",
      "move:bounce",
      "move:swim",
      "move:portal",
    ],
    [
      "move:walk",
      "move:jump",
      "move:portal",
    ],
  ],
}
