import os

DIRNAME = os.path.abspath(os.path.dirname(__file__))

DEBUG = TEMPLATE_DEBUG = False

ADMINS = (
    ('Den Schigrov', 'den.schigrov@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'img',
        'USER': 'img',
    }
}

TIME_ZONE = 'America/Toronto'

LANGUAGE_CODE = 'en-us'

MEDIA_ROOT = os.path.join(DIRNAME, 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = DIRNAME + '/static'
STATIC_URL = '/static/'

ADMIN_MEDIA_PREFIX = '/static/admin/'

STATICFILES_DIRS = (
    DIRNAME + '/staticfiles',
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'tw425ehotwktw4io4209yot42142yjtlkegwknlqr3kl325gwrewklt24'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'annoying.middlewares.RedirectMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'content.context_processors.site_elements',
)

ROOT_URLCONF = 'img.urls'

TEMPLATE_DIRS = (
    DIRNAME + '/templates',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'content',
    'contact',
    'imagekit',
    'publicauth'
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
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

STATIC_SERVE_ROOT = None

try:
    from settings_local import *
except:
    pass

