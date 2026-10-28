#!/usr/bin/env python3
"""Collect PA2 SWE-99 Spec Kit Markdown snapshots from pinned public GitHub commits.

Usage from docs-SWE repo root:
    python3 PA2/SpecKit/collect_speckit.py
    python3 PA2/SpecKit/collect_speckit.py --verify-only

Requires Git, Python 3.9+, and internet access for initial collection.
"""
import argparse
import csv
import hashlib
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
TSV = HERE / "Source_Files.tsv"


def git_blob_sha(payload: bytes) -> str:
    # Git object ID (SHA1) of the exact bytes, independent of local line endings.
    return hashlib.sha1(b"blob " + str(len(payload)).encode("ascii") + b"\0" + payload).hexdigest()


def run_git(*args: str, cwd: Path):
    return subprocess.run(["git", *args], cwd=cwd, check=True, text=True,
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def load_manifest():
    with TSV.open(encoding="utf-8", newline="") as fp:
        entries = list(csv.DictReader(fp, delimiter="\t"))
    assert len(entries) == 48, f"Expected 48 files; got {len(entries)}"
    for row in entries:
        if not row["source_commit"] or not row["blob_sha"]:
            raise ValueError("Source SHA missing from inventory")
    return entries


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify-only", action="store_true",
                        help="Do not fetch; verify all already collected local snapshots")
    parser.add_argument("--force", action="store_true",
                        help="Overwrite an existing snapshot only if its hash differs")
    args = parser.parse_args()

    manifest = load_manifest()
    by_repo = {}
    for r in manifest:
        by_repo.setdefault(r["repo"], []).append(r)

    count = 0
    if args.verify_only:
        for r in manifest:
            dst = HERE / r["snapshot_path"]
            if not dst.is_file():
                raise FileNotFoundError(f"Missing snapshot: {dst}")
            actual = git_blob_sha(dst.read_bytes())
            if actual != r["blob_sha"]:
                raise ValueError(f"SHA mismatch: {dst}: {actual} != {r['blob_sha']}")
            count += 1
        print(f"PASS: {count}/48 Markdown snapshots are present and hash verified.")
        return

    if shutil.which("git") is None:
        raise RuntimeError("Git not installed or not in PATH")

    with tempfile.TemporaryDirectory(prefix="speckit-swe99-") as temp:
        for short, group in by_repo.items():
            r0 = group[0]
            name, commit = r0["repository"], r0["source_commit"]
            work = Path(temp) / short
            work.mkdir()
            print(f"Fetching {name} @ {commit[:12]} ...", flush=True)
            run_git("init", "-q", cwd=work)
            run_git("remote", "add", "origin", f"https://github.com/Adiff-git/{name}.git", cwd=work)
            run_git("fetch", "--quiet", "--depth", "1", "origin", commit, cwd=work)
            run_git("checkout", "--quiet", "--detach", "FETCH_HEAD", cwd=work)
            got = run_git("rev-parse", "HEAD", cwd=work).stdout.strip()
            if got != commit:
                raise ValueError(f"Fetched unexpected revision for {name}: {got}")

            for r in group:
                src = work / r["path"]
                dst = HERE / r["snapshot_path"]
                if not src.is_file():
                    raise FileNotFoundError(f"Source file missing: {name}:{r['path']}")
                content = src.read_bytes()
                actual = git_blob_sha(content)
                if actual != r["blob_sha"]:
                    raise ValueError(f"Source modified: {name}:{r['path']}, blob={actual}")
                if dst.is_file() and dst.read_bytes() != content and not args.force:
                    raise FileExistsError(f"Different local file: {dst}. Re-run with --force to replace")
                dst.parent.mkdir(parents=True, exist_ok=True)
                dst.write_bytes(content)
                count += 1
            print(f"  OK: {len(group)} Markdown files", flush=True)

    if count != 48:
        raise AssertionError(f"Incomplete collection: {count} / 48")
    print("PASS: All 48 real Markdown files collected and verified by pinned Git blob SHA.")
    print("Next: git add PA2/SpecKit && git commit -m 'docs: collect Spec Kit markdown artifacts (SWE-99)'")


if __name__ == "__main__":
    try:
        main()
    except (FileNotFoundError, RuntimeError, ValueError, subprocess.CalledProcessError) as err:
        print(f"ERROR: {err}", file=sys.stderr)
        sys.exit(1)
