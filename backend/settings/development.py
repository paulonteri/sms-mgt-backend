from backend.settings.common import *
from dotenv import load_dotenv

env_path = f'{BASE_DIR}/.env'

load_dotenv(dotenv_path=env_path)

# Africa's talking
AFRICASTALKING_USERNAME = get_env_variable("AFRICASTALKING_USERNAME")
AFRICASTALKING_API_KEY = get_env_variable("AFRICASTALKING_API_KEY")

CORS_ORIGIN_ALLOW_ALL = True