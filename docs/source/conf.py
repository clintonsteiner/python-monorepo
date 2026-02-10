# Configuration file for the Sphinx documentation builder.


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
html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_logo = "_static/hildie.jpeg"
html_favicon = "_static/hildie.jpeg"

html_theme_options = {
    "logo_only": False,
    "display_version": True,
}

# -- Intersphinx configuration -----------------------------------------------
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}
