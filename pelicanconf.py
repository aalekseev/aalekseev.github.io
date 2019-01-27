#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Anton Alekseev'
SITENAME = 'Robotehnik Thoughts'
SITEURL = ''

PATH = 'content'
TIMEZONE = 'Europe/Tallinn'
DEFAULT_LANG = 'en'
THEME = 'theme'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

MENUITEMS = (
    ('All posts', '/'),
)

LINKS = (
    ('GitHub', 'https://github.com/aalekseev'),
    ('LinkedIn', 'https://linkedin.com/in/robotehnik/'),
)

# GitHub Pages
STATIC_PATHS = ['extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

DEFAULT_PAGINATION = False
