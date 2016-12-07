#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'wadou'
SITENAME = 'wadou\'s blog'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'Chinese'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Email', 'wei_pengfei@163.com'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# wadou theme
THEME = "themes/pelican-elegant"

# wadou plugins
PLUGIN_PATHS = ["plugins"]
PLUGINS = ["extract_toc"]

# wadou date
DEFAULT_DATE = 'fs'
DEFAULT_DATE_FORMAT = '%a %Y/%m/%d %H:%M:%S'

# wadou landing page about
LANDING_PAGE_ABOUT = {
        'title': '',
        'details': 'what do you want to know about me?'}