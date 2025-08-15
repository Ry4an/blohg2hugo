"""
Adds front matter to the file, drawing from git and the input restructedText
file itself.  Modifies in place, so have a clean checkout before letting it
run wild.

Requires ADDED_DATES.tsv in current directory

Takes the filenames to tweak as arguments, which much have matching pathes in
ADDED_DATES.tsv.
"""

import sys
from textwrap import dedent
from datetime import datetime

added_date = {}
with open('ADDED_DATES.tsv', 'r') as added_dates:
    added_date.update([line.rstrip().split("\t") for line in added_dates])

for filename in sys.argv[1:]:
    print(f"Munging {filename}...")

    with open(filename, 'r') as original:
        lines = original.readlines()

    title = lines[0].strip() or lines[1].strip()

    tags=set()
    date = added_date[filename]
    for line in lines:
        if line.startswith(".. tags: "):
            tags.update([tag.strip() for tag in line[9:].split(",")])
        if line.startswith(".. date: "):
            date = datetime.fromtimestamp(int(line[9:].strip())).isoformat()

    tags_str = ", ".join(f'"{tag}"' for tag in tags)

    front_matter = dedent(f"""\
            +++
            title = "{title}"
            date = "{date}"
            tags = [{tags_str}]
            +++

    """)

    print(f"\n{front_matter}-----------------\n")

    with open (filename, 'w') as modified:
        modified.writelines(front_matter)
        modified.writelines(lines)
