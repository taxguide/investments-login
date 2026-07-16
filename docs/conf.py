# Configuration file for the Sphinx documentation builder.

project = 'Fidelity Investments Login'
author = 'Fidelity Investments Login'
release = '1.0'

extensions = [
    'sphinx_sitemap',
]

# Templates
templates_path = ['_templates']

exclude_patterns = []

html_theme = 'alabaster'

# Static files
html_static_path = ['_static']

language = 'en'

html_title = "Fidelity Investments Login 2026"

# Sitemap
html_baseurl = "https://fidelity-fidelity-netbenefits-log-in.readthedocs-hosted.com/"
sitemap_url_scheme = "{link}"
