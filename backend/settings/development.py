from backend.settings.common import *
from dotenv import load_dotenv

env_path = f'{BASE_DIR}/.env'

load_dotenv(dotenv_path=env_path)

SECRET_KEY = 'n7)kkdn%^rrz9*3@4u86l4y7($#fb!$-szsmkd%&n7(b9_3m@r'

DEBUG = False

ALLOWED_HOSTS = ["*", ]

# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
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
AFRICASTALKING_USERNAME = os.environ.setdefault('AFRICASTALKING_USERNAME', 'sandbox')
AFRICASTALKING_API_KEY = os.environ.setdefault('AFRICASTALKING_API_KEY', 'AFRICASTALKING_API_KEY')

CORS_ORIGIN_ALLOW_ALL = True
