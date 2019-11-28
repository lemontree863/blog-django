from .common import *

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'l6fz72#cf01twzjtgf=l^r9xar60t=rmdrp7ge_15t_^+&_&5('
SECRET_KEY = os.environ['DJANGO_SECRET_KEY']
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '116.62.160.157']
