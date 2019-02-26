#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2019 releng-tool

from sphinx.util.pycompat import execfile_
import os
import sys

base_dir = os.path.dirname(os.path.abspath(__file__))
releng_tool_dir = os.path.join(base_dir, 'releng-tool')
releng_tool_doc_dir = os.path.join(releng_tool_dir, 'Documentation')

# inject releng-tool into system path to allow autodocs content to render
sys.path.insert(0, releng_tool_dir)

# load releng-tool's sphinx configuration
execfile_(os.path.join(releng_tool_doc_dir, 'conf.py'), globals())

# theme overrides
templates_path = [os.path.join(base_dir, '_templates/')]

# version/language information
if 'RELENG_VERSION' not in os.environ:
    raise SyntaxError('version not provided')
version = os.environ['RELENG_VERSION']

if 'RELENG_VERSIONS' not in os.environ:
    raise SyntaxError('supported versions not provided')
html_context['versions'] = os.environ['RELENG_VERSIONS'].split(',')

if 'RELENG_LANGUAGES' not in os.environ:
    raise SyntaxError('supported languages not provided')
html_context['languages'] = os.environ['RELENG_LANGUAGES'].split(',')

# localization options
if 'RELENG_LOCALE_DIR' not in os.environ:
    raise SyntaxError('locale directory not provided')

locale_dirs = [os.environ['RELENG_LOCALE_DIR']]
gettext_compact = False

# overrides
html_show_copyright = False
html_show_sphinx = True

def setup(app):
    # point application documentation to releng-tool's set
    app.confdir = releng_tool_doc_dir
    app.srcdir = releng_tool_doc_dir
