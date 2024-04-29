"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 5.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
import os
import secrets
from pathlib import Path
import dj_database_url
import django_heroku

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-xf8$jfcv(pp25u0$%k)sisg2+2dh$*urd8w_p_ekch5y(@3#xs",

# Determine the environment from the DJANGO_ENV environment variable
env = os.environ.get('DJANGO_ENV', 'dev')

IS_HEROKU_APP = "DYNO" in os.environ and not "CI" in os.environ

# SECURITY WARNING: don't run with debug turned on in production!
if not IS_HEROKU_APP:
    DEBUG = True

if IS_HEROKU_APP:
    from ecdgt_be.config_prod import Config
    ALLOWED_HOSTS = ["*"]
    CORS_ALLOWED_ORIGINS = [
        "http://ec-dgt.web.app",
        "https://ec-dgt.web.app",
    ]
else:
    from ecdgt_be.config_dev import Config
    ALLOWED_HOSTS = ['localhost', '127.0.0.1', "*"]
    CORS_ALLOWED_ORIGINS = [
        "http://localhost:3000",
        "https://localhost:3000",
    ]

API_URL = Config.API_URL


# Application definition

INSTALLED_APPS = [
    "whitenoise.runserver_nostatic",

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'backend',
    "rest_framework",
    "django_filters",
    "api"
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ecdgt_be.urls'

# Static files (CSS, JavaScript, images)
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'frontend', 'build', 'static'),
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates', 'frontend', 'build')],
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

WSGI_APPLICATION = 'ecdgt_be.wsgi.application'


if IS_HEROKU_APP:
    # In production on Heroku the database configuration is derived from the `DATABASE_URL`
    # environment variable by the dj-database-url package. `DATABASE_URL` will be set
    # automatically by Heroku when a database addon is attached to your Heroku app. See:
    # https://devcenter.heroku.com/articles/provisioning-heroku-postgres
    # https://github.com/jazzband/dj-database-url
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'db84t9c5vlfhks',
            'USER': 'hrcspgucoaaufd',
            'PASSWORD': 'f7955cb89479046157d35e42684c37e0fe75b141da14fd2fc653e65509eb9274',
            'HOST': 'ec2-3-232-218-211.compute-1.amazonaws.com',
            'PORT': '5432',
        }
    }
# DATABASES = {
#     "default": dj_database_url.config(
#         conn_max_age=600,
#         conn_health_checks=True,
#         ssl_require=True,
#     ),
# }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "ecdgt_be/db.sqlite3",
        }
    }

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

django_heroku.settings(locals())

# STORAGES = {
#     # Enable WhiteNoise's GZip and Brotli compression of static assets:
#     # https://whitenoise.readthedocs.io/en/latest/django.html#add-compression-and-caching-support
#     "staticfiles": {
#         "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
#     },
# }

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

WHITENOISE_KEEP_ONLY_HASHED_FILES = False

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'novadiscsscorecards@gmail.com'  # Your Gmail address
# Eventually eastcoastdiscgolftour@gmail.com but need a password
EMAIL_HOST_PASSWORD = 'cjbktyfzkqbffuct'     # Your Gmail password or app password
