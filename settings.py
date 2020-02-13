import os
from sc4py.env import env
URL_PATH_PREFIX = env("URL_PATH_PREFIX", "sead/acesso/")
os.environ.setdefault("URL_PATH_PREFIX", env("", "sead/acesso/"))
os.environ.setdefault("MY_APPS", "acesso")
os.environ.setdefault("POSTGRES_DB", env("POSTGRES_DB_ACESSO"))

os.environ.setdefault("DJANGO_AUTH_USER_MODEL", "acesso.User")
os.environ.setdefault("DJANGO_LOGIN_URL", env("DJANGO_LOGIN_URL", '/%slogin/' % URL_PATH_PREFIX))
os.environ.setdefault("DJANGO_LOGOUT_URL", env("DJANGO_LOGOUT_URL", '/%slogout/' % URL_PATH_PREFIX))
os.environ.setdefault("DJANGO_LOGIN_REDIRECT_URL", env("DJANGO_LOGIN_REDIRECT_URL", '/%s' % URL_PATH_PREFIX))
os.environ.setdefault("DJANGO_LOGOUT_REDIRECT_URL", env("DJANGO_LOGOUT_REDIRECT_URL", '/%s' % URL_PATH_PREFIX))

from suap_ead.template_settings import *

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

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {'console': {'class': 'logging.StreamHandler'}, },
    'loggers': {
        '': {'handlers': ['console'], 'level': 'DEBUG'},
        'parso': {'handlers': ['console'], 'level': 'INFO'},
    },
}
