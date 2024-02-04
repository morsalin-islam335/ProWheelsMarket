from pathlib import Path

import environ
env = environ.Env()



environ.Env.read_env()


SECRET_KEY = env('SECRET_KEY') # eta read kora assign korba
DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': env("DB_NAME"), 
       'USER': env("DB_USER"),
       'PASSWORD': env("DB_PASSWORD"),
       'HOST': env("DB_HOST"),
       'PORT': env("DB_PORT"),
   }
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER  = env("Email") #sender's email-id
EMAIL_HOST_PASSWORD = env("Email_Password") #password associated with above email-id




BASE_DIR = Path(__file__).resolve().parent.parent



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
    'user',
    'car',
    'company',
    'crispy_forms',
    'crispy_bootstrap5',

]

CRISPY_ALLOWED_TEMPLATES_PACKS = 'bootstrap5'
CRISPY_TEMPLATE_PACK = 'bootstrap5'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ProWheelsMarket.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'ProWheelsMarket.wsgi.application'

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


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Dhaka'

USE_I18N = True

USE_TZ = True



STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR/'static'
]



MEDIA_URL = '/media/'
# MEDIA_ROOT = BASE_DIR/'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


