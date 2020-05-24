from contacts.services.contacts import get_all_contacts_numbers, return_contact_numbers_with_tag, get_contact_number
from sms.services.africastalking_api import send_sms


def send_to_all_contacts(user, message):
    # send message to all contacts
    try:
        send_sms(user, message, get_all_contacts_numbers())
    except Exception as e:
        raise e


def send_to_tags(user, message, tags):
    # send message to specific tags
    try:
        send_sms(user, message, return_contact_numbers_with_tag(tags))
    except Exception as e:
        raise e


def send_to_contact(user, message, contact):
    # send message to specific contact
    try:
        send_sms(user, message, get_contact_number(contact))
    except Exception as e:
        raise e
