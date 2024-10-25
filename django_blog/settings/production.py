from os import environ

# SITE SETTINGS
DEBUG = True
ALLOWED_HOSTS = []
SECRET_KEY = environ['SECRET_KEY']

# SMTP
EMAIL_HOST = environ['EMAIL_HOST']
EMAIL_USE_TLS = environ['EMAIL_USE_TLS']
EMAIL_USE_SSL = environ['EMAIL_USE_SSL']
EMAIL_PORT = environ['EMAIL_PORT']
EMAIL_HOST_USER = environ['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = environ['EMAIL_HOST_PASSWORD']

# POSTGRES
POSTGRES_DB = environ['POSTGRES_DB']
POSTGRES_USER = environ['POSTGRES_USER']
POSTGRES_PASSWORD = environ['POSTGRES_PASSWORD']
POSTGRES_HOST = environ['POSTGRES_HOST']
POSTGRES_PORT = environ['POSTGRES_PORT']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': POSTGRES_DB,
        'USER': POSTGRES_USER,
        'PASSWORD': POSTGRES_PASSWORD,
        'HOST': POSTGRES_HOST,
        'PORT': POSTGRES_PORT,
    }
}

INTERNAL_IPS = environ['INTERNAL_IPS']

# RECAPTCHA
RECAPTCHA_PUBLIC_KEY = environ['RECAPTCHA_PUBLIC_KEY']
RECAPTCHA_PRIVATE_KEY = environ['RECAPTCHA_PRIVATE_KEY']
RECAPTCHA_DEFAULT_ACTION = 'generic'
RECAPTCHA_SCORE_THRESHOLD = 0.5

# CELERY
CELERY_BROKER_URL = environ['CELERY_BROKER_URL']
CELERY_BROKER_TRANSPORT_OPTIONS = environ['CELERY_BROKER_TRANSPORT_OPTIONS']
CELERY_RESULT_BACKEND = environ['CELERY_RESULT_BACKEND']
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASKS_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'



