#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2019 releng-tool

from sphinx.util.pycompat import execfile_
import os
import sys

base_dir = os.path.dirname(os.path.abspath(__file__))
releng_tool_dir = os.path.join(base_dir, '.releng_work', 'releng-tool')
releng_tool_doc_dir = os.path.join(releng_tool_dir, 'Documentation')

# inject releng-tool into system path to allow autodocs content to render
sys.path.insert(0, releng_tool_dir)

# load releng-tool's sphinx configuration
execfile_(os.path.join(releng_tool_doc_dir, 'conf.py'), globals())

# theme overrides
templates_path = [
    os.path.join(releng_tool_doc_dir, '_templates/'),
    os.path.join(base_dir, '_templates/'),
]

# version/language information
if 'RELENG_VERSION' not in os.environ:
    raise SyntaxError('version not provided')
version = os.environ['RELENG_VERSION']

if 'RELENG_VERSIONS' not in os.environ:
    raise SyntaxError('supported versions not provided')
html_context['versions'] = os.environ['RELENG_VERSIONS'].split(',')

if 'RELENG_STABLE' not in os.environ:
    raise SyntaxError('stable version not provided')
most_stable_version = os.environ['RELENG_STABLE']

if 'RELENG_LANGUAGE' not in os.environ:
    raise SyntaxError('language not provided')
language = os.environ['RELENG_LANGUAGE']

if 'RELENG_LANGUAGES' not in os.environ:
    raise SyntaxError('supported languages not provided')
html_context['languages'] = os.environ['RELENG_LANGUAGES'].split(',')

sys.path.insert(0, base_dir)
from messages import *

stable_text = STABLE_MSG.format(most_stable_version)
stable_data = '<a href="https://docs.releng.io/{}/latest/">{}</a>'.format(
    language,
    stable_text
    )
if version == 'master':
    html_context['version_warning'] = DEVELOPMENT_MSG + ' | ' + stable_data
elif version != most_stable_version and version != 'latest':
    html_context['version_warning'] = LEGACY_MSG + ' | ' + stable_data

# localization options
if 'RELENG_LOCALE_DIR' not in os.environ:
    raise SyntaxError('locale directory not provided')

locale_dirs = [os.environ['RELENG_LOCALE_DIR']]
gettext_compact = False

# overrides
html_theme_options['canonical_url'] = 'https://docs.releng.io/'
html_show_copyright = False
html_show_sphinx = True

def setup(app):
    # point application documentation to releng-tool's set
    app.confdir = releng_tool_doc_dir
    app.srcdir = releng_tool_doc_dir
