#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2019 releng-tool

from releng_tool_docbuilder_locale import L
from releng_tool_docbuilder_locale import add_translation_to_context
from releng_tool_docbuilder_locale import register_message_catalog
import os
import sys


if 'RELENG_TARGET_DIR' not in os.environ:
    raise SyntaxError('target directory not provided')

base_dir = os.path.dirname(os.path.abspath(__file__))
releng_tool_dir = os.path.abspath(os.environ['RELENG_TARGET_DIR'])
releng_tool_doc_dir = os.path.join(releng_tool_dir, 'Documentation')

# inject releng-tool into system path to allow autodocs content to render
sys.path.insert(0, releng_tool_dir)

# load releng-tool's sphinx configuration
releng_tool_conf = os.path.join(releng_tool_doc_dir, 'conf.py')
with open(releng_tool_conf, 'rb') as source_file:
    code = compile(source_file.read(), releng_tool_conf, 'exec')
exec(code, globals(), locals())
try:
    releng_tool_doc_setup = setup
except NameError:
    releng_tool_doc_setup = None

# builder sphinx configuration
canonical_url = 'https://docs.releng.io/'
html_show_copyright = False
html_show_sphinx = True

# check if we are using a legacy theme (v0.9 and older), as we will still apply
# an older theme on older revisions
legacy_theme = html_theme != 'furo'

# theme overrides
if not legacy_theme:
    templates_path = [
        os.path.join(base_dir, 'templates/'),
    ]

    html_js_files = [
        'theme_overrides_global.js',
    ]

    html_static_path.append(os.path.join(base_dir, '_static/'))

# legacy theme
else:
    templates_path = [
        os.path.join(base_dir, 'legacy', 'templates/'),
    ]

    html_theme_options['canonical_url'] = canonical_url
    html_static_path.append(os.path.join(base_dir, 'legacy', '_static/'))

# note: v0.8 older injected into the html context
try:
    html_context
except NameError:
    html_context = {}

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

if 'RELENG_LOCALE_DIR' not in os.environ:
    raise SyntaxError('locale directory not provided')
locale_dirs = [os.environ['RELENG_LOCALE_DIR']]


def build_announcement():
    announcement = None
    stable_text = L('Stable v{}').format(most_stable_version)
    stable_data = '<a href="{}/{}/latest/">{}</a>'.format(
        canonical_url,
        language,
        stable_text
        )
    if version == 'development':
        announcement = L('Development Version') + ' | ' + stable_data
    elif version != most_stable_version and version != 'latest':
        announcement = L('Legacy Version') + ' | ' + stable_data

    return announcement


def configure_furo_announcement(app, config):

    # inject an announcement message into furo theme (if needed)
    announcement = build_announcement()
    if announcement:
        html_theme_options['announcement'] = build_announcement()


def configure_lang_context(app, pagename, templatename, context, doctree):

    # configure a version string for the version box's title area
    if version == 'development':
        context['version_str'] = L('Development')
    elif version == 'latest':
        context['version_str'] = L('Latest')
    else:
        context['version_str'] = version

    # inject an announcement message into legacy theme (if needed)
    announcement = build_announcement()
    if announcement:
        context['version_warning'] = announcement


def setup(app):
    theme_override = 'theme_overrides_global.css'

    # invoke releng-tool's documentation setup
    if releng_tool_doc_setup:
        releng_tool_doc_setup(app)

        # inject additional theme overrides
        app.add_css_file(theme_override)
    else:
        html_context['css_files'].append('_static/' + theme_override)

    # point application documentation to releng-tool's set
    app.confdir = releng_tool_doc_dir
    app.srcdir = releng_tool_doc_dir

    # register locale support
    app.connect('config-inited', register_message_catalog)
    app.connect('html-page-context', add_translation_to_context)

    app.connect('html-page-context', configure_lang_context)
    if not legacy_theme:
        app.connect('config-inited', configure_furo_announcement)
