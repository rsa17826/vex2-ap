#!/usr/bin/env bash
# rank_starting_items.sh
#
# For each candidate item, forces it onto a target free location (via
# items.py's FORCED_ITEMS dict), runs the fuzzer RUNS times, and records the
# Success/Failures counts. Ranks candidates by lowest failure count and
# prints inverse-failure weights suitable for weighted random selection.
#
# Run this from the Archipelago repo root's worlds/vex2 directory, or adjust
# WORLD_DIR below.
set -euo pipefail

WORLD_DIR="."
ITEMS_FILE="${WORLD_DIR}/items.py"
RUNS=1000
JOBS=12

# Candidates to test as the forced item for hub - level:stage0
STAGE0_CANDIDATES=(
  "move:walljump" "move:bounce" "move:slide" "move:swim" "move:lever"
  "move:cannon" "move:kick" "move:polejump" "move:portal" "move:pulley"
  "level:stage0"
  "level:stage1"
  "level:stage2"
  "level:stage3"
  "level:stage4"
  "level:stage5"
  "level:stage6"
  "level:stage7"
  "level:stage8"
  "level:stage9"
  "level:stage10"
)

# Set true to also sweep achievement:30:MICROWAVE (runs on top of whatever
# STAGE0_BEST_ITEM you lock in first -- see main())
SWEEP_MICROWAVE=false
MICROWAVE_CANDIDATES=(
  "move:walljump" "move:bounce" "move:slide"
)

declare -A RESULTS # key: "<receive>::<item>" -> "success failures"

backup_files() {
  cp "$ITEMS_FILE" "${ITEMS_FILE}.bak"
}

restore_files() {
  if [[ -f "${ITEMS_FILE}.bak" ]]; then
    mv "${ITEMS_FILE}.bak" "$ITEMS_FILE"
  fi
}
trap restore_files EXIT

# Rewrites the FORCED_ITEMS dict body in items.py to contain exactly the
# given set of (room, receive) -> item entries.
# Args: alternating room receive item triples, e.g.:
#   set_forced_items "hub" "level:stage0" "move:walljump" "hub" "achievement:30:MICROWAVE" "move:bounce"
set_forced_items() {
  python3 - "$ITEMS_FILE" "$@" <<'EOF'
import re, sys

path = sys.argv[1]
triples = sys.argv[2:]
assert len(triples) % 3 == 0, "expected room/receive/item triples"

entries = []
for i in range(0, len(triples), 3):
    room, receive, item = triples[i], triples[i + 1], triples[i + 2]
    entries.append(f'  ("{room}", "{receive}"): "{item}",')

with open(path) as f:
    content = f.read()

new_block = "FORCED_ITEMS: dict[tuple[str, str], str] = {\n" + "\n".join(entries) + ("\n" if entries else "") + "}"

pattern = re.compile(r"FORCED_ITEMS: dict\[tuple\[str, str\], str\] = \{.*?\}", re.DOTALL)
if not pattern.search(content):
    raise SystemExit("FORCED_ITEMS dict not found in items.py -- has the file been edited?")

content = pattern.sub(new_block, content, count=1)

with open(path, "w") as f:
    f.write(content)
EOF
}

run_fuzz() {
  # Runs from the Archipelago repo root (two levels up from worlds/vex2).
  (python3.13 ../../fuzz.py -r "$RUNS" -j "$JOBS" -g vex2 -n 1) 2>&1 || :
}

parse_counts() {
  local out="$1"
  local success failures
  success=$(cat ./fuzz_output/report.json | jq '.stats.success')
  failures=$(cat ./fuzz_output/report.json | jq '.stats.failure')
  echo "${success:-0} ${failures:-0}"
}

sweep_slot() {
  # Args: room receive candidate1 candidate2 ...
  local slot_room="$1" slot_receive="$2"
  shift 2
  local candidates=("$@")

  echo "=== Sweeping forced item for ${slot_room} - ${slot_receive} ===" >&2
  for item in "${candidates[@]}"; do
    echo "--- Testing ${item} ---" >&2
    set_forced_items "$slot_room" "$slot_receive" "$item"

    local out success failures
    out=$(run_fuzz)
    read -r success failures <<<"$(parse_counts "$out")"

    echo "  Success: ${success}  Failures: ${failures}" >&2
    RESULTS["${slot_receive}::${item}"]="${success} ${failures}"
  done
}

print_ranking() {
  local slot_receive="$1"
  shift
  local candidates=("$@")

  echo ""
  echo "=== Ranking for ${slot_receive} (lowest failures first) ==="
  for item in "${candidates[@]}"; do
    local key="${slot_receive}::${item}"
    local vals="${RESULTS[$key]:-0 9999}"
    local failures="${vals#* }"
    echo "${failures} ${item}"
  done | sort -n | awk '{printf "  %-20s failures=%-6s\n", $2, $1}'
}

compute_weights() {
  local slot_receive="$1"
  shift
  local candidates=("$@")

  echo ""
  echo "=== Inverse-failure weights for ${slot_receive} ==="
  echo "  (weight ~ 1 / (failures + 1), normalized -- use for weighted random pick of forced item)"

  local weights_json="["
  local first=true
  for item in "${candidates[@]}"; do
    local key="${slot_receive}::${item}"
    local vals="${RESULTS[$key]:-0 9999}"
    local failures="${vals#* }"
    if $first; then first=false; else weights_json+=","; fi
    weights_json+="[\"$item\",$failures]"
  done
  weights_json+="]"

  python3 - "$weights_json" <<'EOF'
import sys, json

data = json.loads(sys.argv[1])
raw = [(item, 1.0 / (failures + 1)) for item, failures in data]
total = sum(w for _, w in raw)
for item, w in sorted(raw, key=lambda x: -x[1]):
    print(f"  {item:<20} weight={w/total*100:6.2f}%   (failures={dict(data)[item]})")
EOF
}

main() {
  backup_files

  sweep_slot "hub" "level:stage0" "${STAGE0_CANDIDATES[@]}"
  print_ranking "level:stage0" "${STAGE0_CANDIDATES[@]}"
  compute_weights "level:stage0" "${STAGE0_CANDIDATES[@]}"

  if $SWEEP_MICROWAVE; then
    sweep_slot "hub" "achievement:30:MICROWAVE" "${MICROWAVE_CANDIDATES[@]}"
    print_ranking "achievement:30:MICROWAVE" "${MICROWAVE_CANDIDATES[@]}"
    compute_weights "achievement:30:MICROWAVE" "${MICROWAVE_CANDIDATES[@]}"
  fi
}

main "$@"
