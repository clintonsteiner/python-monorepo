# Configuration file for the Sphinx documentation builder.

import os
import sys

# Add the project root to the path so autodoc can find the modules
sys.path.insert(0, os.path.abspath("../.."))

# -- Project information -----------------------------------------------------
project = "Hildie"
copyright = "2026, Clinton Steiner"
author = "Clinton Steiner"
release = "0.1.0"

# -- General configuration ---------------------------------------------------
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
]

templates_path = ["_templates"]
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
html_theme = "alabaster"  # Built-in theme, no extra package needed
html_static_path = ["_static"]
html_logo = "_static/hildie.png"
html_favicon = "_static/hildie.png"

html_theme_options = {
    "logo": "hildie.png",
    "logo_name": True,
    "description": "Named after Hildie, because all the good names were taken!",
    "github_user": "clintonsteiner",
    "github_repo": "python-monorepo",
}

# -- Intersphinx configuration -----------------------------------------------
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}
