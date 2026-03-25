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