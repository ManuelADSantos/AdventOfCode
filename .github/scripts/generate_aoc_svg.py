from pathlib import Path

# --------------------------
# Config
# --------------------------
# For years with fewer than 25 days (the default is 25)
days_per_year = {2025: 12}

SIZE = 28
PADDING = 8

COLOR_EMPTY = "#eeeeee"
COLOR_PART1 = "#2ecc71"
COLOR_BOTH = "#f1c40f"  # gold

repo_root = Path(__file__).resolve().parents[2]
graphics_dir = repo_root / ".github/graphics"
graphics_dir.mkdir(parents=True, exist_ok=True)
print(f"Repository root: {repo_root}")

# --------------------------
# SVG generator
# --------------------------
def generate_year_svg(year_dir: Path):
    year = year_dir.name

    def day_status(day: int) -> str:
        day_dir = year_dir / f"Day{day:02d}"
        if not day_dir.is_dir():
            return "empty"
        if (day_dir / "part2.py").exists():
            return "both"
        if (day_dir / "part1.py").exists():
            return "part1"
        return "empty"

    total_days = days_per_year.get(int(year), 25)

    # Layout
    COLS = days_per_year.get(int(year), 25)
    rows = (total_days + COLS - 1) // COLS
    width = COLS * (SIZE + PADDING) + PADDING
    height = rows * (SIZE + PADDING) + PADDING

    rects = []
    for day in range(1, total_days + 1):
        row = (day - 1) // COLS
        col = (day - 1) % COLS

        x = PADDING + col * (SIZE + PADDING)
        y = PADDING + row * (SIZE + PADDING)

        status = day_status(day)

        if status == "both":
            color = COLOR_BOTH
            title = f"Day {day}: ⭐⭐"
        elif status == "part1":
            color = COLOR_PART1
            title = f"Day {day}: ⭐"
        else:
            color = COLOR_EMPTY
            title = f"Day {day}: not solved"

        rects.append(
            f'''
            <a href="./{year}/Day{day:02d}">
              <rect x="{x}" y="{y}"
                    width="{SIZE}" height="{SIZE}"
                    rx="6" ry="6"
                    fill="{color}">
                <title>{title}</title>
              </rect>
            </a>
            '''
        )

    svg = f"""<svg
        xmlns="http://www.w3.org/2000/svg"
        width="{width}"
        height="{height}"
        viewBox="0 0 {width} {height}"
    >
        {"".join(rects)}
    </svg>
    """

    output = graphics_dir / f"aoc-progress-{year}.svg"
    output.write_text(svg)
    print(f"Generated {output}")


# --------------------------
# Generate all SVGs
# --------------------------
years_generated = []
for year_dir in repo_root.iterdir():
    if year_dir.is_dir() and year_dir.name.isdigit():
        generate_year_svg(year_dir)
        years_generated.append(year_dir.name)


# --------------------------
# Update README.md automatically
# --------------------------
readme_path = repo_root / "README.md"
start_marker = "<!-- AOC_PROGRESS_START -->"
end_marker = "<!-- AOC_PROGRESS_END -->"

# Default cleared content between markers
default_content = f"{start_marker}\n{end_marker}"

if readme_path.exists():
    old_content = readme_path.read_text()
    if start_marker in old_content and end_marker in old_content:
        # Reset section to default first
        pre = old_content.split(start_marker)[0]
        post = old_content.split(end_marker)[1]
        readme_content = pre + default_content + post
    else:
        # Append default markers if missing
        readme_content = old_content.strip() + "\n\n" + default_content
else:
    readme_content = default_content

# Now insert the generated SVGs inside markers
lines = [start_marker, ""]
for year in sorted(years_generated):
    lines.append(f"## {year}")
    lines.append(f'<p align="center"><img src="./.github/graphics/aoc-progress-{year}.svg" alt="AoC {year} progress"/></p>\n')
lines.append(end_marker)

# Replace the marker section
readme_content = readme_content.split(start_marker)[0] + "\n".join(lines) + readme_content.split(end_marker)[1]

readme_path.write_text(readme_content)
print(f"Updated {readme_path}")
