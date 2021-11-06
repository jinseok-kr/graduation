import os

from .base import *


#SECRET_KEY = os.environ['SECRET_KEY']

STATIC_ROOT = BASE_DIR / 'static/'
STATICFILES_DIRS = []
DEBUG = False

# AWS Example
ALLOWED_HOSTS = ['52.79.75.94']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'newsbigdata_db',
        'USER': 'dbmasteruser',
        'PASSWORD': ';xP0?$*typbh)^|~)-;:X[Qe+HWdf_iJ',
        'HOST': 'ls-a4875428c9f9f192e67b1bb761477cd8f9b4475f.c1kek88oj7uy.ap-northeast-2.rds.amazonaws.com',
        'PORT': '5432',
        # 'OPTIONS': {
        #     'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        # },
    }
}
