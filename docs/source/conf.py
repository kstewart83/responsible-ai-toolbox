# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------

project = "rai-toolbox"
copyright = "2022 Massachusetts Institute of Technology"
author = "Ryan Soklaski, Justin Goodwin, Olivia Brown, Michael Yee"

# The short X.Y version
version = ""
# The full version, including alpha/beta/rc tags
release = ""


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
    "sphinx.ext.githubpages",
    "sphinx.ext.autosummary",
    "numpydoc",
    "sphinx_copybutton",
    "sphinx_tabs.tabs",
    "nbsphinx",
]

# Strip input prompts:
# https://sphinx-copybutton.readthedocs.io/en/latest/#strip-and-configure-input-prompts-for-code-cells
copybutton_prompt_text = r">>> |\.\.\. |\$ |In \[\d*\]: | {2,5}\.\.\.: | {5,8}: "
copybutton_prompt_is_regexp = True


default_role = "py:obj"

autodoc_typehints = "none"
numpydoc_show_class_members = False

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
}

autosummary_generate = False

# https://www.sphinx-doc.org/en/master/usage/extensions/extlinks.html
# A dictionary of external sites
#   alias ->  (base-URL, prefix)
_repo = "https://github.com/mit-ll-responsible-ai/responsible-ai-toolbox"
extlinks = {
    "commit": (_repo + "commit/%s", "commit "),
    "gh-file": (_repo + "blob/master/%s", ""),
    "gh-link": (_repo + "%s", ""),
    "issue": (_repo + "issues/%s", "issue #"),
    "pull": (_repo + "pull/%s", "pull request #"),
    "plymi": ("https://www.pythonlikeyoumeanit.com/%s", ""),
    "hydra": ("https://hydra.cc/docs/%s", ""),
}

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "pydata_sphinx_theme"
html_logo = "../../brand/logo_no_text.png"

html_theme_options = {
    "collapse_navigation": True,
    "navigation_depth": 4,
    "icon_links": [
        {
            "name": "GitHub",
            "url": _repo,
            "icon": "fab fa-github-square",
        },
    ],
    "favicons": [
        {
            "rel": "icon",
            "sizes": "16x16",
            "href": "favicon-16x16.png",
        },
        {
            "rel": "icon",
            "sizes": "32x32",
            "href": "favicon-32x32.png",
        },
        {
            "rel": "apple-touch-icon",
            "sizes": "180x180",
            "href": "apple-touch-icon.png",
        },
    ],
}


# def setup(app):
#     app.add_js_file(
#         "https://www.googletagmanager.com/gtag/js?id=UA-115029372-2",
#         loading_method="async",
#     )
#     app.add_js_file("gtag.js")


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
