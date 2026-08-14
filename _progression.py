from typing import NotRequired, TypedDict


class ProgressionNode(TypedDict):
  receive: list[str]
  # requires: NotRequired[list[list[str]]]
  requires: list[list[str]]
  info: NotRequired[str]


PROG: list[ProgressionNode] = [
  {
    "requires": [
      [],
    ],
    "receive": [
      "stage1",
    ],
  },
  {
    "requires": [
      [
        "stage1",
      ],
    ],
    "receive": [
      "stage2",
    ],
  },
  {
    "requires": [
      [
        "stage2",
      ],
    ],
    "receive": [
      "stage3",
    ],
  },
  {
    "requires": [
      [
        "stage3",
      ],
    ],
    "receive": [
      "stage4",
    ],
  },
  {
    "requires": [
      [
        "stage4",
      ],
    ],
    "receive": [
      "stage5",
    ],
  },
  {
    "requires": [
      [
        "stage5",
      ],
    ],
    "receive": [
      "stage6",
    ],
  },
  {
    "requires": [
      [
        "stage6",
      ],
    ],
    "receive": [
      "stage7",
    ],
  },
  {
    "requires": [
      [
        "stage7",
      ],
    ],
    "receive": [
      "stage8",
    ],
  },
  {
    "requires": [
      [
        "stage8",
      ],
    ],
    "receive": [
      "stage9",
    ],
  },
  {
    "requires": [
      [
        "stage9",
      ],
    ],
    "receive": [
      "stage10",
    ],
  },
  {
    "requires": [
      [
        "stage10",
      ],
    ],
    "receive": [
      "stage11",
    ],
  },
]
