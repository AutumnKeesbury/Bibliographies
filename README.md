## Contents
- CivilWarStudies.bib
  - Sources for my paper on the intersection of carceral and clinical geometries in the context of the CW
- secession.bib
  - A bunch of primary documents about why the south seceded
 
## How to Use
### Updating .bib files
  To update .bib files, use JabRef to add/remove/edit sources, and then cd to '/Users/autumn/bib', and run
  '
  git add .
  git commit
  git push
  '
### Importing specific .bib file
  To import a given .bib file, if you're in nvim, press F7 to open ToggleTerm, and then run
  '
   curl 'https://raw.githubusercontent.com/AutumnKeesbury/Bibliographies/refs/heads/main/example.bib' > ref.bib
  '
  but replacing 'example.bib' with the name of the .bib file.
