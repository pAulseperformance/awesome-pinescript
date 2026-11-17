#!/usr/bin/env python3
"""Turn a link-check reading into a badge shields.io can serve.

The reading is the machine record; this is the one line a visitor sees without
opening the Actions tab. The date is in the message on purpose: a green badge
that cannot say when it was measured is decoration, not evidence.

    python3 scripts/publish_health.py health.json assets/verified.json
"""

import json
import sys
from datetime import datetime
from pathlib import Path


def main():
    src = Path(sys.argv[1] if len(sys.argv) > 1 else "health.json")
    dst = Path(sys.argv[2] if len(sys.argv) > 2 else "assets/verified.json")

    reading = json.loads(src.read_text(encoding="utf-8"))
    dead = int(reading["dead"])
    when = datetime.strptime(reading["checked_at"][:10], "%Y-%m-%d").strftime("%d %b")
    # No middle dot in a shields message: its escaping turns one into a blank.
    message = f"{dead} dead, {when}" if dead else f"all clear, {when}"

    badge = {
        "schemaVersion": 1,
        "label": "links verified",
        "message": message,
        "color": "red" if dead else "brightgreen",
    }
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(json.dumps(badge) + "\n", encoding="utf-8")
    print(f"{dst} -> {message}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
