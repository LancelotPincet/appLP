# Configuration file for the Sphinx documentation builder.

import os
import sys
import toml

# Add path
sys.path.insert(0, os.path.abspath('../../src'))

# Project informations
project = 'appLP'
copyright = '2025, Lancelot PINCET'
author = 'Lancelot PINCET'
with open('../../pyproject.toml') as file :
    data = toml.load(file)
version = data['project']['version']
release = version
master_doc = 'index'

# Sphinx extensions
extensions = [
    'sphinx.ext.autodoc', # reads the docstrings
    'sphinx.ext.viewcode', # links to the codes
    'sphinx.ext.napoleon', # Google/NumPy docstrings
    'sphinx.ext.todo', # Google/NumPy docstrings
    'sphinx_design', # Enable tabs, dropdowns, cards and alerts
    ]

exclude_patterns = []

# Build
html_theme = 'sphinx_rtd_theme'
suppress_warnings = ['toc.excluded', 'toc.dupe']

# -----------------------------
# PDF / LaTeX styling
# -----------------------------

# Use XeLaTeX for modern fonts and Unicode support
latex_engine = 'xelatex'

# LaTeX document settings
latex_documents = [
    (master_doc, f'{project}.tex', f'{project} Documentation',
     author, 'manual'),
]

# Customize LaTeX elements
latex_elements = {
    # Paper size and font size
    'papersize': 'a4paper',
    'pointsize': '11pt',
    'figure_align': 'htbp',

    # Preamble: fonts, colors, boxes, and code
    'preamble': r'''
% -----------------------------
% Fonts
% -----------------------------
\usepackage{fontspec}
\setmainfont{TeX Gyre Termes} % serif font for body
\setsansfont{TeX Gyre Heros} % sans-serif like RTD
\setmonofont{Fira Code}[Contextuals=Alternate,Scale=MatchLowercase,FakeSlant=0.2]
\setlength{\headheight}{14pt}

\usepackage{setspace}
\onehalfspacing

% -----------------------------
% Colored boxes for notes and warnings
% -----------------------------
\usepackage{tcolorbox}
\tcbuselibrary{listings}

\newtcolorbox{notebox}{
  colback=blue!5!white,
  colframe=blue!75!black,
  boxrule=0.5pt,
  arc=4pt,
  left=2mm, right=2mm, top=1mm, bottom=1mm
}
\newtcolorbox{warningbox}{
  colback=red!5!white,
  colframe=red!75!black,
  boxrule=0.5pt,
  arc=4pt,
  left=2mm, right=2mm, top=1mm, bottom=1mm
}\newtcolorbox{tipbox}{
  colback=green!5!white,
  colframe=green!75!black,
  boxrule=0.5pt, arc=4pt, left=2mm, right=2mm, top=1mm, bottom=1mm
}
\newtcolorbox{importantbox}{
  colback=yellow!5!white,
  colframe=yellow!75!black,
  boxrule=0.5pt, arc=4pt, left=2mm, right=2mm, top=1mm, bottom=1mm
}
\newtcolorbox{cautionbox}{
  colback=orange!5!white,
  colframe=orange!75!black,
  boxrule=0.5pt, arc=4pt, left=2mm, right=2mm, top=1mm, bottom=1mm
}

% Map Sphinx admonitions to tcolorbox
\renewenvironment{sphinxnote}{\begin{notebox}}{\end{notebox}}
\renewenvironment{sphinxwarning}{\begin{warningbox}}{\end{warningbox}}
\renewenvironment{sphinxtip}{\begin{tipbox}}{\end{tipbox}}
\renewenvironment{sphinximportant}{\begin{importantbox}}{\end{importantbox}}
\renewenvironment{sphinxcaution}{\begin{cautionbox}}{\end{cautionbox}}

% -----------------------------
% Code block styling
% -----------------------------
\usepackage{listings}
\usepackage{xcolor}

\lstset{
  basicstyle=\ttfamily\small,
  keywordstyle=\color{blue},
  commentstyle=\color{gray},
  stringstyle=\color{orange},
  breaklines=true,
  frame=single,
  frameround=tttt,
  backgroundcolor=\color{gray!5},
}
''',
}

