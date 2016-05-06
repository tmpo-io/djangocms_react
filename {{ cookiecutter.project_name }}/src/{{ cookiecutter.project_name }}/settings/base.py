# -*- coding: utf-8 -*-

import os
from .. import config

gettext = lambda s: s

DATA_DIR = os.path.dirname(
    os.path.dirname(os.path.dirname(__file__))
)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = DATA_DIR

SECRET_KEY = config.env('SECRET_KEY',
                'l!rc@u)-xwv9@sl6gcjo*oa4r0z63@0pbbl)-il#=_s8=apd@$')

DEBUG = True
ALLOWED_HOSTS = ['*']

ADMINS = [
    ('Jordi', 'j@tmpo.io',),
    ('Oriol', 'o@tmpo.io',)
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config.env('DB_NAME', '{{ cookiecutter.project_name }}'),
        'USER': config.env('DB_USER', 'tempo'),
        'PASSWORD': config.env('DB_PASSWORD', ''),
        'HOST': config.env('DB_HOST', 'mysql'),
        'PORT': '',
        'OPTIONS': {
            "init_command": "SET foreign_key_checks = 0;",
        }
    }
}

EMAIL_HOST = config.env("EMAIL_HOST", "smtp.mailgun.org")
EMAIL_PORT = 25
EMAIL_HOST_USER = config.env('EMAIL_HOST_USER', 'postmaster@dev.tmpo.io')
EMAIL_HOST_PASSWORD = config.env('EMAIL_HOST_PASSWORD', '')


# Application definition
ROOT_URLCONF = '{{ cookiecutter.project_name }}.urls'
WSGI_APPLICATION = '{{ cookiecutter.project_name }}.wsgi.application'

LANGUAGE_CODE = '{{ cookiecutter.languages.strip().split(',')[0] }}'
TIME_ZONE = 'Europe/Madrid'
USE_I18N = True
USE_L10N = True
USE_TZ = False


STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(DATA_DIR, 'media')
STATIC_ROOT = os.path.join(DATA_DIR, 'static')

LOCALE_PATHS = (
    os.path.join(DATA_DIR, 'conf/locale'),
)
ROSETTA_MESSAGES_SOURCE_LANGUAGE_CODE = '{{ cookiecutter.languages.strip().split(',')[0] }}'

STATICFILES_DIRS = (
    os.path.join(DATA_DIR, 'assets'),

)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

SITE_ID = 1

MIDDLEWARE_CLASSES = (
    'opbeat.contrib.django.middleware.OpbeatAPMMiddleware',
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
)


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            # os.path.join(DATA_DIR, 'transtic', 'templates')
            # PROJECT_DIR.child('templates')
            os.path.join(BASE_DIR, 'templates'),
        ],
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                'cms.context_processors.cms_settings',
                'sekizai.context_processors.sekizai',
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
                'django.template.loaders.eggs.Loader',
            ],
            'debug': True,
        },
    },
]


COMPRESS_ENABLED = None

INSTALLED_APPS = (
    'django_extensions',
    'djangocms_admin_style',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'compressor',
    'cms',
    'menus',
    'sekizai',
    'treebeard',
    'djangocms_style',
    'djangocms_text_ckeditor',
    'djangocms_column',
    'djangocms_googlemap',
    'djangocms_inherit',
    'djangocms_teaser',
    'easy_thumbnails',
    'filer',
    'cmsplugin_filer_file',
    'cmsplugin_filer_folder',
    'cmsplugin_filer_link',
    'cmsplugin_filer_image',
    'cmsplugin_filer_teaser',
    'cmsplugin_filer_video',
    'reversion',
    'rosetta',
    'opbeat.contrib.django',
    '{{ cookiecutter.project_name }}',
    '{{ cookiecutter.project_name }}cms',
)

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)

MIGRATION_MODULES = {
    'cmsplugin_filer_file': 'cmsplugin_filer_file.migrations_django',
    'cmsplugin_filer_folder': 'cmsplugin_filer_folder.migrations_django',
    'cmsplugin_filer_link': 'cmsplugin_filer_link.migrations_django',
    'cmsplugin_filer_image': 'cmsplugin_filer_image.migrations_django',
    'cmsplugin_filer_teaser': 'cmsplugin_filer_teaser.migrations_django',
    'cmsplugin_filer_video': 'cmsplugin_filer_video.migrations_django',
}

LANGUAGES = (
    {% for language in cookiecutter.languages.strip().split(',') -%}
    ('{{ language|trim }}', gettext('{{ language|trim }}')),
    {% endfor %}
)

CMS_LANGUAGES = {
    # Customize this
    'default': {
        'public': True,
        'hide_untranslated': False,
        'redirect_on_fallback': True,
    },
    1: [
        {% for language in cookiecutter.languages.strip().split(',') -%}
        {
            'public': True,
            'code': '{{ language|trim }}',
            'hide_untranslated': False,
            'name': gettext('{{ language|trim }}'),
            'redirect_on_fallback': True,
        },
        {% endfor %}
    ],
}

CMS_CACHE_DURATION = 60


CMS_TEMPLATES = (
    # Customize this
    ('home.html', 'Home'),
)

CMS_PERMISSION = True

CMS_PLACEHOLDER_CONF = {
}

OPBEAT = {
    'ORGANIZATION_ID': '',
    'APP_ID': '',
    'SECRET_TOKEN': '',
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
