from contacts.models import Contact


def get_all_contacts_numbers():
    # return list of all contacts' phone numbers
    return Contact.objects.all().values_list("phone_number", flat=True)


def return_contact_numbers_with_tag(tags):
    """
    :return: the phone numbsers of contacts witha certain tag
    """
    # verify data
    if not (len(tags) > 0):
        raise Exception("Tags cannot be blank")
    if not isinstance(tags, list):
        raise Exception("Incorrect data type, the Tags value should be a list")
    for q in tags:
        if not (isinstance(q, int)):
            raise Exception("Incorrect data type, the individual tags should be integers")

    # get contact numbers
    phone_nos = []
    for tag in tags:
        try:
            phone_nos.extend(Contact.objects.filter(contacttag=tag).values_list("phone_number", flat=True))
        except:
            pass

    if not (len(phone_nos) > 0):
        raise Exception("No contacts Found")
    else:
        return phone_nos


def get_contact_number(contact):
    # get a single contacts phone number
    try:
        cont = [Contact.objects.get(pk=contact).phone_number, ]
        return cont
    except:
        raise Exception("Contact does not exist")
