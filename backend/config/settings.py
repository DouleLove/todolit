import pathlib

import gnvext

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent

SECRET_KEY = gnvext.StringEnvVariable(
    name='DJANGO_SECRET_KEY',
    default='',
).value

DEBUG = gnvext.BooleanEnvVariable(
    name='DJANGO_DEBUG',
    default=True,
).value

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres',
    'rest_framework',
    'corsheaders',
    'users',
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

CORS_ALLOWED_ORIGINS = gnvext.CollectionEnvVariable(
    name="CORS_ALLOWED_ORIGINS",
    default=[],
).value

ROOT_URLCONF = 'config.urls'

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

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': gnvext.StringEnvVariable(
            name='DATABASE_ENGINE',
            default=RuntimeError('db engine is not specified in .env'),
        ).value,
        'NAME': gnvext.StringEnvVariable(
            name='DATABASE_NAME',
            default=RuntimeError('db name is not specified in .env'),
        ).value,
        'USER': gnvext.StringEnvVariable(
            name='DATABASE_USER',
            default=RuntimeError('db user is not specified in .env'),
        ).value,
        'PASSWORD': gnvext.StringEnvVariable(
            name='DATABASE_PASSWORD',
            default=RuntimeError('db user password is not specified in .env'),
        ).value,
        'HOST': gnvext.StringEnvVariable(
            name='DATABASE_HOST',
            default=RuntimeError('db host is not specified in .env'),
        ).value,
        'PORT': gnvext.StringEnvVariable(
            name='DATABASE_PORT',
            default=RuntimeError('db port is not specified in .env'),
        ).value,
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation'
                '.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation'
                '.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation'
                '.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation'
                '.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'users.User'

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'drfseriperm.renderers.BrowsableAPINoFieldsRenderer',
    ],
}
