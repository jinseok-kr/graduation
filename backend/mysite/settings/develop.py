from .base import *

#SECRET_KEY = '6dwf-@4q5iv=ztd5p7jgb0%$nbp0&0_v6q+wi!8pz*9x3+@ql5'

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
