#!/usr/bin/env sh
# ./.venv/bin/pytest --ignore=test/webhost --color=yes |tee ax.ans;tail -n +"$(grep -n "game='Vex2'" a.ans | head -n 2 | tail -n 1 | cut -d: -f1)" a.ans>as.ans&&mv as.ans a.ans&&rm ax.ans
# ./.venv/bin/pytest --ignore=test/webhost --color=no |tee ax.ans;tail -n +"$(grep -n "= short test summary info =" a.ans | head -n 2 | tail -n 1 | cut -d: -f1)" a.ans>as.ans&&mv as.ans a.ans&&rm ax.ans
../../.venv/bin/pytest --ignore=test/webhost --color=yes |
  tee ax.ans
tail -n +"$(grep -n "= short test summary info =" ax.ans |
  head -n 2 |
  tail -n 1 |
  cut -d: -f1)" \
  ax.ans >as.ans &&
  mv as.ans a.ans &&
  rm ax.ans
