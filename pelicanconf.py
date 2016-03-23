#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Ace King'
SITENAME = u"""<span style="color:black;">Wonux</span> <span style="color:#AA1032;">Blog</span>"""
SITEURL = 'http://wonux.github.io'
#SITEURL = 'http://localhost:8000'
#AUTHOR = 'wonux'

TIMEZONE = 'Asia/Shanghai'
DATE_FORMATS = {'en': '%b %d, %Y'}
DEFAULT_LANG = u'en'

DISQUS_SITENAME = 'wonux'

PLUGIN_PATHS = ["../pelican-plugins"]
PLUGINS = ['sitemap', 'extract_toc', 'tipue_search', 'liquid_tags.img', 'neighbors', 'latex', 'related_posts', 'assets', 'share_post', 'multi_part']
MD_EXTENSIONS = ['codehilite(css_class=highlight,linenums=True)', 'extra', 'headerid', 'toc(permalink=true)', 'fenced_code', ]

SITEMAP = {
    'format': 'xml',
    'priorities': {
         'articles': 0.5,
         'indexes': 0.5,
         'pages': 0.5
     },
     'changefreqs': {
         'articles': 'monthly',
         'indexes': 'daily',
         'pages': 'monthly'
     }
}

# Appearance
THEME = '../pelican-elegant'
TYPOGRIFY = True
DEFAULT_PAGINATION = False

# Defaults
DEFAULT_CATEGORY = 'Misc'
USE_FOLDER_AS_CATEGORY = False
ARTICLE_URL = u'{slug}.html'
PAGE_URL = u'{slug}.html'
PAGE_SAVE_AS = u'{slug}.html'


# Feeds
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = 'feeds/%s.atom.xml'

# Social
SOCIAL = (
        ('Weibo', 'http://weibo.com/wonux'),
        ('Github', 'https://github.com/wonux'),
        ('Book', 'https://douban.com/people/wonux'),
        ('Email', 'mailto:wonux@qq.com'),
          )

# Elegant theme
STATIC_PATHS = ['theme/images', 'images']
DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'archives', 'search', '404'))
TAG_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
USE_SHORTCUT_ICONS = True

# Elegant Labels
SOCIAL_PROFILE_LABEL = u'Contact'
RELATED_POSTS_LABEL = 'Keep Reading'
SHARE_POST_INTRO = 'Share on:'
COMMENTS_INTRO = u'Comments Below:'

# Mailchimp
#EMAIL_SUBSCRIPTION_LABEL = u'Get Monthly Updates'
#EMAIL_FIELD_PLACEHOLDER = u'Enter your email...'
#SUBSCRIBE_BUTTON_TITLE = u'Send me Free updates'
#MAILCHIMP_FORM_ACTION = u'empty'

# SMO
TWITTER_USERNAME = u'wonux'
FEATURED_IMAGE = SITEURL + '/theme/images/apple-touch-icon-152x152.png'

# Legal
SITE_LICENSE = u'<span xmlns:dct="http://purl.org/dc/terms/" property="dct:title"> Wonux Blog "</span> by <a xmlns:cc="http://creativecommons.org/ns#" href="http://weibo.com/wonux" property="cc:attributionName" rel="cc:attributionURL">Ace King</a> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/3.0/deed.en_US">Creative Commons Attribution-ShareAlike 3.0 Unported License</a>.'

# SEO
SITE_DESCRIPTION = u'My name is Ace King \u2016 a communication engineer in China Unicom. I am wonux at Github and @wonux at weibo. This is my personal blog.'

# Landing Page
PROJECTS = [
        {
            'name': 'Weibo',
            'url':
            'http://weibo.com/wonux',
            'description': 'My personal media, which shares my daily life, articles and news.'},
        {
            'name': 'Github',
            'url':
            'https://github.com/wonux',
            'description': 'My open source project and code.'},
        {
            'name': 'Douban',
            'url':
            'https://www.douban.com/people/wonux',
            'description': 'My website in douban, that shares my interets in reading, music and movies.'},
        {
            'name': 'Wonux Douban Site',
            'url':
            'https://site.douban.com/271881',
            'description': 'A small website gathering people with common interests on unix/linux.'},
        {   
            'name': 'Wonux Blog in Chinese',
            'url':
            'http://wonux.coding.me',
            'description': 'Another blog published in Coding because of the GFW.'},
        {
            'name': 'Index of my projects',
            'url':
            'http://wonux.github.io/mkdocs',
            'description': 'A project gathering all of my project.'
            }]

LANDING_PAGE_ABOUT = {'title': '孤逐王 开源博客主站/Open Source Master',
        'details': """<div itemscope itemtype="http://schema.org/Person">
        <p>My name is <span itemprop="name">Ace King</span>. I am <a href="https://github.com/wonux/" title="My Github profile" itemprop="url"><span itemprop="nickname">wonux</span></a> at Github and <a href="http://weibo.com/wonux/" title="My Weibo profile" itemprop="url">@孤逐王</a> at Sina Weibo. You can also reach me via <a href="mailto:wonux@qq.com" title="My email address" itemprop="email">email</a>.</p>
        <p>I am a communication engineer working in China Unicom. After work I am a Linux amateur. The first time I used Linux in college，I fell in love with it. As the famous saying goes，"where there is shell,there is a way". It is really cool to work with the command line in the terminal. I Like Unix philosophy and opon source software. I agree with what DistroWatch said "Put the fun back into computing.Use Linux,BSD."</p>
        <p>My favourite Linux distribution is gentoo, as well as arch. And I also dabble in C, C++ and Python. I also often contribute to open source projects and beta test startup products.</p></div>"""}

