from typing import NotRequired, TypedDict


class ProgressionNode(TypedDict):
  room: str
  receive: list[str]
  # requires: NotRequired[list[list[str]]]
  requires: list[list[str]]
  info: NotRequired[str]


PROG: list[ProgressionNode] = [
  {
    "room": "stage1",
    "requires": [
      [],
    ],
    "receive": [
      "level:stage1",
    ],
  },
  {
    "room": "stage2",
    "requires": [
      [
        "level:stage1",
      ],
    ],
    "receive": [
      "level:stage2",
      "flag:beat stage1",
    ],
  },
  {
    "room": "stage3",
    "requires": [
      [
        "level:stage2",
      ],
    ],
    "receive": [
      "level:stage3",
      "flag:beat stage2",
    ],
  },
  {
    "room": "stage4",
    "requires": [
      [
        "level:stage3",
      ],
    ],
    "receive": [
      "level:stage4",
      "flag:beat stage3",
    ],
  },
  {
    "room": "stage5",
    "requires": [
      [
        "level:stage4",
      ],
    ],
    "receive": [
      "level:stage5",
      "flag:beat stage4",
    ],
  },
  {
    "room": "stage6",
    "requires": [
      [
        "level:stage5",
      ],
    ],
    "receive": [
      "level:stage6",
      "flag:beat stage5",
    ],
  },
  {
    "room": "stage7",
    "requires": [
      [
        "level:stage6",
      ],
    ],
    "receive": [
      "level:stage7",
      "flag:beat stage6",
    ],
  },
  {
    "room": "stage8",
    "requires": [
      [
        "level:stage7",
      ],
    ],
    "receive": [
      "level:stage8",
      "flag:beat stage7",
    ],
  },
  {
    "room": "stage9",
    "requires": [
      [
        "level:stage8",
      ],
    ],
    "receive": [
      "level:stage9",
      "flag:beat stage8",
    ],
  },
  {
    "room": "stage10",
    "requires": [
      [
        "level:stage9",
      ],
    ],
    "receive": [
      "level:stage10",
      "flag:beat stage09",
    ],
  },
  {
    "room": "stage11",
    "requires": [
      [
        "level:stage10",
      ],
    ],
    "receive": [
      "level:stage11",
      "flag:beat stage10",
    ],
  },
  {
    "room": "stage12",
    "requires": [
      [
        "level:stage11",
      ],
    ],
    "receive": [
      "flag:beat stage11",
    ],
  },
]
