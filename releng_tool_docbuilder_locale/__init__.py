# -*- coding: utf-8 -*-
# Copyright 2021 releng-tool

from sphinx.locale import get_translation
import os


# name of the gettext catalog
MESSAGE_CATALOG_NAME = 'releng-tool-docbuilder'

# translator for messages in documentation
L = get_translation(MESSAGE_CATALOG_NAME)


# register the translator into the html context for templates to use
def add_translation_to_context(app, pagename, templatename, context, doctree):
    context['L'] = L


# register the message catalog into sphinx
def register_message_catalog(app, config):
    locale_dir = os.path.abspath(os.path.dirname(__file__))
    app.add_message_catalog(MESSAGE_CATALOG_NAME, locale_dir)
