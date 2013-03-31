import os

DEBUG = True
TEMPLATE_DEBUG = True

DIRNAME = os.path.abspath(os.path.dirname(__file__))
STATIC_SERVE_ROOT = os.path.join(DIRNAME, 'media/')

SITE_HOST = '0.0.0.0:8000'
SITE_URL = 'http://0.0.0.0:8000/'

ROOT_URLCONF = 'urls'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'den.schigrov@gmail.com'
EMAIL_HOST_PASSWORD = 'vitamina'
EMAIL_PORT = 587
EMAIL_USE_TLS = True