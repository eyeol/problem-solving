import json
import os
import re

import requests

BOJ_ID = "kamu_kamui"

BOJ_TIER_NAMES = {
    0: "Unrated",
    1: "Bronze V", 2: "Bronze IV", 3: "Bronze III", 4: "Bronze II", 5: "Bronze I",
    6: "Silver V", 7: "Silver IV", 8: "Silver III", 9: "Silver II", 10: "Silver I",
    11: "Gold V", 12: "Gold IV", 13: "Gold III", 14: "Gold II", 15: "Gold I",
    16: "Platinum V", 17: "Platinum IV", 18: "Platinum III", 19: "Platinum II", 20: "Platinum I",
    21: "Diamond V", 22: "Diamond IV",
}
BOJ_TIER_BY_NAME = {name: tier for tier, name in BOJ_TIER_NAMES.items()}
PLATINUM_END = 20

LEETCODE_GOAL = 150  # Top Interview 150

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
PROGRESS_JSON = os.path.join(ROOT, "data", "progress.json")
TOP150_MAP = os.path.join(ROOT, "data", "top150_map.json")
README_PATH = os.path.join(ROOT, "README.md")
SVG_PATH = os.path.join(ROOT, "assets", "progress.svg")
LC_DIRS = [
    os.path.join(ROOT, "leetcode"),
    os.path.join(ROOT, "LeetCode"),
]


def fetch_boj():
    url = f"https://solved.ac/api/v3/user/show?handle={BOJ_ID}"
    headers = {
        "User-Agent": "problem-solving-progress/1.0",
        "Accept": "application/json",
    }
    res = requests.get(url, timeout=10, headers=headers)
    res.raise_for_status()
    data = res.json()
    tier = data["tier"]
    solved = data["solvedCount"]
    tier_name = BOJ_TIER_NAMES.get(tier, f"Tier {tier}")
    progress = min(tier / PLATINUM_END, 1.0)
    return tier_name, solved, progress


def load_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def save_progress(progress):
    with open(PROGRESS_JSON, "w", encoding="utf-8") as f:
        json.dump(progress, f, ensure_ascii=False, indent=2)
        f.write("\n")


def cache_boj_stats(progress, tier_name, solved, progress_value):
    progress["boj"] = {
        "handle": BOJ_ID,
        "tier_name": tier_name,
        "solved": solved,
        "progress": round(progress_value, 4),
    }


def load_cached_boj_stats(progress):
    cached = progress.get("boj")
    if isinstance(cached, dict):
        tier_name = cached.get("tier_name")
        solved = cached.get("solved")
        progress_value = cached.get("progress")
        if isinstance(tier_name, str) and isinstance(progress_value, (int, float)):
            solved_value = solved if isinstance(solved, int) else 0
            return tier_name, solved_value, float(progress_value)

    if not os.path.exists(SVG_PATH):
        return None

    with open(SVG_PATH, encoding="utf-8") as f:
        svg = f.read()

    match = re.search(
        r">BOJ</text>.*?text-anchor=\"middle\">([^<]+)</text>",
        svg,
        re.DOTALL,
    )
    if not match:
        return None

    tier_name = match.group(1).strip()
    tier = BOJ_TIER_BY_NAME.get(tier_name)
    if tier is None:
        return None

    progress_value = min(tier / PLATINUM_END, 1.0)
    return tier_name, 0, progress_value


def resolve_boj_stats(progress):
    try:
        boj_stats = fetch_boj()
    except (requests.RequestException, KeyError, ValueError) as exc:
        cached = load_cached_boj_stats(progress)
        if cached is None:
            print(f"  BOJ fetch failed: {exc}")
            print("  No cached BOJ stats found; keeping the existing SVG")
            return None
        print(f"  BOJ fetch failed: {exc}")
        print("  Falling back to cached BOJ stats")
        cache_boj_stats(progress, *cached)
        return cached

    cache_boj_stats(progress, *boj_stats)
    return boj_stats


def scan_leetcode_folder():
    """Return the set of problem slugs under LeetCode folders."""
    slugs = set()
    pattern = re.compile(r"^\d+-(.+)$")

    for lc_dir in LC_DIRS:
        if not os.path.isdir(lc_dir):
            continue
        for _, dirnames, _ in os.walk(lc_dir):
            for name in dirnames:
                m = pattern.match(name)
                if m:
                    slugs.add(m.group(1))

    return slugs


def sync_lc_progress(progress, slug_map):
    """Recompute lc_top150 solved counts from leetcode/ folder contents."""
    solved_slugs = scan_leetcode_folder()
    for cat in progress["lc_top150"].values():
        cat["solved"] = 0
    matched = 0
    for slug in solved_slugs:
        category = slug_map.get(slug)
        if category and category in progress["lc_top150"]:
            progress["lc_top150"][category]["solved"] += 1
            matched += 1
    return matched, len(solved_slugs)


def track_totals(track):
    solved = sum(cat["solved"] for cat in track.values())
    total = sum(cat["total"] for cat in track.values())
    progress = min(solved / total, 1.0) if total else 0.0
    return solved, total, progress


def generate_svg(boj_tier, boj_progress, lc_count, lc_progress, ct_stage, ct_total, ct_progress):
    W = 470
    H = 217
    pad = 24
    bar_w = W - pad * 2
    row_h = 54

    def row(y, label, badge_text, badge_color, badge_bg, right_text, progress, bar_color):
        fill_w = round(progress * bar_w)
        return f"""
  <text x="{pad}" y="{y}" font-family="'SF Mono','Fira Code',monospace"
    font-size="12" font-weight="500" fill="#24292f">{label}</text>
  <g transform="translate({pad}, {y + 6})">
    <rect width="80" height="19" rx="4" fill="{badge_bg}"/>
    <text x="40" y="13.5" font-family="'SF Mono','Fira Code',monospace"
      font-size="10.5" font-weight="500" fill="{badge_color}" text-anchor="middle">{badge_text}</text>
  </g>
  <text x="{W - pad}" y="{y + 17}" font-family="'SF Mono','Fira Code',monospace"
    font-size="10" fill="#8b949e" text-anchor="end">{right_text}</text>
  <rect x="{pad}" y="{y + 30}" width="{bar_w}" height="4" rx="2" fill="#eaeef2"/>
  <rect x="{pad}" y="{y + 30}" width="{fill_w}" height="4" rx="2" fill="{bar_color}"/>
"""

    return f"""<svg width="{W}" height="{H}" viewBox="0 0 {W} {H}"
  xmlns="http://www.w3.org/2000/svg">

  <style>
    svg {{ font-family: 'SF Mono', 'Fira Code', 'Consolas', monospace; }}
  </style>

  <rect width="{W}" height="{H}" rx="8" fill="#ffffff" stroke="#e1e4e8" stroke-width="1"/>

  <text x="{pad}" y="22" font-size="9" font-weight="500" letter-spacing="1.5"
    fill="#8b949e" font-family="'SF Mono','Fira Code',monospace">GOALS</text>
  <text x="{pad + 48}" y="22" font-size="9" fill="#8b949e"
    font-family="'SF Mono','Fira Code',monospace">BOJ Platinum · LC Top Interview 150 · Codetree Trails</text>

  <line x1="{pad}" y1="30" x2="{W - pad}" y2="30" stroke="#e1e4e8" stroke-width="0.5"/>

  <text x="{pad}" y="46" font-size="9" font-weight="500" letter-spacing="1.5"
    fill="#8b949e" font-family="'SF Mono','Fira Code',monospace">PROGRESS</text>

  {row(64, "BOJ", boj_tier, "#0F6E56", "#E1F5EE", "→ Platinum", boj_progress, "#1D9E75")}
  {row(64 + row_h, "LC Top150", f"{lc_count} / {LEETCODE_GOAL}", "#854F0B", "#FAEEDA", f"{round(lc_progress*100)}%", lc_progress, "#EF9F27")}
  {row(64 + row_h * 2, "Codetrails", f"{ct_stage} / {ct_total}", "#3A4CB4", "#E6E9FA", f"{int(ct_progress*100)}%", ct_progress, "#5468DB")}

</svg>"""


def unicode_bar(progress, width=10):
    filled = round(progress * width)
    return "█" * filled + "░" * (width - filled)


LC_LAYOUT = [
    ("Array & Hashing", ["Array / String", "Two Pointers", "Sliding Window", "Matrix", "Hashmap", "Intervals"]),
    ("Linear DS", ["Stack", "Linked List", "Heap"]),
    ("Search & Bits", ["Binary Search", "Bit Manipulation", "Math"]),
    ("Tree", ["Binary Tree General", "Binary Tree BFS", "Binary Search Tree", "Trie"]),
    ("Graph & Backtracking", ["Graph General", "Graph BFS", "Backtracking"]),
    ("DP & D&C", ["Divide & Conquer", "Kadane's Algorithm", "1D DP", "Multidimensional DP"]),
]


CAT_W = 180
PROG_W = 150
COUNT_W = 20


def _render_group(title, names, track):
    lines = [
        f"#### {title}",
        "",
        "<table>",
        "  <tr>"
        f"<th align=\"left\" width=\"{CAT_W}\">Category</th>"
        f"<th align=\"left\" width=\"{PROG_W}\">Progress</th>"
        f"<th align=\"left\" width=\"{COUNT_W}\">Count</th>"
        "</tr>",
    ]
    for name in names:
        cat = track[name]
        solved, total = cat["solved"], cat["total"]
        pct = solved / total if total else 0.0
        lines.append(
            f"  <tr>"
            f"<td width=\"{CAT_W}\">{name}</td>"
            f"<td width=\"{PROG_W}\"><code>{unicode_bar(pct)}</code> {round(pct*100)}%</td>"
            f"<td width=\"{COUNT_W}\">{solved} / {total}</td>"
            f"</tr>"
        )
    lines.append("</table>")
    lines.append("")
    return lines


def render_total_banner(solved, total, pct):
    width = 30
    filled = round(pct * width)
    bar = "▰" * filled + "▱" * (width - filled)
    return [
        "<table width=\"100%\">",
        "  <tr><td align=\"center\">",
        "    <sub>OVERALL PROGRESS</sub><br/>",
        f"    <h2>{solved} <sub>/ {total}</sub> &nbsp;·&nbsp; {round(pct*100)}%</h2>",
        f"    <code>{bar}</code>",
        "  </td></tr>",
        "</table>",
        "",
    ]


def render_category_table(track):
    layout_names = {n for _, names in LC_LAYOUT for n in names}
    missing = set(track.keys()) - layout_names
    extra = layout_names - set(track.keys())
    if missing or extra:
        raise RuntimeError(f"LC_LAYOUT mismatch with progress.json (missing={missing}, extra={extra})")

    lines = ["### LeetCode Top Interview 150", ""]
    solved_sum, total_sum, pct_sum = track_totals(track)
    lines.extend(render_total_banner(solved_sum, total_sum, pct_sum))
    for title, names in LC_LAYOUT:
        lines.extend(_render_group(title, names, track))
    return "\n".join(lines)


def update_readme(progress):
    body = render_category_table(progress["lc_top150"])
    block = f"<!-- CATEGORIES:START -->\n\n{body}\n<!-- CATEGORIES:END -->"

    with open(README_PATH, encoding="utf-8") as f:
        content = f.read()

    pattern = re.compile(
        r"<!-- CATEGORIES:START -->.*?<!-- CATEGORIES:END -->",
        re.DOTALL,
    )
    if not pattern.search(content):
        raise RuntimeError("README.md is missing <!-- CATEGORIES:START --> / <!-- CATEGORIES:END --> markers")
    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(pattern.sub(block, content))


def main():
    print("Loading progress.json + top150_map.json...")
    progress = load_json(PROGRESS_JSON)
    slug_map = load_json(TOP150_MAP)["slug_to_category"]

    matched, found = sync_lc_progress(progress, slug_map)
    print(f"  leetcode/ scan: {found} slugs found, {matched} matched Top 150")

    print("Fetching BOJ stats...")
    boj_stats = resolve_boj_stats(progress)
    if boj_stats is None:
        boj_tier = boj_solved = boj_progress = None
    else:
        boj_tier, boj_solved, boj_progress = boj_stats
        print(f"  tier={boj_tier}, solved={boj_solved}, progress={boj_progress:.2f}")

    lc_count, lc_total, lc_progress = track_totals(progress["lc_top150"])
    print(f"  LC Top150: {lc_count} / {lc_total} ({lc_progress*100:.0f}%)")

    ct_stage = progress["codetree"]["stage"]
    ct_total = progress["codetree"]["total"]
    ct_progress = min(ct_stage / ct_total, 1.0) if ct_total else 0.0
    print(f"  Codetree: {ct_stage} / {ct_total} ({int(ct_progress*100)}%)")

    save_progress(progress)

    if boj_stats is None and os.path.exists(SVG_PATH):
        print("SVG update skipped because BOJ stats are unavailable")
    else:
        if boj_stats is None:
            boj_tier, boj_progress = "Unrated", 0.0
            print("Writing a placeholder SVG because no previous BOJ SVG exists")
        svg = generate_svg(boj_tier, boj_progress, lc_count, lc_progress, ct_stage, ct_total, ct_progress)
        os.makedirs(os.path.dirname(SVG_PATH), exist_ok=True)
        with open(SVG_PATH, "w", encoding="utf-8") as f:
            f.write(svg)
        print(f"SVG written to {SVG_PATH}")

    update_readme(progress)
    print("README categories section updated")


if __name__ == "__main__":
    main()
