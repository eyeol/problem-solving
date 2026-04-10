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
    res = requests.get(url, timeout=10)
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


def generate_svg(boj_tier, boj_progress, lc_count, lc_progress):
    W = 360
    H = 156
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
    font-family="'SF Mono','Fira Code',monospace">BOJ Platinum · LC Top Interview 150</text>

  <line x1="{pad}" y1="30" x2="{W - pad}" y2="30" stroke="#e1e4e8" stroke-width="0.5"/>

  <text x="{pad}" y="46" font-size="9" font-weight="500" letter-spacing="1.5"
    fill="#8b949e" font-family="'SF Mono','Fira Code',monospace">PROGRESS</text>

  {row(60, "BOJ", boj_tier, "#0F6E56", "#E1F5EE", "→ Platinum", boj_progress, "#1D9E75")}
  {row(60 + row_h, "LC Top150", f"{lc_count} / {LEETCODE_GOAL}", "#854F0B", "#FAEEDA", f"{round(lc_progress*100)}%", lc_progress, "#EF9F27")}

</svg>"""


def unicode_bar(progress, width=10):
    filled = round(progress * width)
    return "█" * filled + "░" * (width - filled)


def render_category_table(track):
    lines = ["### LeetCode Top Interview 150", ""]
    lines.append("| Category | Progress | Count | Done |")
    lines.append("| --- | --- | --- | --- |")
    for name, cat in track.items():
        solved, total = cat["solved"], cat["total"]
        pct = solved / total if total else 0.0
        done = cat.get("completed_at") or ("✅" if solved >= total and total > 0 else "")
        lines.append(f"| {name} | `{unicode_bar(pct)}` {round(pct*100)}% | {solved} / {total} | {done} |")
    solved_sum, total_sum, pct_sum = track_totals(track)
    lines.append(f"| **Total** | `{unicode_bar(pct_sum)}` **{round(pct_sum*100)}%** | **{solved_sum} / {total_sum}** | |")
    lines.append("")
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
    save_progress(progress)

    print("Fetching BOJ stats...")
    boj_tier, boj_solved, boj_progress = fetch_boj()
    print(f"  tier={boj_tier}, solved={boj_solved}, progress={boj_progress:.2f}")

    lc_count, lc_total, lc_progress = track_totals(progress["lc_top150"])
    print(f"  LC Top150: {lc_count} / {lc_total} ({lc_progress*100:.0f}%)")

    svg = generate_svg(boj_tier, boj_progress, lc_count, lc_progress)
    os.makedirs(os.path.dirname(SVG_PATH), exist_ok=True)
    with open(SVG_PATH, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"SVG written to {SVG_PATH}")

    update_readme(progress)
    print("README categories section updated")


if __name__ == "__main__":
    main()
