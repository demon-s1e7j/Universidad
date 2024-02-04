(TeX-add-style-hook
 "main"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("exam" "12pt")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("inputenc" "utf8") ("geometry" "margin=1in") ("enumitem" "shortlabels")))
   (add-to-list 'LaTeX-verbatim-environments-local "lstlisting")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "lstinline")
   (add-to-list 'LaTeX-verbatim-macros-with-delims-local "lstinline")
   (TeX-run-style-hooks
    "latex2e"
    "exam"
    "exam12"
    "amsthm"
    "libertine"
    "inputenc"
    "geometry"
    "amsmath"
    "amssymb"
    "multicol"
    "enumitem"
    "siunitx"
    "cancel"
    "graphicx"
    "pgfplots"
    "listings"
    "tikz")
   (TeX-add-symbols
    "class"
    "examnum"
    "examdate"
    "timelimit"))
 :latex)

