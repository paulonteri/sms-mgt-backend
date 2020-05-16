from contacts.models import Contact


def get_all_contacts_numbers():
    # return list of all contacts' phone numbers
    return Contact.objects.all().values_list("phone_number", flat=True)
