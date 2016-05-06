# -*- coding: UTF-8 -*-
# http://tmpo.io


from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'localhost',
        'NAME': '{{ cookiecutter.project_name }}',
        'PASSWORD': '',
        'PORT': '',
        'USER': 'root',
        'OPTIONS': {
            "init_command": "SET foreign_key_checks = 0;",
        }
    }
}


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
