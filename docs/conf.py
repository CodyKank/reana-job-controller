#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# reana documentation build configuration file, created by
# sphinx-quickstart on Mon Jan 23 14:17:34 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

from __future__ import print_function

import os
import sys

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath('..'))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Do not warn on external images.
suppress_warnings = ['image.nonlocal_uri']

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.coverage',
    'sphinx.ext.doctest',
    'sphinx.ext.graphviz',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
    'sphinxcontrib.httpdomain',
    'sphinxcontrib.redoc',
]

redoc = [
    {
        'page': '_static/api',
        'spec': 'openapi.json',
        'embed': True,
        'opts': {
            'hide-loading': True,
            'hide-hostname': True,
         }
    }
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'reana'
copyright = '2017, info@reana.io'
author = 'info@reana.io'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.

# Get the version string. Cannot be done with import!
g = {}
with open(os.path.join('..', 'reana_job_controller', 'version.py'),
          'rt') as fp:
    exec(fp.read(), g)
    version = g['__version__']

# The full version, including alpha/beta/rc tags.
release = version

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    'logo': 'logo-reana.png',
    'description': """<p>REANA-Job-Controller is a component of the <a
                      href="http://www.reana.io">REANA</a> reusable and
                      reproducible research data analysis
                      platform.</p><p>REANA-Job-Controller takes care of
                      executing and managing jobs on compute clouds.</p>""",
    'github_user': 'reanahub',
    'github_repo': 'reana-job-controller',
    'github_button': False,
    'github_banner': True,
    'show_powered_by': False,
    'extra_nav_links': {
        'REANA@DockerHub': 'https://hub.docker.com/u/reanahub/',
        'REANA@GitHub': 'https://github.com/reanahub',
        'REANA@Twitter': 'https://twitter.com/reanahub',
        'REANA@Web': 'http://www.reana.io',
    }
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar templates, maps document names to template names.
html_sidebars = {
    '**': [
        'about.html',
        'navigation.html',
        'relations.html',
        'searchbox.html',
        'donate.html',
    ]
}

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'reanadoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'reana.tex', 'reana Documentation',
     'info@reana.io', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'reana', 'reana Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'reana', 'reana Documentation',
     author, 'reana', 'One line description of project.',
     'Miscellaneous'),
]

rest_api_modules = ['reana_job_controller.app']


def get_name(full_module_name):
    """
    Pull out the class/function name from the full_module_name.
    Split the full_module_name by "."'s
    """
    # split the full_module_name by "."'s
    module_name = ".".join(full_module_name.split(".")[:2])
    function_name = full_module_name.split('.')[-1]
    return module_name, function_name


def process_docstring(app, what, name, obj, options, lines):
    """
    Deletes unnecessary docstring, saves summary and formats a hyperlink
    to redocs.
    """
    module_name, function_name = get_name(name)
    description = ''
    operation_id = ''
    if what != "module" and module_name in rest_api_modules:
        for line in lines:
            if "summary:" in line:
                description = line.split("summary: ", 1)[1]
            if "operationId:" in line:
                operation_id = line.split('operationId: ', 1)[1]
        url = "`%s <_static/api.html#operation/%s>`_" % (description,
                                                         operation_id)
        # clearing the list of docstrings
        del lines[:]
        # adding back description
        lines.append(url)

# Intersphinx configuration
intersphinx_mapping = {
    'kubernetes': ('https://kubernetes.readthedocs.io/en/latest/', None),
}

def setup(app):
    app.connect('autodoc-process-docstring', process_docstring)
