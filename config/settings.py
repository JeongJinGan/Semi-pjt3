"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 3.2.13.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
    "best11kdt-env.eba-m22kfyhv.ap-northeast-2.elasticbeanstalk.com",
]


# Application definition

INSTALLED_APPS = [
    "storages",  # 12/02 등록(이수경)
    "imagekit",  # 11/27 등록(이수경)
    "korea",  # 11/27 등록(이수경)
    "accounts",  # 11/27 등록(이수경)
    "sns",  # 12월5일(주세환)
    "django_bootstrap5",  # 11/27 등록(이수경)
    "django_cleanup.apps.CleanupConfig",  # 11/27 등록(이수경) - 글이 삭제되었을 때 로컬에 남은 이미지들도 삭제될 수 있게 처리
    "django_summernote",  # 11/28 등록(차화영)
    "mathfilters", # 12/06 등록 (간정진)
    "corsheaders",  # CORS 관련 추가
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.admin",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",  # CORS 관련 추가
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

CORS_ORIGIN_WHITELIST = ["http://127.0.0.1:8000", "http://localhost:8000"]
CORS_ALLOW_CREDENTIALS = True

SUMMERNOTE_CONFIG = {
    "summernote": {
        "width": "100%",
        "height": "480",
    }
}

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "ko-kr"

TIME_ZONE = "Asia/Seoul"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = "staticfiles"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]


# Media files (user uploaded files)

# MEDIA_URL = "/media/"
# MEDIA_ROOT = BASE_DIR / "images"


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# User Model
AUTH_USER_MODEL = "accounts.User"


# 기존 미디어 코드 주석처리 후, AWS S3 관련 코드 추가
# DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"

# AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
# AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
# AWS_STORAGE_BUCKET_NAME = os.getenv("AWS_STORAGE_BUCKET_NAME")

# AWS_REGION = "ap-northeast-2"
# AWS_S3_CUSTOM_DOMAIN = "%s.s3.%s.amazonaws.com" % (
#     AWS_STORAGE_BUCKET_NAME,
#     AWS_REGION,
# )


# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": "best11_rds",
#         "USER": "postgres",
#         "PASSWORD": "1q2w3e4r!",
#         "HOST": "best-11-kdt.cgyji6nar9u7.ap-northeast-2.rds.amazonaws.com",
#         "PORT": "5432",
#     }
# }

DEBUG = os.getenv("DEBUG") == "True"
# DEBUG = False

if DEBUG:
    MEDIA_URL = "/media/"
    MEDIA_ROOT = BASE_DIR / "images"
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

else:
    # DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
    DEFAULT_FILE_STORAGE = "config.storages.MediaStorage"

    AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
    AWS_STORAGE_BUCKET_NAME = os.getenv("AWS_STORAGE_BUCKET_NAME")

    AWS_REGION = "ap-northeast-2"
    AWS_S3_CUSTOM_DOMAIN = "%s.s3.%s.amazonaws.com" % (
        AWS_STORAGE_BUCKET_NAME,
        AWS_REGION,
    )
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.getenv("DATABASE_NAME"),  # .env 파일에 value 작성
            "USER": "postgres",
            "PASSWORD": os.getenv("DATABASE_PASSWORD"),  # .env 파일에 value 작성
            "HOST": os.getenv("DATABASE_HOST"),  # .env 파일에 value 작성
            "PORT": "5432",
        }
    }
