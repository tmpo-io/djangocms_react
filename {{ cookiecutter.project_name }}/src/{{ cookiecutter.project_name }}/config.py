# -*- coding: utf-8 -*-
# http://tmpo.io

"""
Utils to work with environment values.
If environment is not defined or default value used, logs a
error / info message.

Load secrets variables, from volumes/files as kubernetts secrets
storage

"""

import os

import logging
logger = logging.getLogger('configs')

def env(var_name, default=None):
    v = os.getenv(var_name, None)
    if not v:
        if not default:
            logger.error(
                "%s not declared in environment. Using ''",
                var_name
            )
            return ''
        logger.info(
            "%s not declared in environment. Using default",
            var_name
        )
        return default
    return v


def env_asbool(var_name, default=None):
    value = env(var_name, default)
    if str(value).lower().strip() in ['true', 't', '1', 'yes']:
        return True
    if str(value).lower().strip() in ['false', 'f', '0', 'no', 'none']:
        return False
    return False


def env_asint(var_name, default=None):
    value = env(var_name, default)
    return int(value)


def get_secret(path_file, cast=None, default=''):
    if not os.path.isfile(path_file):
        logger.info(
            "%s not found using ''", path_file
        )
        return default
    file = open(path_file, 'r')
    value = file.read().strip()
    if cast:
        return cast(value)
    return value


