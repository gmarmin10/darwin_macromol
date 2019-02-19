# -*- coding: utf-8 -*-
#
# MITgcm documentation build configuration file, created by
# sphinx-quickstart on Tue Jun  6 11:04:04 2017.
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
import os
import sys
sys.path.insert(0, os.path.join(os.path.abspath('.'), '_extensions'))


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinxcontrib.bibtex',
    'mitgcm']

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
project = u'MITgcm'
copyright = u'1997-, MITgcm contributors'
# When updating the list of authors, remember to also
# change the LaTeX list below and the list in index.rst
author = u'Alistair Adcroft, Jean-Michel Campin, Ed Doddridge, Stephanie Dutkiewicz, Constantinos Evangelinos, David Ferreira, Mick Follows, Gael Forget, Baylor Fox-Kemper, Patrick Heimbach, Chris Hill, Ed Hill, Helen Hill, Oliver Jahn, Jody Klymak, Martin Losch, John Marshall, Guillaume Maze, Matt Mazloff, Dimitris Menemenlis, Andrea Molod, and Jeff Scott'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#

from subprocess import check_output, CalledProcessError

def get_version():
    """
    Return the latest tag (checkpoint) and, if there have
    been commits since the version was tagged, the commit hash.

    To get just the release tag use:
    version = version.split('-')[0]
    """

    try:
        version = check_output(['git', 'describe', '--tags', '--always'],
                               universal_newlines=True)
    except CalledProcessError:
        return 'unknown version'

    return version.rstrip()

# "version" is used for html build
version = get_version()
# "release" is used for LaTeX build
release = version



# The language for content autogenerated by Sphinx. 
# Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# Do not highlight code blocks unless a language is specified explicitly.
highlight_language = 'none'

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# number figures

numfig_format = {'figure': 'Figure %s',
                 'table': 'Table %s',
                 'code-block': 'Code %s',
                }

numfig = True

# number figures within section
numfig_secnum_depth = 1

#math_number_all = True

numfig_format = {'figure': 'Figure %s', 'table': 'Table %s', 'code-block': 'Listing %s', 'section': 'Section %s'}

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#html_theme = 'alabaster'

import sphinx_rtd_theme

html_theme = "sphinx_rtd_theme"

html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'MITgcmdoc'


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
    'preamble': r'''
    \setcounter{secnumdepth}{3}
    \newcommand{\p}[1]{\frac{\partial }{\partial #1}}
    \newcommand{\pp}[2]{\frac{\partial #1}{\partial #2}}
    \newcommand{\dd}[2]{\frac{d #1}{d #2}}
    \newcommand{\h}{\frac{1}{2}}
    \newcommand{\op}[1]{\operatorname{#1}}
    \setlength{\tymax}{0.5\textwidth}
    ''',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'MITgcm.tex', u'MITgcm Documentation',
     u'Alistair Adcroft, Jean-Michel Campin, Ed Doddridge, \\and Stephanie Dutkiewicz, Constantinos Evangelinos, \\and David Ferreira, Mick Follows, Gael Forget, \\and Baylor Fox-Kemper, Patrick Heimbach, Chris Hill, Ed Hill, \\and Helen Hill, Oliver Jahn, Jody Klymak, Martin Losch, \\and John Marshall, Guillaume Maze, Matt Mazloff, \\and Dimitris Menemenlis, Andrea Molod, and Jeff Scott', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'mitgcm', u'MITgcm Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'MITgcm', u'MITgcm Documentation',
     author, 'MITgcm', 'A highly configurable general circulation model.',
     'Miscellaneous'),
]

def setup(app):
    app.add_stylesheet('css/custom.css')
    app.add_stylesheet('css/wrap_tables.css')
