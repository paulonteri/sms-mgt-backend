from backend.settings.common import *

# from dotenv import load_dotenv
# env_path = f'{BASE_DIR}/.env'
# load_dotenv(dotenv_path=env_path)

SECRET_KEY = 'n7)kkdn%^rrz9*3@4u86l4y7($#fb!$-szsmkd%&n7(b9_3m@r'

DEBUG = get_env_variable("DEBUG")

ALLOWED_HOSTS = ["*", ]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_env_variable("DB_NAME"),
        'USER': get_env_variable("DB_USER"),
        'PASSWORD': get_env_variable("DB_PASSWORD"),
        'HOST': get_env_variable("DB_HOST"),
        'PORT': get_env_variable("DB_PORT"),
    }
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES':
        ('knox.auth.TokenAuthentication',),
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny'
    ]
}


# Africa's talking
AFRICASTALKING_USERNAME = get_env_variable("AFRICASTALKING_USERNAME")
AFRICASTALKING_API_KEY = get_env_variable("AFRICASTALKING_API_KEY")

CORS_ORIGIN_ALLOW_ALL = True
