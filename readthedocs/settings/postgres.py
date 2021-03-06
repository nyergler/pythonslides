import os
from .base import *  # noqa


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pyslides',
        'USER': 'deployer',  # Not used with sqlite3.
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '',
    }
}

DEBUG = os.environ.get('DEBUG', False)
TEMPLATE_DEBUG = DEBUG
CELERY_ALWAYS_EAGER = not DEBUG

MEDIA_URL = '/media/'
STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = MEDIA_URL + 'admin/'
SESSION_ENGINE = "django.contrib.sessions.backends.cached_db"

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
        'URL': 'http://odin:8983/solr',
    }
}

CACHES = {
    'default': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': 'localhost:6379',
        'PREFIX': 'docs',
        'OPTIONS': {
            'DB': 1,
            'PARSER_CLASS': 'redis.connection.HiredisParser'
        },
    },
}

# Elasticsearch settings.
ES_HOSTS = ['backup:9200', 'db:9200']
ES_DEFAULT_NUM_REPLICAS = 1
ES_DEFAULT_NUM_SHARDS = 5

SLUMBER_API_HOST = 'https://readthedocs.org'
WEBSOCKET_HOST = 'websocket.readthedocs.org:8088'

PRODUCTION_DOMAIN = 'readthedocs.org'
USE_SUBDOMAIN = True
NGINX_X_ACCEL_REDIRECT = True

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTOCOL", "https")

REDIS = {
    'host': 'localhost',
    'port': 6379,
    'db': 0,
}

try:
    from local_settings import *  # noqa
except:
    pass
