import bibtexparser

bibfile = "CivilWarStudies_reformatted.bib"
library = bibtexparser.parse_file(bibfile)

if len(library.failed_blocks) > 0:
    print("Some blocks failed to parse. Check the entries of `library.failed_blocks`.")
else:
    print("All blocks parsed successfully.")

for entry in library.entries:
    if entry.entry_type == "misc":
        entry.__setitem__("keywords", "primary")
    else:
        entry.__setitem__("keywords", "secondary")


bibtexparser.write_file(
    "CWStudies_v3.bib", library, bibtex_format=bibtexparser.BibtexFormat()
)
