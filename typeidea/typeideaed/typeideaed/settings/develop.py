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