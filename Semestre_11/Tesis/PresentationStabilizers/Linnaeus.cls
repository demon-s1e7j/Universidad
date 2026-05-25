\ProvidesClass{Linnaeus}

\LoadClass[12pt]{beamer}
\RequirePackage{booktabs,pifont,times,mathptmx}

% Soporte para referencias en el pie de página
\RequirePackage[backend=biber, style=verbose, autocite=footnote]{biblatex}

\hypersetup{pdfpagemode=UseThumbs}

\titlegraphic{ \includegraphics[width=0.4\textwidth]{./site_logo.png} }

\mode<beamer>
\setbeamertemplate{blocks}[rounded][shadow=true]

% COLORES Y FUENTES
\newcommand{\Linne}{yellow!96!red}

\setbeamercolor{background canvas}{bg=\Linne}
\setbeamercolor{title}{fg=black}
\setbeamercolor{normal text}{fg=black}
\setbeamercolor{frametitle}{fg=black}
\setbeamerfont{frametitle}{series=\bfseries}   
\setbeamercolor{item}{fg=black}
\setbeamercolor{block title}{fg=black, bg=\Linne}
\setbeamerfont{block title}{size=\large, series=\bfseries}   
\setbeamerfont{block body}{size=\small}
\setbeamercolor{block body}{fg=black}

% Ajuste de color para las notas al pie (Footnotes)
\setbeamercolor{footnote}{fg=black}
\setbeamercolor{footnote mark}{fg=black}
\setbeamerfont{footnote}{size=\tiny}

\setbeamertemplate{navigation symbols}{}
\setbeamertemplate{frametitle continuation}[from second][(\insertcontinuationcount)]

% PARAGRAPHS
\setlength{\parindent}{0pt}
\setlength{\parskip}{1.5ex}

% FOOTER (Línea decorativa original)
\setbeamertemplate{footline}{%
    \centering
    \color{black}
    \rule{0.842\textwidth}{0.35mm} 
    \vspace{0.1cm}   
}
