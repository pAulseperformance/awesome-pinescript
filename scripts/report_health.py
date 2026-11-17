#!/usr/bin/env python3
"""Report a link-check reading as ONE issue, updated rather than repeated.

A weekly job that opens a new issue every time it fails is noise, and noise gets
ignored faster than silence. So this keeps a single issue whose title carries the
count: it is created when the first link dies, rewritten on every later failure,
reopened if it was closed, and closed by itself when the list is clean again.

    python3 scripts/report_health.py health.json --run-url https://github.com/...
    python3 scripts/report_health.py health.json --dry-run

Needs `gh` on PATH and GH_TOKEN in the environment (the workflow's own token).
"""

import argparse
import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path

MARKER = "[link check]"


def gh(*args, check=True):
    return subprocess.run(["gh", *args], capture_output=True, text=True, check=check)


def existing_issue():
    out = gh("issue", "list", "--state", "all", "--limit", "100",
             "--json", "number,title,state", check=False)
    if out.returncode != 0:
        print(out.stderr.strip(), file=sys.stderr)
        return None
    issues = json.loads(out.stdout or "[]")
    mine = [i for i in issues if i["title"].startswith(MARKER)]
    mine.sort(key=lambda i: i["number"], reverse=True)
    return mine[0] if mine else None


def body_for(reading, run_url):
    dead = [r for r in reading["links"] if r["status"] == "dead"]
    when = datetime.strptime(reading["checked_at"][:10], "%Y-%m-%d").strftime("%d %B %Y")
    lines = [
        f"The scheduled check found **{len(dead)} dead** "
        f"link{'s' if len(dead) != 1 else ''} on {when}.",
        "",
        "| section | link | answer |",
        "| --- | --- | --- |",
    ]
    for r in dead:
        lines.append(f"| {r['section'] or '(no section)'} | {r['url']} | {r['reason']} |")
    lines += [
        "",
        f"Checked {reading['total']} links: {reading['ok']} answered, "
        f"{reading['gated']} behind a bot wall, {reading['allowed']} allowlisted. "
        "Only 404 and 410 count as dead here, so a 403 or a bad minute never "
        "reaches this list.",
        "",
        "Fix: replace the entry, or drop it if the resource is gone. "
        "The next successful run closes this issue on its own.",
    ]
    if run_url:
        lines += ["", f"Run: {run_url}"]
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("reading", nargs="?", default="health.json")
    ap.add_argument("--run-url", default="")
    ap.add_argument("--dry-run", action="store_true",
                    help="print what would be posted, change nothing")
    args = ap.parse_args()

    reading = json.loads(Path(args.reading).read_text(encoding="utf-8"))
    dead = reading["dead"]
    when = datetime.strptime(reading["checked_at"][:10], "%Y-%m-%d").strftime("%d %B %Y")
    found = existing_issue()

    if dead:
        title = f"{MARKER} {dead} dead link{'s' if dead != 1 else ''}"
        body = body_for(reading, args.run_url)
        if args.dry_run:
            print(f"would open or rewrite: {title}\n\n{body}")
            return 0
        if found:
            Path("/tmp/link-check-body.md").write_text(body, encoding="utf-8")
            gh("issue", "edit", str(found["number"]), "--title", title,
               "--body-file", "/tmp/link-check-body.md")
            if found["state"] == "CLOSED":
                gh("issue", "reopen", str(found["number"]))
            print(f"updated issue #{found['number']}: {title}")
        else:
            Path("/tmp/link-check-body.md").write_text(body, encoding="utf-8")
            out = gh("issue", "create", "--title", title,
                     "--body-file", "/tmp/link-check-body.md")
            print("opened " + out.stdout.strip())
        return 0

    message = (f"Every one of the {reading['total']} links resolved on {when}. "
               f"{reading['gated']} sit behind a bot wall and {reading['allowed']} "
               "are allowlisted, neither of which is a dead link.")
    if args.dry_run:
        print(f"would close: {message}")
        return 0
    if found and found["state"] == "OPEN":
        gh("issue", "close", str(found["number"]), "--comment", message,
           "--reason", "completed")
        print(f"closed issue #{found['number']}")
    else:
        print("nothing dead, no issue to close")
    return 0


if __name__ == "__main__":
    sys.exit(main())
