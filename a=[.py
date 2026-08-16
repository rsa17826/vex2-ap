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
  #
  #
  #
  #
  #
  #
  #
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
