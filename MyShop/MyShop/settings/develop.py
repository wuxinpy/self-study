# @Time      : 2022/11/28  下午9:57
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

