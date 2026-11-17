#!/usr/bin/env python3
"""Measure how established every entry is, so a reader can filter for themselves.

The list is a directory: it names the options and lets the reader choose. This
script supplies the half a reader cannot see at a glance, and it prints only
numbers that have a public source:

  GitHub        stars, and the repository's own birthday, from the API
  TradingView   boosts, read off the script page
  any domain    first capture in the Wayback Machine, which gives "around since"
  App Store     average rating and count, from Apple's public search API
  Trustpilot    attempted, and recorded as blocked when it refuses (it does)

Nothing here invents a user count. A closed service that publishes none shows a
dash, and a dash is a fact about the evidence rather than about the service.

    python3 scripts/adoption.py                 # refresh what is stale, write ADOPTION.md
    python3 scripts/adoption.py --max-age 0     # re-measure everything
    python3 scripts/adoption.py --limit 5       # smoke test on the first five entries

The cache is scripts/adoption.json and it is written after every phase, so a run
that is cut short keeps what it measured. Wayback results are memoised per HOST,
because thirty entries share tradingview.com and it is the slowest source.
"""

import argparse
import json
import re
import shutil
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.parse import quote, urlparse

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36")
ROOT = Path(__file__).resolve().parent.parent
CACHE = ROOT / "scripts" / "adoption.json"
OUT = ROOT / "ADOPTION.md"
SKIP_SECTIONS = {"contents", "contributing"}
# docs rather than products: tradingview.com's first capture says nothing about a manual
RENDER_SKIP = {"official resources"}


def curl(url, timeout=20):
    try:
        out = subprocess.run(["curl", "-sS", "-L", "--max-time", str(timeout), "-A", UA, url],
                             capture_output=True, text=True, timeout=timeout + 8)
        return out.stdout, out.returncode
    except subprocess.TimeoutExpired:
        return "", 28


def entries(markdown):
    section, rows = None, []
    for line in markdown.splitlines():
        head = re.match(r"^##\s+(.+?)\s*$", line)
        if head:
            section = head.group(1).strip()
            continue
        item = re.match(r"^\s*-\s+\[(.+?)\]\((https?://[^)\s]+)\)\s*-\s*(.+)$", line)
        if item and section and section.lower() not in SKIP_SECTIONS:
            rows.append({"name": item.group(1), "url": item.group(2), "section": section})
    return rows


def github(url):
    m = re.match(r"https?://github\.com/([^/]+/[^/#?]+)", url)
    if not m:
        return None
    repo = m.group(1).removesuffix(".git")
    body = ""
    # The unauthenticated API allows 60 requests an hour per IP and this machine
    # shares one, so carry a token when `gh` is on PATH and fall back to curl.
    if shutil.which("gh"):
        try:
            body = subprocess.run(["gh", "api", f"repos/{repo}"], capture_output=True,
                                  text=True, timeout=30).stdout
        except subprocess.TimeoutExpired:
            body = ""
    if not body.lstrip().startswith("{"):
        body, _ = curl(f"https://api.github.com/repos/{repo}")
    if not body.lstrip().startswith("{"):
        return None
    try:
        d = json.loads(body)
    except json.JSONDecodeError:
        return None
    if "stargazers_count" not in d:
        return None
    return {"stars": d["stargazers_count"], "first": (d.get("created_at") or "")[:4]}


def tradingview(url):
    if "tradingview.com/script/" not in url:
        return None
    body, rc = curl(url)
    m = re.search(r'aria-label="([\d,]+)\s+boost', body) if rc == 0 else None
    return {"boosts": int(m.group(1).replace(",", ""))} if m else None


def appstore(host, name):
    """Average rating and count from Apple's public search API, matched on the BRAND.

    The brand is the domain's own name (3commas from 3commas.io), not the entry's
    title, because a title search matches any app that happens to share a word:
    "Raindrops" and "Charts" both return strangers' apps, and a stranger's rating
    beside an entry is worse than a dash.
    """
    brand = host.split(".")[-2] if host.count(".") >= 1 else host
    brand = re.sub(r"[^a-z0-9]", "", brand.lower())
    entry = re.sub(r"[^a-z0-9]", "", name.replace("†", "").lower())
    # the brand AND the entry's own name have to agree, or tradingview.to picks up
    # the TradingView app, which is a different company
    if len(brand) < 4 or brand != entry:
        return None
    body, rc = curl(f"https://itunes.apple.com/search?term={quote(brand)}&entity=software&limit=8")
    if rc != 0:
        return None
    try:
        results = json.loads(body).get("results", [])
    except json.JSONDecodeError:
        return None
    for r in results:
        got = re.sub(r"[^a-z0-9]", "", (r.get("trackName") or "").lower())
        if got.startswith(brand) and r.get("userRatingCount", 0) >= 20:
            return {"app_score": round(float(r["averageUserRating"]), 1),
                    "app_count": int(r["userRatingCount"])}
    return None


def first_seen_host(host):
    """Earliest Wayback capture for a host, or None. Slow and rate-limited."""
    for attempt in (1, 2):
        body, rc = curl(f"https://web.archive.org/cdx/search/cdx?url={host}&output=json"
                        f"&limit=1&fl=timestamp&filter=statuscode:200", timeout=25)
        if rc == 0:
            try:
                # a CDX timestamp is fourteen digits (YYYYMMDDhhmmss), not eight
                rows = json.loads(body)
                stamp = rows[1][0]
                if stamp[:4].isdigit():
                    return stamp[:4]
            except (json.JSONDecodeError, IndexError, TypeError):
                pass
        time.sleep(1.5 * attempt)
    return None


def trustpilot(host):
    body, rc = curl(f"https://www.trustpilot.com/review/{host}")
    if rc != 0 or "trustScore" not in body:
        return None
    score = (re.search(r'"ratingValue"\s*:\s*"?([\d.]+)', body)
             or re.search(r"trustScore[^0-9]*([\d.]+)", body))
    count = (re.search(r'"reviewCount"\s*:\s*"?(\d+)', body)
             or re.search(r"numberOfReviews[^0-9]*(\d+)", body))
    if not (score and count):
        return None
    return {"score": float(score.group(1)), "count": int(count.group(1))}


def save(cache, cache_path, rows):
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    cache_path.write_text(json.dumps(cache, indent=1, sort_keys=True) + "\n", encoding="utf-8")


def quick(row, max_age, cache):
    key = row["url"]
    old = cache.get(key, {})
    if (time.time() - old.get("checked", 0)) < max_age * 86400:
        return old
    rec = {"name": row["name"], "url": key, "section": row["section"], "checked": int(time.time())}
    gh = github(key)
    if gh:
        rec.update(gh)
    else:
        tv = tradingview(key)
        if tv:
            rec.update(tv)
        # only a service with its own domain can have its own app; a TradingView
        # script does not, and searching its title finds a stranger's app
        if "tradingview.com" not in key and "github.com" not in key:
            store = appstore(urlparse(key).netloc.lower().removeprefix("www."), row["name"])
            if store:
                rec.update(store)
    # an App Store match is NOT carried over: the matcher was once looser, and a
    # stale wrong rating is worse than a dash
    for field in ("stars", "boosts", "first"):
        if field in old and field not in rec:
            rec[field] = old[field]
    return rec


def fmt(n):
    return f"{n / 1000:.1f}k".replace(".0k", "k") if n >= 1000 else str(n)


def render(rows, cache):
    out = ["# Adoption and evidence", "",
           "The list is a directory: it says what each resource is, and this page says how established",
           "it is. Every number carries the date it was measured, and a dash means no public number",
           "exists, which is a fact about the evidence rather than about the resource.", "",
           "Sources: stars and a repository's birthday from the GitHub API, boosts from each TradingView",
           "script page, the domain's first capture from the Wayback Machine's CDX index, and ratings",
           "from Apple's public search API. `domain since` is when the DOMAIN first appeared, which is",
           "not always when the service did: a domain that changed hands carries the older date.", ""]
    heads = ["resource", "evidence", "domain since", "reviewers"]

    # Build one section at a time, then drop any column that is empty for that
    # section: a table full of dashes reads as missing data rather than as honesty.
    section, block = None, []
    def flush():
        if not block or section is None:
            return []
        keep = [0] + [i for i in range(1, 4) if any(r[i] != "—" for r in block)]
        lines = ["", f"## {section}", "",
                 "| " + " | ".join(heads[i] for i in keep) + " |",
                 "| " + " | ".join("---" for _ in keep) + " |"]
        for r in block:
            lines.append("| " + " | ".join(r[i] for i in keep) + " |")
        return lines

    for row in rows:
        if row["section"].lower() in RENDER_SKIP:
            continue
        c = cache.get(row["url"], {})
        if row["section"] != section:
            out += flush()
            section, block = row["section"], []
        bits = []
        if c.get("stars") is not None:
            bits.append(f"★ {fmt(c['stars'])} on GitHub")
        if c.get("boosts") is not None:
            bits.append(f"{fmt(c['boosts'])} boosts")
        since = c.get("first")
        if "tradingview.com" in row["url"]:
            since = None      # the host's first capture says nothing about a script published later
        tp, rv = c.get("trustpilot"), "—"
        if tp:
            rv = f"Trustpilot {tp['score']} ({fmt(tp['count'])}, {time.strftime('%b %Y', time.gmtime(tp.get('checked', 0)))})"
        elif c.get("app_score") is not None:
            rv = f"App Store {c['app_score']} ({fmt(c['app_count'])})"
        block.append([f"[{row['name']}]({row['url']})", ", ".join(bits) or "—", since or "—", rv])
    out += flush()
    out += ["", "---", "",
            f"Measured {time.strftime('%d %B %Y', time.gmtime())} by `scripts/adoption.py`. A lookup that",
            "is refused keeps its previous reading rather than dropping out, and Trustpilot refuses",
            "scripted requests from this host, so its column fills only when a browser has read it.", ""]
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--max-age", type=int, default=7)
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--out", default=str(OUT))
    ap.add_argument("--cache", default=str(CACHE))
    ap.add_argument("--skip-web", action="store_true")
    args = ap.parse_args()

    rows = entries((ROOT / "README.md").read_text(encoding="utf-8"))
    if args.limit:
        rows = rows[:args.limit]
    cache_path = Path(args.cache)
    cache = json.loads(cache_path.read_text(encoding="utf-8")) if cache_path.exists() else {}
    stale = [r for r in rows if (time.time() - cache.get(r["url"], {}).get("checked", 0)) >= args.max_age * 86400]

    print(f"{len(rows)} entries, {len(stale)} stale", flush=True)
    with ThreadPoolExecutor(max_workers=8) as pool:
        for row, rec in zip(rows, pool.map(lambda r: quick(r, args.max_age, cache), rows)):
            # replace, never merge: a field that is absent this run (a rating the
            # matcher no longer trusts) must disappear rather than linger
            cache[row["url"]] = rec
    save(cache, cache_path, rows)
    print(f"pass 1 done: {sum(1 for r in rows if cache[r['url']].get('stars') is not None)} stars, "
          f"{sum(1 for r in rows if cache[r['url']].get('boosts') is not None)} boosts", flush=True)

    if not args.skip_web:
        hosts = []
        for r in stale:
            h = urlparse(r["url"]).netloc.lower().removeprefix("www.")
            if f"host:{h}" not in cache and h not in hosts and not cache[r["url"]].get("first"):
                hosts.append(h)
        print(f"wayback: {len(hosts)} hosts", flush=True)
        for i, h in enumerate(hosts, 1):
            year = first_seen_host(h)
            cache[f"host:{h}"] = {"first": year, "checked": int(time.time())}
            if i % 10 == 0:
                save(cache, cache_path, rows)
                print(f"  {i}/{len(hosts)} ({sum(1 for x in hosts[:i] if cache[f'host:{x}'].get('first'))} answered)",
                      flush=True)
            # archive.org throttles hard: a faster loop comes back empty, which
            # reads exactly like a host with no captures
            time.sleep(1.2)
        for r in rows:
            h = urlparse(r["url"]).netloc.lower().removeprefix("www.")
            if cache[r["url"]].get("first") is None and cache.get(f"host:{h}", {}).get("first"):
                cache[r["url"]]["first"] = cache[f"host:{h}"]["first"]
        save(cache, cache_path, rows)
        print("trustpilot: recorded as blocked when it refuses", flush=True)
        for r in stale:
            h = urlparse(r["url"]).netloc.lower().removeprefix("www.")
            if cache.get(f"host:{h}", {}).get("tp_blocked"):
                continue
            got = trustpilot(h)
            if got:
                cache[r["url"]]["trustpilot"] = {**got, "checked": int(time.time())}
            else:
                cache[f"host:{h}"] = {**cache.get(f"host:{h}", {}), "tp_blocked": int(time.time())}
            time.sleep(0.2)
        save(cache, cache_path, rows)

    Path(args.out).write_text(render(rows, cache), encoding="utf-8")
    print(f"evidence: {sum(1 for r in rows if cache[r['url']].get('stars') is not None)} stars, "
          f"{sum(1 for r in rows if cache[r['url']].get('boosts') is not None)} boosts, "
          f"{sum(1 for r in rows if cache[r['url']].get('first'))} since, "
          f"{sum(1 for r in rows if cache[r['url']].get('app_score') is not None)} app store, "
          f"{sum(1 for r in rows if cache[r['url']].get('trustpilot'))} trustpilot -> {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
