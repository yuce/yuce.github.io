#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Yuce Tekol'
SITENAME = u"yüce's blog"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Istanbul'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('@tklx', 'https://twitter.com/tklx'),
         ('Github', 'https://github.com/yuce'),
)

SOCIAL = (('twitter', 'https://twitter.com/tklx'),
          ('github', 'https://github.com/yuce'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'themes/pelican-hyde'
STATIC_PATHS = ['images', 'favicon.ico']
GA_ACCOUNT = "UA-35253376-2"
PROFILE_IMAGE = 'me.png'