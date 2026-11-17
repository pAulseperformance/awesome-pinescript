#!/usr/bin/env python3
"""Check every link in a markdown file. Standard library only.

Exit 0 when nothing is dead, 1 when something is, 2 when the file is missing.

Only 404/410 and a total transport failure count as dead. A 401/403/405/429 is
a bot wall: reported as gated, and it does not fail the run. Probe with GET and
a browser user agent, because a HEAD request answers 404 on paths that serve 200
and that artifact is what produces bulk false findings.

A host that refuses curl entirely (code 000) can be excused with --allow, but
only for the transport failure. A 404 on an allowed host still fails, so the
allowlist cannot hide a missing page.
"""

import argparse
import re
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.parse import urlparse

UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
)
GATED = {"401", "403", "405", "429"}
DEAD = {"404", "410"}


def links(text):
    """Map each unique URL to the last heading above it."""
    seen = {}
    section = ""
    for line in text.splitlines():
        heading = re.match(r"^#{2,4}\s+(.*)", line)
        if heading:
            section = heading.group(1).strip()
        for m in re.finditer(r"\[[^\]]+\]\((https?://[^)\s]+)\)", line):
            seen.setdefault(m.group(1), section)
    return seen


def host_of(url):
    return urlparse(url).netloc.lower().removeprefix("www.")


def load_allow(path):
    if not path or not Path(path).exists():
        return set()
    hosts = set()
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        line = line.split("#", 1)[0].strip()
        if line:
            hosts.add(line.lower().removeprefix("www."))
    return hosts


def probe(url):
    for attempt in (1, 2):
        try:
            out = subprocess.run(
                ["curl", "-sS", "-L", "--max-time", "30", "-A", UA,
                 "-o", "/dev/null", "-w", "%{http_code}", url],
                capture_output=True, text=True, timeout=45,
            )
            code = out.stdout.strip() or "000"
            # A 5xx on a big host is usually a bad moment, not a missing page.
            if code.startswith("5") and attempt == 1:
                time.sleep(3)
                continue
            return url, code, out.stderr.strip(), out.returncode
        except subprocess.TimeoutExpired:
            if attempt == 1:
                continue
            return url, "000", "timeout", 28
    return url, "000", "no response", 7


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("path", nargs="?", default="README.md")
    ap.add_argument("--workers", type=int, default=10)
    ap.add_argument("--allow", default="scripts/link_allowlist.txt",
                    help="hosts whose curl transport failure is known-good")
    args = ap.parse_args()

    path = Path(args.path)
    if not path.exists():
        print(f"no file at {path}", file=sys.stderr)
        return 2

    allowed_hosts = load_allow(args.allow)
    found = links(path.read_text(encoding="utf-8"))
    print(f"checking {len(found)} unique links in {path.name}")
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        results = list(pool.map(probe, found))

    ok = gated = dead = excused = flaky = 0
    for url, code, err, rc in results:
        if code.startswith(("2", "3")):
            ok += 1
        elif code in GATED:
            gated += 1
            print(f"  gated  {code}  {url}")
        elif code.startswith("5"):
            # Retried once already. A host having a bad minute is not a dead link,
            # but it should be visible rather than silently counted as fine.
            flaky += 1
            print(f"  flaky  {code}  {url}")
        elif rc == 60:
            # The server sends an incomplete certificate chain. Browsers fetch the
            # missing intermediate and open the page, so this is not a dead link,
            # but it is worth seeing on every run until the host fixes its chain.
            gated += 1
            print(f"  gated  TLS  {url}  (incomplete certificate chain)")
        elif code == "000" and host_of(url) in allowed_hosts:
            excused += 1
            print(f"  allowed 000  {url}  (verified by a second method)")
        else:
            dead += 1
            reason = code if code != "000" else (err.splitlines()[0] if err else "no response")
            print(f"  DEAD   {code}  {url}  {reason}")

    print(f"\n{ok} ok, {gated} gated, {flaky} flaky, {excused} allowed, {dead} dead")
    if dead:
        print("every DEAD line needs a second method before it is reported: "
              "openssl s_client, a real browser load, or the registry API")
    return 1 if dead else 0


if __name__ == "__main__":
    sys.exit(main())
