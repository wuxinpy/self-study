# @Time      : 2022/11/27  上午10:14
# @Author    : cooper
# @Email     : wuxinpy.@gmail.com
# @File      : product.py
# @Software  : PyCharm


from .base import *

DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blogdb',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#         'LOCATION': [
#             '172.19.26.240.11211',
#             '172.19.26.242.11211',
#         ]
#     }
# }