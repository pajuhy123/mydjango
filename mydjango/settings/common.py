"""
Django settings for mydjango project.

Generated by 'django-admin startproject' using Django 1.11.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
from os.path import abspath, dirname, join

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
#"/Users/joon/mydjango/manage.py"
#"/Users/joon/mydjango/mydjango/settings.py  기존 경로
#BASE_DIR = dirname(dirname(abspath(__file__))) 기존경로에 따른 설정
#"/Users/joon/mydjango/mydjango/settings/common.py  바뀐 경로
BASE_DIR = dirname(dirname(dirname(abspath(__file__))))  #바뀐 경로에 따른 설정, 1파일의 깊이 만큼


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@jb8wzd_lp@wjwn0@vw5!*vay*op+eoq7qni(2p)1s6xi)65vt'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*'] #서비스할 도메인만 입력하는 것이 좋다.


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'el_pagination',
    'raven.contrib.django.raven_compat',
    'imagekit',
    'bootstrap3',
    
    'django_extensions',
    'accounts', 
    'blog',
    'dojo',
    'shop',

]

MIDDLEWARE = [
    
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mydjango.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [  os.path.join(BASE_DIR, 'mydjango', 'templates'),   ], #프로젝트 template 경로 설정
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'blog.context_processor.blog',
            ],
        },
    },
]

WSGI_APPLICATION = 'mydjango.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
#프로젝트(제일 상위)에서 css 파일 경로 설정
STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'mydjango', 'static'),
]
#배포를 위한 설정 ,, 배포시 이곳에 1개의 파일이라도 들어있어야 한다. 빈 디렉토리면, git은 관리 하지 않는다.
STATIC_ROOT =  os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media') #실서비스시 추천 os.path.join(BASE_DIR,'..', 'media') 



NAVER_CLIENT_ID = 'zlf18uHwXtdpWfKfZwAP'  # 이 값은 개별 ID

import raven
#ref #SentryDashboard
# FIXME: 현 프로젝트 ROOT 지정 
GIT_ROOT = BASE_DIR
if os.path.exists(os.path.join(GIT_ROOT, '.git')):
    release = raven.fetch_git_sha(GIT_ROOT) # 현재 최근 커밋해시 획득
else:
    release = 'dev'

RAVEN_CONFIG = {
'release': release,
# FIXME: 각자 설정에 맞춰 수정 - https://docs.sentry.io/clients/python/integrations/django/
 'dsn': 'https://ccf7f9b746e942f5a2a5646c57c349ef:f4fb8e5cb2014ba089d9c31a55b64610@sentry.io/208691',
}
