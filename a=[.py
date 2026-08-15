# @regex "(?!move:|move:walk|move:jump|move:walljump|move:swim|move:lever|move:bounce|move:slide|move:pole jump|move:pole drop)[^\s-"]+"
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
    "move:pole jump",
    "move:pole drop",
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
  #
  "3-0": [
    [
      "move:walk",
      "move:jump",
      "move:lever",
      "move:pole jump",
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
      "move:pole jump",
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
      "move:",
    ],
  ],
  "4-win": [
    [
      "move:walk",
      "move:jump",
      "move:",
    ],
  ],
  #
  "5-0": [
    [
      "move:walk",
      "move:jump",
      "move:",
    ],
  ],
  "5-1": [
    [
      "move:walk",
      "move:jump",
      "move:",
    ],
  ],
  "5-win": [
    [
      "move:walk",
      "move:jump",
      "move:",
    ],
  ],
  #
  "6-0": [
    [
      "move:walk",
      "move:jump",
      "move:",
    ],
  ],
  "6-1": [
    [
      "move:walk",
      "move:jump",
      "move:",
    ],
  ],
  "6-2": [
    [
      "move:walk",
      "move:jump",
      "move:",
    ],
  ],
  "6-win": [
    [
      "move:walk",
      "move:jump",
      "move:",
    ],
  ],
  #
  "7-0": [
    [
      "move:walk",
      "move:jump",
      "move:",
    ],
  ],
  "7-win": [
    [
      "move:walk",
      "move:jump",
      "move:",
    ],
  ],
  #
  "8-0": [
    [
      "move:walk",
      "move:jump",
      "move:",
    ],
  ],
  "8-1": [
    [
      "move:walk",
      "move:jump",
      "move:",
    ],
  ],
  "8-win": [
    [
      "move:walk",
      "move:jump",
      "move:",
    ],
  ],
  #
  "9-0": [
    [
      "move:walk",
      "move:jump",
      "move:",
    ],
  ],
  "9-1": [
    [
      "move:walk",
      "move:jump",
      "move:",
    ],
  ],
  "9-2": [
    [
      "move:walk",
      "move:jump",
      "move:",
    ],
  ],
  "9-win": [
    [
      "move:walk",
      "move:jump",
      "move:",
    ],
  ],
  #
  "10-0": [
    [
      "move:walk",
      "move:jump",
      "move:",
    ],
  ],
  "10-1": [
    [
      "move:walk",
      "move:jump",
      "move:",
    ],
  ],
  "10-2": [
    [
      "move:walk",
      "move:jump",
      "move:",
    ],
  ],
  "10-3": [
    [
      "move:walk",
      "move:jump",
      "move:",
    ],
  ],
  "10-4": [
    [
      "move:walk",
      "move:jump",
      "move:",
    ],
  ],
  "10-5": [
    [
      "move:walk",
      "move:jump",
      "move:",
    ],
  ],
}
