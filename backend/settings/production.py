from backend.settings.common import *
SECRET_KEY = 'n7)kkdn%^rrz9*3@4u86l4y7($#fb!$-szsmkd%&n7(b9_3m@r'

DEBUG = True

ALLOWED_HOSTS = ["*", ]

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