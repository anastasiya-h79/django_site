"""
Django settings for drums project.

Generated by 'django-admin startproject' using Django 3.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...) папка, гед лежитпроект
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret! нужен, чтобы запустить проект и в идеале потом закрыть
SECRET_KEY = '7hpq$pe3u9u0)@8(+6v4kpw9&3fd9x@4&xr9i+8c97^5dg(07)'

# SECURITY WARNING: don't run with debug turned on in production! режим разработки. false - когда сайт уже работает
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'prodapp',
    'boxapp',
    'usersapp',
    'debug_toolbar',
    'rest_framework',
    'rest_framework.authtoken',
    'crispy_forms',
    #добавляем в самый низ:
    'django_cleanup.apps.CleanupConfig'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'vrhelmet.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'boxapp.context_processors.getting_basket_info',
            ],
        },
    },
]

WSGI_APPLICATION = 'vrhelmet.wsgi.application'


# Database - можно подключить базу данных
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'ru-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

MEDIA_URL = '/media/'   # по какому адресу джанго б. брать медиа

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')    # куда джанго б. грузить медиа

#письмо уходит в консоль
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

#письмо отправляется и хранится как файл - не сработало
# EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
# EMAIL_FILE_PATH = '/tmp/emails'

# Переопределить модели пользователя
AUTH_USER_MODEL = 'usersapp.SiteUser'

# Переходы
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
# Куда идти на логин (если нет прав, перенаправляет на страницу логина)
LOGIN_URL = 'users/login/'

###

CART_SESSION_ID = 'cart'

# django-debug-toolbar
INTERNAL_IPS = [
    # ...
    '127.0.0.1',
    # ...
]

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',

    ]
}
CRISPY_TEMPLATE_PACK = 'bootstrap4'