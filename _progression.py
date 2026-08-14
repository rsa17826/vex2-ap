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
      "level:stage1",
    ],
  },
  {
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
