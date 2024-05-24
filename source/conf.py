import os
import sys

sys.path.insert(0, os.path.abspath("."))

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "myst_parser",
    "sphinx_autoapi.extension",
    "sphinx_rtd_theme",
    "sphinx_github_changelog",
]

github_project_url = "https://github.com/rohitsh26/sphinx-changelog-poc"

templates_path = ["_templates"]
master_doc = "index"
project = "Sphinx Changelog POC"
author = "Your Name"
