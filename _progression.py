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
      "level:stage1",
      "flag:beat stage0",
      "star:1-0",
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
      "level:stage2",
      "flag:beat stage1",
      "star:2-0",
      "star:2-1",
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
      "level:stage3",
      "flag:beat stage2",
      "star:3-0",
      "star:3-1",
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
      "level:stage4",
      "flag:beat stage3",
      "star:4-0",
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
      "level:stage5",
      "flag:beat stage4",
      "star:5-0",
      "star:5-1",
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
      "level:stage6",
      "flag:beat stage5",
      "star:6-0",
      "star:6-1",
      "star:6-2",
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
      "level:stage7",
      "flag:beat stage6",
      "star:7-0",
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
      "level:stage8",
      "flag:beat stage7",
      "star:8-0",
      "star:8-1",
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
      "level:stage09",
      "flag:beat stage8",
      "star:9-0",
      "star:9-1",
      "star:9-2",
    ],
  },
  {
    "room": "stage09",
    "requires": [
      [
        "level:stage09",
      ],
    ],
    "receive": [
      "level:stage10",
      "flag:beat stage09",
      "star:10-0",
      "star:10-1",
      "star:10-2",
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
      "star:11-0",
      "star:11-1",
      "star:11-2",
      "star:11-3",
      "star:11-4",
      "star:11-5",
      "flag:beat stage10",
    ],
  },
]
