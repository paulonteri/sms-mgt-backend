from backend.settings.common import *
import json
from environs import Env

env = Env()

# from dotenv import load_dotenv
# env_path = f'{BASE_DIR}/.env'
# load_dotenv(dotenv_path=env_path)

SECRET_KEY = get_env_variable('SECRET_KEY')

DEBUG = env.bool('DEBUG')

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_env_variable("DB_NAME"),
        'USER': get_env_variable("DB_USER"),
        'PASSWORD': get_env_variable("DB_PASSWORD"),
        'HOST': get_env_variable("DB_HOST"),
        'PORT': get_env_variable("DB_PORT"),
        # TODO enable this when moving to self hosted db
        # 'CONN_MAX_AGE': 20,
    }
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES':
        ('knox.auth.TokenAuthentication',),
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated'
    ]
}

# Africa's talking
AFRICASTALKING_USERNAME = get_env_variable("AFRICASTALKING_USERNAME")
AFRICASTALKING_API_KEY = get_env_variable("AFRICASTALKING_API_KEY")

CORS_ORIGIN_ALLOW_ALL = True
