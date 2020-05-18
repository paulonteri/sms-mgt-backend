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

    try:
        phone_nos.extend(Contact.objects.filter(contacttag__in=tags).values_list("phone_number", flat=True))
    except Exception as e:
        raise Exception(e)
    if not (len(phone_nos) > 0):
        raise Exception("No contacts Found")
    else:
        return phone_nos


def get_contact_number(contacts):
    # get a single contacts phone number
    # try:
    #     cont = [Contact.objects.get(pk=contact).phone_number, ]
    #     return cont
    # except:
    #     raise Exception("Contact does not exist")

    """
    :return: the phone numbsers of contacts witha certain tag
    """
    # verify data
    if not (len(contacts) > 0):
        raise Exception("Contacts cannot be blank")
    if not isinstance(contacts, list):
        raise Exception("Incorrect data type, the Contacts value should be a list")
    for q in contacts:
        if not (isinstance(q, int)):
            raise Exception("Incorrect data type, the individual contacts should be integers")

    # get contact numbers
    phone_nos = []
    try:
        phone_nos.extend(Contact.objects.filter(pk__in=contacts).values_list("phone_number", flat=True))
    except Exception as e:
        raise Exception(e)

    if not (len(phone_nos) > 0):
        raise Exception("No contacts Found")
    else:
        print(phone_nos)
        return phone_nos
