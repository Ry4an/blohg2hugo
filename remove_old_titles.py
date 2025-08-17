"""
Removes markup titles from rst pages.  Modifies in place, so have a clean
checkout before letting it run wild.

Takes the filenames to tweak as arguments.
"""

import sys
import re

pattern = r'^title\s*=\s*"(.*?)"'

for filename in sys.argv[1:]:
    print(f"Munging {filename}...")

    with open(filename, 'r') as original:
        lines = original.readlines()

    match = None
    for line in lines:
        match = re.search(pattern, line)
        if match:
            print(f"\tFound title: {match.group(1)}")
            break

    if not match:
        print("\tUnable to find title. Skipping")
        continue

    skip = 0
    with open (filename, 'w') as modified: 
        for line in lines:
            if line.rstrip() == match.group(1):
                skip = 2
            if skip:
                skip -= 1
                print("\t Skipping:", line.rstrip())
            else:
                modified.write(line)
