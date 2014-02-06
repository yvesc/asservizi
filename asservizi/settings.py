"""
Django settings for asservizi project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


#seti ID site
SITE_ID = 1 


ADMINS = (
    ('Orizio Pierangelo', 'pierangelo1982@gmail.com'),
)

MANAGERS = (
    ('Orizio Pierangelo', 'pierangelo1982@gmail.com'),
)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'i^*(4@ts^cxbb&(#7cx#2z5_pp!&=w7*l23gq*9n&pji(m@d4+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


#TEMPLATE CONTEXT


TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.contrib.messages.context_processors.messages",
    'django.core.context_processors.request',

    )


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'contact_form',
    #'commenti_form',
    'tinymce',
    'easy_thumbnails',
    'image_cropping', 
    'sito',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'asservizi.urls'

WSGI_APPLICATION = 'asservizi.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.mysql',
        'NAME': 'asservizi',
        'USER': 'asservizi',
        'PASSWORD': 'montecarmelo',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'it-IT'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

STATIC_URL = '/static/'

MEDIA_ROOT = '/var/www/vhosts/vps42667.ovh.net/asservizi.it/asservizi/asservizi/media/'

MEDIA_URL = "http://www.asservizi.it/media/"



########### EMAIL CONF ################
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'pierangelo1982@gmail.com'
EMAIL_HOST_PASSWORD = 'mediolanum'
DEFAULT_FROM_EMAIL = 'pierangelo1982@gmail.com'

MYPATH = "http://localhost/"



############# TINYMCE ################
#TINYMCE_JS_URL = os.path.join(MEDIA_ROOT, "path/to/tiny_mce/tiny_mce.js")
#TINYMCE_JS_ROOT = os.path.join(MEDIA_ROOT, "path/to/tiny_mce")
TINYMCE_DEFAULT_CONFIG = {
    'plugins': "table,spellchecker,paste,searchreplace",
    'theme': "advanced",
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 10,
}
TINYMCE_SPELLCHECKER = True
##TINYMCE_COMPRESSOR = True

########## Fine TinyMCE #######################