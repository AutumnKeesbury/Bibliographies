import bibtexparser
import re

bibfile = "CivilWarStudies.bib"
library = bibtexparser.parse_file(bibfile)
if len(library.failed_blocks) > 0:
    print("Some blocks failed to parse. Check the entries of `library.failed_blocks`.")
else:
    print("All blocks parsed successfully.")

key_pattern = r"[a-z]{4}:\d|\d{2}:\d{4}"
key_regex = re.compile(key_pattern)


def keyMatch(key):
    return bool(key_regex.match(key))


new_lib = bibtexparser.Library()

key_reel = []
key_frame = []
indicies = []

for entry in library.entries:
    key = entry.key
    if keyMatch(key):
        key_split = re.split(r":", key)

        reel = key_split[1]
        key_reel.append(reel)

        try:
            entry.__getitem__("index")
        except:
            entry.__setitem__("index", f"f{key_split[2]}")

        index = str(entry.__getitem__("index"))

        indicies.append(entry.get("key"))

        key = f"ussc:{reel}:{index}"
        print(f"new key = {key}\n")
        entry.key = key
    new_lib.add(entry)


bibtexparser.write_file(
    "CivilWarStudies_reformatted.bib",
    new_lib,
    bibtex_format=bibtexparser.BibtexFormat(),
)
