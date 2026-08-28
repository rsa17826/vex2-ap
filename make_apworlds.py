"""
Standalone .apworld packager — extracted from setup.py's BuildExeCommand.run(),
but targets the live worlds/ directory instead of a staged build/ copy, and
does NOT delete the source folders afterward.

Usage (from repo root):
    python make_apworlds.py [worldname ...]

With no args, packages every registered world (except those in non_apworlds).
With args, only packages the named world(s) (folder name under worlds/).
"""

import json
import os
import sys
import zipfile
from pathlib import Path

os.chdir("/home/nyix/projects/Archipelago")
sys.path.insert(0, os.getcwd())

from Utils import version_tuple # type: ignore
from worlds.AutoWorld import AutoWorldRegister
from worlds.Files import APWorldContainer

# NOTE: we deliberately do NOT `import setup` — setup.py calls cx_Freeze.setup(...)
# unconditionally at module level (not guarded by `if __name__ == "__main__"`),
# so importing it runs the whole build/argv-parsing machinery. Instead we just
# duplicate the small non_apworlds set (these are games that ship built-in and
# aren't meant to be standalone .apworld files); keep in sync with setup.py if it changes.
non_apworlds: set[str] = {
  "A Link to the Past",
  "Adventure",
  "Archipelago",
  "Lufia II Ancient Cave",
  "Meritous",
  "Ocarina of Time",
  "Overcooked! 2",
  "Raft",
  "Super Mario 64",
  "VVVVVV",
  "Wargroove",
}

OUT_DIR = Path("output") / "apworlds"
OUT_DIR.mkdir(parents=True, exist_ok=True)

only = set(sys.argv[1:])

for worldname, worldtype in AutoWorldRegister.world_types.items():
  if worldname in non_apworlds:
    continue

  world_directory = Path(os.path.dirname(worldtype.__file__))
  file_name = world_directory.name

  if only and file_name not in only and worldname not in only:
    continue

  manifest_file = world_directory / "archipelago.json"
  if manifest_file.is_file():
    with open(manifest_file, "r", encoding="utf-8") as f:
      manifest = json.load(f)

    assert manifest.get("game") == worldtype.game, f"{world_directory}: manifest game ({manifest.get('game')!r}) != World.game ({worldtype.game!r})"
  else:
    manifest = {}

  zip_path = OUT_DIR / f"{file_name}.apworld"
  if zip_path.exists():
    zip_path.unlink()

  apworld = APWorldContainer(str(zip_path))
  # apworld.minimum_ap_version = version_tuple
  # apworld.maximum_ap_version = version_tuple
  apworld.game = worldtype.game
  manifest.update(apworld.get_manifest())
  apworld.manifest_path = f"{file_name}/archipelago.json"

  # honor .apignore in the world directory if present (gitignore-style patterns)
  ignore_patterns: list[str] = []
  apignore_path = world_directory / ".apignore"
  if apignore_path.is_file():
    with open(apignore_path, "r", encoding="utf-8") as f:
      ignore_patterns = [line.strip() for line in f if line.strip() and not line.strip().startswith("#")]


  def is_ignored(rel: str) -> bool:
    for pat in ignore_patterns:
      pat = pat.rstrip("/")
      if pat and (rel == pat or rel.startswith(pat + "/") or Path(rel).match(pat)):
        return True


    return False

  with zipfile.ZipFile(zip_path, "x", zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
    for path in world_directory.rglob("*.*"):
      if "__pycache__" in path.parts:
        continue

      relative_path = os.path.join(*path.parts[path.parts.index("worlds") + 1 :])
      # strip the leading "<file_name>/" for .apignore matching against world-relative paths
      world_relative = os.path.relpath(relative_path, file_name)
      if is_ignored(world_relative):
        continue

      if not relative_path.endswith("archipelago.json"):
        # ZipInfo.from_file() derives the timestamp from the file's mtime, which
        # can be pre-1980 (e.g. epoch 0 from some checkout/build tools) and zipfile
        # rejects that. Build the ZipInfo manually with a safe fixed timestamp.
        zinfo = zipfile.ZipInfo(relative_path, date_time=(1980, 1, 1, 0, 0, 0))
        zinfo.compress_type = zipfile.ZIP_DEFLATED
        with open(path, "rb") as fsrc:
          zf.writestr(zinfo, fsrc.read(), compresslevel=9)



    zf.writestr(apworld.manifest_path, json.dumps(manifest))

  print(f"built {zip_path}")
