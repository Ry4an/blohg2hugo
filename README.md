Get Initial Creation Date
=========================
This was close but had some dates wrong:
```
git ls-tree -r --name-only HEAD | while read filename; do echo -e "$filename\t$(git log --date=iso-strict -1 --format="%ad" -- "$filename")"; done | grep '\.rst' >| ADDED_DATES.tsv
```

This was correct, but needed some text munging for hugo to like its iso format
```
for filename in $(find content/post -name '*.rst') ; do echo -n $filename; hg log --template '\t{date|isodate}\n' -r 0:tip -l 1 $filename; done >| ADDED_DATES.tsv
```

Adding Front Matter
===================

Used [a script](add_front_matter.py) like this: `find content/post -name '*.rst' | xargs python3 add_front_matter.py`

Fix Images and Attachments
==========================
Blohg used a non-standard image tag, but it's near identical to the real one,
and fixed with:

`rg -l '\.\. attachment-image' | xargs perl -p -i -e 's/^\.\. attachment-image:: /.. image:: \/unblog\/attachments\//'`
