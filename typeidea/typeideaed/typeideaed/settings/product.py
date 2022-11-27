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

ADMINS = MANAGERS = (
    ('the5fire', 'thefivefire@gmail.com'),  # 你的邮件地址
)

# EMAIL_HOST = ''
# EMAIL_HOST_USER = 'the5fire'
# EMAIL_HOST_PASSWORD = ''
# EMAIL_SUBJECT_PREFIX = ''
# DEFAULT_FROM_EMAIL = ''
# SERVER_EMAIL = ''

STATIC_ROOT = '/home/the5fire/venvs/typeidea-env/static_files/'

# REDIS_URL = '127.0.0.1:6379:1'
#
# CACHES = {
#     'default': {
#         'BACKEND': 'django_redis.cache.RedisCache',
#         'LOCATION': REDIS_URL,
#         'TIMEOUT': 300,
#         'OPTIONS': {
#             # 'PASSWORD': '<对应密码>',
#             'CLIENT_CLASS': 'django_redis.client.DefaultClient',
#             'PARSER_CLASS': 'redis.connection.HiredisParser',
#         },
#         'CONNECTION_POOL_CLASS': 'redis.connection.BlockingConnectionPool',
#     }
# }

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '%(levelname)s %(asctime)s %(module)s:'
                      '%(funcName)s:%(lineno)d %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'default',
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'typeidea.log',
            'formatter': 'default',
            'maxBytes': 1024 * 1024,  # 1M
            'backupCount': 5,
        },

    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
    }
}