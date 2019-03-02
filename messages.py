#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2019 releng-tool

import gettext
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
locale_dir = os.path.join(base_dir, 'locale')

# load translator
language = os.environ['RELENG_LANGUAGE']
t = gettext.translation('messages',localedir=locale_dir, languages=[language],
    fallback = True)
_ = t.gettext

# ##############################################################################

#: message to identify Documentation based of a development version
DEVELOPMENT_MSG = _('development version')

#: message to identify Documentation based of a legacy version
LEGACY_MSG = _('legacy version')

#: message to identify the most recent stable release
STABLE_MSG = _('stable v{}')
