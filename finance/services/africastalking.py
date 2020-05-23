import africastalking
import requests

from django.conf import settings

# Initialize SDK
username = settings.AFRICASTALKING_USERNAME
apikey = settings.AFRICASTALKING_API_KEY
africastalking.initialize(username, apikey)
app = africastalking.Application


def get_balance():
    try:
        response = app.fetch_application_data()
        string_amount = response["UserData"]["balance"].replace('KES ', '')
        int_amount = float(string_amount)
        print(int_amount)
        return int_amount
    except requests.exceptions.ConnectionError:
        raise Exception("Network Connection Error")
    except requests.HTTPError:
        raise Exception("HTTP Network Error")
    except Exception as e:
        # save the sms info to the db
        raise e
