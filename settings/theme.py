# -*- coding:utf-8 -*-
from collections import OrderedDict

# ---------------------------------------------------------------
# Site Information Settings
# ---------------------------------------------------------------

SITE_TITLE = "FooFish's Notes"

SITE_SUBTITLE = u"不一样的烟火"

# Put your favicon.ico into `hexo-site/source/` directory.
FAVICON = "/favicon.ico"

# Set default keywords (Use a comma to separate)
KEYWORDS = "FooFish, Python"

# Set rss to false to disable feed link.
# Leave rss as empty to use site's feed link.
# Set rss to specific value if you have burned your feed already.
RSS = "/rss/"

# Specify the date when the site was setup
# since: 2015

# Canonical, set a canonical link tag in your hexo, you could use it for your SEO of blog.
# See: https://support.google.com/webmasters/answer/139066
# Tips: Before you open this tag, remeber set up your URL in hexo _config.yml ( ex. url: http://yourdomain.com )
canonical = True

# ---------------------------------------------------------------
# Menu Settings
# ---------------------------------------------------------------
MENU = OrderedDict(sorted({
                              "home": {"label": u"首页", "path": "/", "icon": "home", "position": 1},
                              "categories": {"label": u"分类", "path": "/categories", "icon": "th", "position": 3},
                              "archives": {"label": u"归档", "path": "/archives", "icon": "archive", "position": 2},
                              "tags": {"label": u"标签", "path": "/tags", "icon": "tags", "position": 4},
                              "about": {"label": u"关于", "path": "/about", "icon": "user", "position": 5},

                          }.items(), key=lambda t: t[1]['position']))

# ---------------------------------------------------------------
# Scheme Settings
# ---------------------------------------------------------------
SCHEME = "Pisces"
#
# # ---------------------------------------------------------------
# # Font Settings
# # - Find fonts on Google Fonts (https://www.google.com/fonts)
# # - All fonts set here will have the following styles:
# #     light, light italic, normal, normal intalic, bold, bold italic
# # - Be aware that setting too much fonts will cause site running slowly
# # - Introduce in 5.0.1
# # ---------------------------------------------------------------
# font:
#   enable: true
#
#   # Uri of fonts host. E.g. //fonts.googleapis.com (Default)
#   host:
#
#   # Global font settings used on <body> element.
#   global:
#     # external: true will load this font family from host.
#     external: true
#     family: Lato
#
#   # Font settings for Headlines (h1, h2, h3, h4, h5, h6)
#   # Fallback to `global` font settings.
#   headings:
#     external: true
#     family:
#
#   # Font settings for posts
#   # Fallback to `global` font settings.
#   posts:
#     external: true
#     family:
#
#   # Font settings for Logo
#   # Fallback to `global` font settings.
#   # The `size` option use `px` as unit
#   logo:
#     external: true
#     family:
#     size:
#
#   # Font settings for <code> and code blocks.
#   codes:
#     external: true
#     family:

# ---------------------------------------------------------------
# Sidebar Settings
# ---------------------------------------------------------------


# Social Links
# Key is the link label showing to end users.
# Value is the target link (E.g. GitHub: https://github.com/iissnan)
SOCIAL = OrderedDict(
    sorted({
               "GitHub": {"label": u"GitHub", "link": "https://github.com/lzjun567", "social_icons": "github",
                          "position": 1},
               "Twitter": {"label": u"Twitter", "link": "https://twitter.com/lzjun1", "social_icons": "twitter",
                           "position": 2},
               "Weibo": {"label": u"微博", "link": "http://weibo.com/lzjun567 ", "social_icons": "weibo", "position": 3},
               "Zhihu": {"label": u"知乎", "link": "https://www.zhihu.com/people/zhijun-liu", "social_icons": "",
                         "position": 5},

           }.items(), key=lambda t: t[1]['position']))
#
# # Social Links Icons
# # Icon Mapping:
# #   Map a menu item to a specific FontAwesome icon name.
# #   Key is the name of the item and value is the name of FontAwsome icon. Key is case-senstive.
# #   When an globe mask icon presenting up means that the item has no mapping icon.
# social_icons:
#   enable: true
#   # Icon Mappings.
#   # KeyMapsToSocalItemKey: NameOfTheIconFromFontAwesome
#   GitHub: github
#   Twitter: twitter
#   Weibo: weibo
#
#
# # Sidebar Avatar
# # in theme directory(source/images): /images/avatar.jpg
# # in site  directory(source/uploads): /uploads/avatar.jpg
# #avatar:
#
#
# # Table Of Contents in the Sidebar
# toc:
#   enable: true
#
#   # Automatically add list number to toc.
#   number: true
#
#
# # Creative Commons 4.0 International License.
# # http://creativecommons.org/
# # Available: by | by-nc | by-nc-nd | by-nc-sa | by-nd | by-sa | zero
# #creative_commons: by-nc-sa
# #creative_commons:
#
#   # Sidebar Position, available value: left | right
#   position: left
#   #position: right
#
#   # Sidebar Display, available value:
#   #  - post    expand on posts automatically. Default.
#   #  - always  expand for all pages automatically
#   #  - hide    expand only when click on the sidebar toggle icon.
#   #  - remove  Totally remove sidebar including sidebar toggler.
#   display: post
#   #display: always
#   #display: hide
#   #display: remove
SIDEBAR = {
    "position": "left",
    "display": "post"
}
#
#
# # Blogrolls
# #links_title: Links
# #links_layout: block
# #links_layout: inline
# #links:
#   #Title: http://example.com/
#
#
# # ---------------------------------------------------------------
# # Misc Theme Settings
# # ---------------------------------------------------------------
#
# # Custom Logo.
# # !!Only available for Default Scheme currently.
# # Options:
# #   enabled: [true/false] - Replace with specific image
# #   image: url-of-image   - Images's url
# custom_logo:
#   enabled: false
#   image:
#
#
# # Code Highlight theme
# # Available value:
# #    normal | night | night eighties | night blue | night bright
# # https://github.com/chriskempson/tomorrow-theme
# highlight_theme: normal
#
#
# # Automatically scroll page to section which is under <!-- more --> mark.
# scroll_to_more: true
#
#
# # Automatically Excerpt. Not recommand.
# # Please use <!-- more --> in the post to control excerpt accurately.
# auto_excerpt:
#   enable: false
#   length: 150
#
#
# # Wechat Subscriber
# #wechat_subscriber:
#   #enabled: true
#   #qcode: /path/to/your/wechatqcode ex. /uploads/wechat-qcode.jpg
#   #description: ex. subscribe to my blog by scanning my public wechat account
#
#
#
#
# # ---------------------------------------------------------------
# # Third Party Services Settings
# # ---------------------------------------------------------------
#
# # MathJax Support
# mathjax:
#   enable: false
#   cdn: //cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML
#
#
# # Swiftype Search API Key
# #swiftype_key:
#
# # Baidu Analytics ID
# #baidu_analytics:
#
# # Duoshuo ShortName
DUOSHUO_SHORTNAME = "foofish"
#
# # Disqus
# #disqus_shortname:
#
# # Baidu Share
# # Available value:
# #    button | slide
# #baidushare:
# ##  type: button
#
# # Share
# #jiathis:
# #add_this_id:
#
# # Share
# #duoshuo_share: true
#
# # Google Webmaster tools verification setting
# # See: https://www.google.com/webmasters/
GOOGLE_SITE_VERIFICATION = "your google site verification"
#
#
# # Google Analytics
GOOGLE_ANALYTICS = "you google analytics id"
#
# # CNZZ count
# #cnzz_siteid:
#
#
# # Make duoshuo show UA
# # user_id must NOT be null when admin_enable is true!
# # you can visit http://dev.duoshuo.com get duoshuo user id.
# duoshuo_info:
#   ua_enable: true
#   admin_enable: false
#   user_id: 0
#   #admin_nickname: Author
#
#
# # Facebook SDK Support.
# # https://github.com/iissnan/hexo-theme-next/pull/410
# facebook_sdk:
#   enable: false
#   app_id:       #<app_id>
#   fb_admin:     #<user_id>
#   like_button:  #true
#   webmaster:    #true
#
# # Facebook comments plugin
# # This plugin depends on Facebook SDK.
# # If facebook_sdk.enable is false, Facebook comments plugin is unavailable.
# facebook_comments_plugin:
#   enable: false
#   num_of_posts: 10
#
#
# # Show number of visitors to each article.
# # You can visit https://leancloud.cn get AppID and AppKey.
# leancloud_visitors:
#   enable: false
#   app_id: #<app_id>
#   app_key: #<app_key>
#
# # Show PV/UV of the website/page with busuanzi.
# # Get more information on http://ibruce.info/2015/04/04/busuanzi/
# busuanzi_count:
#   # count values only if the other configs are false
#   enable: false
#   # custom uv span for the whole site
#   site_uv: true
#   site_uv_header: <i class="fa fa-user"></i>
#   site_uv_footer:
#   # custom pv span for the whole site
#   site_pv: true
#   site_pv_header: <i class="fa fa-eye"></i>
#   site_pv_footer:
#   # custom pv span for one page only
#   page_pv: true
#   page_pv_header: <i class="fa fa-file-o"></i>
#   page_pv_footer:
#
# # Tencent analytics ID
# # tencent_analytics:
#
# # Enable baidu push so that the blog will push the url to baidu automatically which is very helpful for SEO
# baidu_push: false
#
#
#
# #! ---------------------------------------------------------------
# #! DO NOT EDIT THE FOLLOWING SETTINGS
# #! UNLESS YOU KNOW WHAT YOU ARE DOING
# #! ---------------------------------------------------------------
#
# # Motion
USE_MOTION = True
#
# # Fancybox
FANCYBOX = True
#
#
# # Script Vendors.
# # Set a CDN address for the vendor you want to customize.
# # For example
# #    jquery: https://ajax.googleapis.com/ajax/libs/jquery/2.2.0/jquery.min.js
# # Be aware that you should use the same version as internal ones to avoid potential problems.
# vendors:
#   # Internal path prefix. Please do not edit it.
#   _internal: vendors
#
#   # Internal version: 2.1.3
#   jquery:
#
#   # Internal version: 2.1.5
#   # http://fancyapps.com/fancybox/
FANCYBOX = True
#   fancybox_css:
#
#   # Internal version: 1.0.6
#   # https://github.com/ftlabs/fastclick
#   fastclick:
#
#   # Internal version: 1.9.7
#   # https://github.com/tuupola/jquery_lazyload
#   lazyload:
#
#   # Internal version: 1.2.1
#   # http://VelocityJS.org
#   velocity:
#
#   # Internal version: 1.2.1
#   # http://VelocityJS.org
#   velocity_ui:
#
#   # Internal version: 0.7.9
#   # https://faisalman.github.io/ua-parser-js/
#   ua_parser:
#
#   # Internal version: 4.4.0
#   # http://fontawesome.io/
#   fontawesome:
#
#
# # Assets
# css: css
# js: js
# images: images
#
# # Theme version
VERSION = '5.0.1'

ALIPAY = ""
WECHATPAY = ""
