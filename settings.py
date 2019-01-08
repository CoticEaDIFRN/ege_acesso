"""
The MIT License (MIT)

Copyright 2015 Umbrella Tech.
Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
import os
import json
from python_brfied.env import env, env_as_bool, env_as_list, env_as_list_of_maps, env_as_int, env_from_json


# BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SECRET_KEY = env('DJANGO_SECRET_KEY', 'changeme')
DEBUG = env_as_bool('DJANGO_DEBUG', True)
ALLOWED_HOSTS = env_as_list('DJANGO_ALLOWED_HOSTS', '*' if DEBUG else '')

# Apps
MY_APPS = env_as_list('MY_APPS', 'ege_acesso,ege_django_theme')
DEV_APPS = env_as_list('DEV_APPS', 'debug_toolbar,django_extensions' if DEBUG else '')
THIRD_APPS = env_as_list('THIRD_APPS', 'django_python3_ldap,rest_framework')
DJANGO_APPS = env_as_list('DJANGO_APPS', 'django.contrib.admin,'
                                         'django.contrib.auth,'
                                         'django.contrib.contenttypes,'
                                         'django.contrib.sessions,'
                                         'django.contrib.messages,'
                                         'django.contrib.staticfiles')
INSTALLED_APPS = MY_APPS + THIRD_APPS + DEV_APPS + DJANGO_APPS


MIDDLEWARE = env_as_list('MIDDLEWARE', 'django.middleware.security.SecurityMiddleware,'
                                       'django.contrib.sessions.middleware.SessionMiddleware,'
                                       'django.middleware.common.CommonMiddleware,'
                                       'django.middleware.csrf.CsrfViewMiddleware,'
                                       'django.contrib.auth.middleware.AuthenticationMiddleware,'
                                       'django.contrib.messages.middleware.MessageMiddleware,'
                                       'django.middleware.clickjacking.XFrameOptionsMiddleware')

if DEBUG:
    MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = env('DJANGO_WSGI_APPLICATION', 'wsgi.application')

DATABASES = {
    'default': {
        'ENGINE': env('POSTGRES_ENGINE', 'django.db.backends.postgresql_psycopg2'),
        'HOST': env('POSTGRES_HOST', 'localhost'),
        'PORT': env('POSTGRES_PORT', '5432'),
        'NAME': env('POSTGRES_DB_ACESSO', 'postgres'),
        'USER': env('POSTGRES_USER', 'postgres'),
        'PASSWORD': env('POSTGRES_PASSWORD', 'postgres'),
    }
}

# Localization
LANGUAGE_CODE = env('LANGUAGE_CODE', 'pt-br')
TIME_ZONE = env('TIME_ZONE', 'UTC')
USE_I18N = env_as_bool('DJANGO_USE_I18N', True)
USE_L10N = env_as_bool('DJANGO_USE_L10N', True)
USE_TZ = env_as_bool('DJANGO_USE_TZ', True)

# Devepment
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {'console': {'class': 'logging.StreamHandler'}, },
    'loggers': {
        '': {'handlers': ['console'], 'level': 'DEBUG'},
    },
}
DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': lambda request: 'localhost' in request.get_host() or '127.0.0.1' in request.get_host() or 'sso' in request.get_host(),
}

# CORS_ORIGIN_ALLOW_ALL = True

# URL and routers
URL_PATH_PREFIX = env('URL_PATH_PREFIX', 'ege/acesso/')
STATIC_URL = "/%s%s" % (URL_PATH_PREFIX, env('DJANGO_STATIC_URL', 'ege/acesso/static/'))
STATIC_ROOT = "/statics/acesso"
ROOT_URLCONF = env('DJANGO_ROOT_URLCONF', 'urls')

# Session
SESSION_CACHE_ALIAS = env('DJANGO_SESSION_CACHE_ALIAS', 'default')
SESSION_COOKIE_AGE = env_as_int('DJANGO_SESSION_COOKIE_AGE', 1209600)
SESSION_COOKIE_DOMAIN = env('DJANGO_SESSION_COOKIE_DOMAIN', None)
SESSION_COOKIE_HTTPONLY = env_as_bool('DJANGO_SESSION_COOKIE_HTTPONLY', True)
SESSION_COOKIE_NAME = env('DJANGO_SESSION_COOKIE_NAME', 'egessosessionid')
SESSION_COOKIE_PATH = env('DJANGO_SESSION_COOKIE_PATH', '/%s' % URL_PATH_PREFIX)
SESSION_COOKIE_SAMESITE = env('DJANGO_SESSION_COOKIE_SAMESITE', 'Strict')
SESSION_COOKIE_SECURE = env_as_bool('DJANGO_SESSION_COOKIE_SECURE', False)

# REST Framework
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.BrowsableAPIRenderer',
        'rest_framework.renderers.JSONRenderer',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'ege_acesso.authentication.ApplicationSecretAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
    ],
    # 'DEFAULT_FILTER_BACKENDS': 'cnes.apiutils.APIFilterBackend',
}


# Auth
LOGIN_URL = '/%slogin/' % URL_PATH_PREFIX
LOGOUT_URL = '/%slogout/' % URL_PATH_PREFIX
LOGIN_REDIRECT_URL = '/%sperfil' % URL_PATH_PREFIX
LOGOUT_REDIRECT_URL = '/%s../perfil' % URL_PATH_PREFIX
AUTHENTICATION_BACKENDS = env_as_list('DJANGO_AUTHENTICATION_BACKENDS', 'django_python3_ldap.auth.LDAPBackend')
AUTH_PASSWORD_VALIDATORS = env_as_list_of_maps('DJANGO_UTH_PASSWORD_VALIDATORS', 'NAME', '')
AUTH_USER_MODEL = env("DJANGO_AUTH_USER_MODEL", 'ege_acesso.User')


# LDAP
USE_LDAP = LDAP_AUTH_URL=env('LDAP_AUTH_URL', None) is not None
LDAP_AUTH_URL = env('LDAP_AUTH_URL')
LDAP_AUTH_USE_TLS = env_as_bool('LDAP_AUTH_USE_TLS')
LDAP_AUTH_SEARCH_BASE = env('LDAP_AUTH_SEARCH_BASE', None)
LDAP_AUTH_OBJECT_CLASS = env('LDAP_AUTH_OBJECT_CLASS', 'user')
LDAP_AUTH_USER_FIELDS = env_from_json('LDAP_AUTH_USER_FIELDS', None, True)
LDAP_AUTH_USER_LOOKUP_FIELDS = env_as_list('LDAP_AUTH_USER_LOOKUP_FIELDS', 'username')
LDAP_AUTH_CLEAN_USER_DATA = env('LDAP_AUTH_CLEAN_USER_DATA')
LDAP_AUTH_SYNC_USER_RELATIONS = env('LDAP_AUTH_SYNC_USER_RELATIONS')
LDAP_AUTH_FORMAT_SEARCH_FILTERS = env('LDAP_AUTH_FORMAT_SEARCH_FILTERS')
LDAP_AUTH_FORMAT_USERNAME = env('LDAP_AUTH_FORMAT_USERNAME',
                                'django_python3_ldap.utils.format_username_active_directory')
LDAP_AUTH_ACTIVE_DIRECTORY_DOMAIN = env('LDAP_AUTH_ACTIVE_DIRECTORY_DOMAIN')
LDAP_AUTH_CONNECT_TIMEOUT = env_as_int('LDAP_AUTH_CONNECT_TIMEOUT', 10)
LDAP_AUTH_RECEIVE_TIMEOUT = env_as_int('LDAP_AUTH_RECEIVE_TIMEOUT', 10)
