Here are the scripts and notes I needed to convert [my
blog](https://ry4an.org/unblog/) from blohg to hugo.  I wrote a bit about the
process here: https://ry4an.org/unblog/post/unblog-generation-four/ .  All of
the steps can be seen in the [blog's
repository](https://github.com/Ry4an/unblog).

## TODO

 - [x] get title corrected
 - [x] get favicon corrected
 - [x] get /unblog/resume/ working
 - [x] fix inline images in rst
 - [x] fix code snippets in rst
 - [x] create footer
 - [x] create header
 - [x] create a md post template
 - [x] first md post
 - [x] verify tags work
 - [x] decide if subtitle should show
 - [x] remove manual titles in rst posts
 - [x] verify rss works
 - [x] redirect old atom feed
 - [x] remove :page: links
 - [x] remove `.. youtube` directives
 - [x] remove old literal syntax highlighting javascript
 - [x] Clean up this README

## Get Initial Creation Date
This was close but had some dates wrong:
```
git ls-tree -r --name-only HEAD | while read filename; do echo -e "$filename\t$(git log --date=iso-strict -1 --format="%ad" -- "$filename")"; done | grep '\.rst' >| ADDED_DATES.tsv
```

This was correct, but needed some text munging for hugo to like its iso format
```
for filename in $(find content/post -name '*.rst') ; do echo -n $filename; hg log --template '\t{date|isodate}\n' -r 0:tip -l 1 $filename; done >| ADDED_DATES.tsv
```

## Adding Front Matter

Used [add_front_matter.py](add_front_matter.py) like this: `find content/post -name '*.rst' | xargs python3 add_front_matter.py`

## Fix Images and Attachments
Blohg used a non-standard image tag, but it's near identical to the real one,
and fixed with:

`rg -l '\.\. attachment-image' | xargs perl -p -i -e 's/^\.\. attachment-image:: /.. image:: \/unblog\/attachments\//'`

## Removing Old Titles

With blohg the title needed to be in the markup, but the hugo template handles
that, so I used [remove_old_titles.py](remove_old_titles.py) like this: `find content/post -name '*.rst' | xargs python3 remove_old_titles.py`
