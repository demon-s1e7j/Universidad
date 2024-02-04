(TeX-add-style-hook
 "main"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("revtex4-1" "a4paper" "amsfonts" "amssymb" "amsmath" "reprint" "showkeys" "nofootinbib" "twoside")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("babel" "spanish") ("inputenc" "utf8") ("todonotes" "colorinlistoftodos" "color=green!40" "prependcaption") ("geometry" "left=23mm" "right=13mm" "top=35mm" "columnsep=15pt") ("fontenc" "T1") ("ulem" "normalem") ("hyperref" "pdftex" "pdftitle={Article}" "pdfauthor={Author}")))
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "path")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "url")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "nolinkurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperbaseurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperimage")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "href")
   (add-to-list 'LaTeX-verbatim-macros-with-delims-local "path")
   (TeX-run-style-hooks
    "latex2e"
    "revtex4-1"
    "revtex4-110"
    "babel"
    "inputenc"
    "float"
    "todonotes"
    "amsthm"
    "mathtools"
    "physics"
    "xcolor"
    "graphicx"
    "geometry"
    "adjustbox"
    "placeins"
    "fontenc"
    "lipsum"
    "csquotes"
    "ulem"
    "hyperref")
   (LaTeX-add-labels
    "tab:table3"
    "fig:my_label")
   (LaTeX-add-bibliographies
    "Referencias"))
 :latex)

