from .common import *  # pylint: disable=unused-wildcard-import

ALLOWED_HOSTS = [
    '127.0.0.1', '*'
] + SECRETS.get('allowed_hosts', [])

DEBUG = False

STATIC_URL = 'http://djangoquickstart.test/static/'
MEDIA_URL = 'http://djangoquickstart.test/media/'
