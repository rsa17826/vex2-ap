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
      "level:stage1",
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
      "star:1-1",
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
      "star:2-1",
      "star:2-2",
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
      "star:3-1",
      "star:3-2",
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
      "star:4-1",
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
      "star:5-1",
      "star:5-2",
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
      "star:6-1",
      "star:6-2",
      "star:6-3",
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
      "star:7-1",
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
      "level:stage9",
      "flag:beat stage8",
      "star:8-1",
      "star:8-2",
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
      "level:stage10",
      "flag:beat stage9",
      "star:9-1",
      "star:9-2",
      "star:9-3",
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
      "level:stage11",
      "flag:beat stage10",
      "star:10-1",
      "star:10-2",
      "star:10-3",
    ],
  },
  {
    "room": "stage11",
    "requires": [
      [
        "level:stage11",
      ],
    ],
    "receive": [
      "star:11-1",
      "star:11-2",
      "star:11-3",
      "star:11-4",
      "star:11-5",
      "star:11-6",
      "flag:beat stage11",
    ],
  },
]
