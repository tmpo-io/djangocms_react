# -*- coding: UTF-8 -*-
# http://tmpo.io


from .base import *

DEBUG = False

SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
