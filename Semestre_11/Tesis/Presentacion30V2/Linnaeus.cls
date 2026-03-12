\ProvidesClass{Linnaeus}

\LoadClass[12pt]{beamer}
\RequirePackage{booktabs,pifont,times,mathptmx}

\hypersetup{pdfpagemode=UseThumbs}

%\newcommand{\virg}[1]{``#1''}

\titlegraphic{ \includegraphics[width=0.5\textwidth]{./site_logo.png} }

\mode<beamer>
%\useinnertheme{circles}
%\useinnertheme[shadow]{rounded}
\setbeamertemplate{blocks}[rounded][shadow=true]

%FOTNS AND COLORS

\newcommand{\Linne}{yellow!96!red}

%\setbeamercolor{title page}{bg=\Linne}
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
\setbeamertemplate{navigation  symbols}{}
\setbeamertemplate{frametitle continuation}[from second][(\insertcontinuationcount)]

%PARAGRAPHS

\setlength{\parindent}{0pt}
\setlength{\parskip}{1.5ex}

% footer
\setbeamertemplate{footline}{%
	\centering
	\color{black}
	\rule{0.842\textwidth}{0.35mm} %	
	\vspace{0.05cm} 	
	
  \includegraphics[height=0.6cm]{./site_logo.png}
	
	\vspace{0.1cm} 	
}


%NEW COMMANDS



\newcommand{\ex}[1]{%
\begin{exampleblock}{\textit{Example}}
#1
\end{exampleblock}
}

\newcommand{\titlebox}[2]{%
\begin{block}{#1}
#2
\end{block}
}

\newcommand{\freccia}{\hspace{0.5em}\ding{212}\hspace{0.5em}}


