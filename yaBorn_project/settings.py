"""
Django settings for yaBorn_project project.

Generated by 'django-admin startproject' using Django 3.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path
from datetime import timedelta


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-$tioc%1hfy(mm!wh7&*x4h2jmdmpk7lf$x^!rczflk)9*05=d-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
# TODO: 感觉admin会进不去 先不关
# 关闭调试模式 django不再处理静态资源

# 允许所有的IP访问网络服务
ALLOWED_HOSTS = ['*']

# 指定需要收集的静态文件的位置
# 即前端打包文件所在位置
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "frontend/dist/"),
]

# 静态文件收集目录
STATIC_ROOT = os.path.join(BASE_DIR, 'collected_static')

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 注册app列表
    'rest_framework',
    'article',
    'article_category',
    'user_info',
    'media',
    'comment',
]

# 媒体资源文件储存位置
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# REST_FRAMEWORK配置
REST_FRAMEWORK = {
    # 分页功能
    'DEFAULT_PAGINATION_CLASS':
        'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 4,  # 设置每页文章数量
    # # JWT为默认认证机制
    # 安装库djangorestframework-simplejwt
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}

# JWT验证时间
SIMPLE_JWT = {
    # Token 有效期设置
    # TODO: 修改 ACCESS_TOKEN_LIFETIME
    #  则前端 Login.vie-script-methods-signin-then 处需要加上对应时长的毫秒
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=10),
    # 'ACCESS_TOKEN_LIFETIME': timedelta(seconds=6),
    'REFRESH_TOKEN_LIFETIME': timedelta(minutes=30),
    # ACCESS token 有效期短 refresh长
    # access过期后 用refresh刷新(判断为活跃用户)
    # refresh过期 重新登录
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'yaBorn_project.urls'

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

WSGI_APPLICATION = 'yaBorn_project.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
