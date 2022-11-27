# @Time      : 2022/11/19  下午5:39
# @Author    : cooper
# @Email     : wuxinpy.@gmail.com
# @File      : develop.py
# @Software  : PyCharm

from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

INSTALLED_APPS += [
    # 'debug_toolbar',
    # 'pympler',
    # 'debug_toolbar_line_profiler',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

# INTERNAL_IPS = ['127.0.0.1']

# DEBUG_TOOLBAR_PANELS = [
#     # 'djdt_flamegraph.FlamegraphPanel',
#     'pympler.panels.MemoryPanel',
#     # 'debug_toolbar_line_profiler.panel.ProfilingPanel',
# ]

DEBUG_TOOLBAR_CONFIG = {
    'JQUERY_URL': 'https://cdn.bootcss.com/jquery/3.3.1/jquery.min.js'
}
