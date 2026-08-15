from typing import NotRequired, TypedDict


class ProgressionNode(TypedDict):
  room: str
  receive: list[str]
  # requires: NotRequired[list[list[str]]]
  requires: list[list[str]]
  info: NotRequired[str]


PROG: list[ProgressionNode] = [
  {
    "room": "hub",
    "requires": [
      [],
    ],
    "receive": [
      "level:stage0",
      # NOTE any stage
      "achievement:13:NOT A SCRATCH",
      "achievement:21:2ND PLACE",
      "achievement:22:1ST PLACE",
      "achievement:23:PERFECT",
      "achievement:30:MICROWAVE",
    ],
  },
  {
    "room": "hub",
    "requires": [
      [
        "level:stage0",
        "level:stage1",
        "level:stage2",
        "level:stage3",
        "level:stage4",
        "level:stage5",
        "level:stage6",
        "level:stage7",
        "level:stage8",
        "level:stage9",
        "level:stage10",
      ],
    ],
    "receive": [
      "achievement:16:BUZZ LIGHTYEAR",
      "achievement:24:OLYMPIAN",
      "achievement:25:PERFECTIONIST",
      # NOTE don't want to have to do single level 22 times starting rando
      "achievement:26:DOUBLE DOWN",
    ],
  },
  {
    "room": "stage0",
    "requires": [
      [
        "level:stage0",
      ],
    ],
    "receive": [
      "achievement:1:TUTORIAL",
      "achievement:12:VEXIPHOBIA",
      "flag:beat stage0",
      "level:stage1",
      "star:0",
    ],
  },
  {
    "room": "stage1",
    "requires": [
      [
        "level:stage1",
      ],
    ],
    "receive": [
      "achievement:2:ACT 1",
      "flag:beat stage1",
      "level:stage2",
      "star:0",
      "star:1",
      "star:2",
    ],
  },
  {
    "room": "stage2",
    "requires": [
      [
        "level:stage2",
      ],
    ],
    "receive": [
      "achievement:3:ACT 2",
      "flag:beat stage2",
      "level:stage3",
      "star:0",
      "star:1",
    ],
  },
  {
    "room": "stage3",
    "requires": [
      [
        "level:stage3",
      ],
    ],
    "receive": [
      "achievement:4:ACT 3",
      "flag:beat stage3",
      "level:stage4",
      "star:0",
      "star:1",
    ],
  },
  {
    "room": "stage4",
    "requires": [
      [
        "level:stage4",
      ],
    ],
    "receive": [
      "achievement:5:ACT 4",
      "flag:beat stage4",
      "level:stage5",
      "star:0",
    ],
  },
  {
    "room": "stage5",
    "requires": [
      [
        "level:stage5",
      ],
    ],
    "receive": [
      "achievement:6:ACT 5",
      "flag:beat stage5",
      "level:stage6",
      "star:0",
      "star:1",
    ],
  },
  {
    "room": "stage6",
    "requires": [
      [
        "level:stage6",
      ],
    ],
    "receive": [
      "achievement:7:ACT 6",
      "flag:beat stage6",
      "level:stage7",
      "star:0",
      "star:1",
      "star:2",
    ],
  },
  {
    "room": "stage7",
    "requires": [
      [
        "level:stage7",
      ],
    ],
    "receive": [
      "achievement:8:ACT 7",
      "flag:beat stage7",
      "level:stage8",
      "star:0",
    ],
  },
  {
    "room": "stage8",
    "requires": [
      [
        "level:stage8",
      ],
    ],
    "receive": [
      "achievement:9:ACT 8",
      "flag:beat stage8",
      "level:stage9",
      "star:0",
      "star:1",
    ],
  },
  {
    "room": "stage9",
    "requires": [
      [
        "level:stage9",
      ],
    ],
    "receive": [
      "achievement:10:ACT 9",
      "flag:beat stage9",
      "level:stage10",
      "star:0",
      "star:1",
      "star:2",
    ],
  },
  {
    "room": "stage10",
    "requires": [
      [
        "level:stage10",
      ],
    ],
    "receive": [
      "achievement:11:VEXED MUCH?",
      "flag:beat stage10",
      "star:0",
      "star:1",
      "star:2",
      "star:3",
      "star:4",
      "star:5",
    ],
  },
  {
    "room": "hub",
    "requires": [
      [
        "level:stage0",
      ],
    ],
    "receive": [
      "achievement:27:CURB STOMP",
    ],
  },
  {
    "room": "hub",
    "requires": [
      [
        "level:stage1",
      ],
      [
        "level:stage2",
      ],
      [
        "level:stage10",
      ],
    ],
    "receive": [
      "achievement:28:LIFESAVER",
    ],
  },
  {
    "room": "hub",
    "requires": [
      [
        "level:stage10",
      ],
    ],
    "receive": [
      "achievement:29:KEYLOGGER",
    ],
  },
  {
    "room": "hub",
    "requires": [
      [
        # "level:stage10",
      ],
    ],
    "receive": [
      "achievement:20:BLOWN AWAY!",
    ],
  },
]
