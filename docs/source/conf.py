# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Sphinx Test'
copyright = '2023, Pablo'
author = 'Pablo'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
    'sphinxcontrib.confluencebuilder',
    'sphinx_copybutton',
    'sphinx.ext.napoleon',
    'autodoc2',
    'nbsphinx'
]


source_suffix = {
    '.rst': 'restructuredtext',
    '.text': 'markdown',
    '.md': 'markdown'
}

templates_path = ['_templates']
exclude_patterns = []

# -- Options for Myst --------------------------------------------------------

myst_enable_extensions = [
    'colon_fence'
]

# -- Options for Autodoc2 ----------------------------------------------------

autodoc2_packages = [
    "../../src"
]

autodoc2_output_dir = "source-docs"

# -- Options for ConfluenceBuilder -------------------------------------------
confluence_publish = True
confluence_space_key = 'SD'
confluence_parent_page = 'MyDocumentation'

confluence_server_url = 'https://ices2.atlassian.net/wiki/'
confluence_server_user = 'pjt1991@gmail.com'
confluence_server_pass = 'ATATT3xFfGF0RQ_RGJfpQYudmb-rMJktJwNIbBXO4XmNPiJp-h_VyI_Cw6YPZi-Zo_mP7huMds65-G2rZlHRRgIG_PU6gJ7CquL3gkMMcqe4CGWBncs4Xbx7StVvbEw2y_ztVeOsb8M-eNX8zHStkkQgMx8Ck2i3m0T_sk-fhQtgs9SR9mAibbs=6298EDCD'

confluence_publish_postfix = ' (auto-generated)'

# confluence_publish_dryrun = True
# confluence_publish_debug = True



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_theme_options = {
    "source_repository": "https://github.com/IceS2/sphinx-test/",
    "source_branch": "main",
    "source_directory": "docs/source/"
}
html_static_path = ['_static']
