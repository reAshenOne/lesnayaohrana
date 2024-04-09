from .base import *

DEBUG = False

SECRET_KEY = "django-insecure-dd@-hd)#m%0n5eaz1=+y@%+w-)sb4vrw188m!2*p!)^2%9acza"

ALLOWED_HOSTS = ['89.111.172.120', 'localhost', 'www.lesnayaohrana.ru']

try:
    from .local import *
except ImportError:
    pass
