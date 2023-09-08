from model.contact import Contact
from random import randrange


def test_mod_first_contact(app):
    if app.contact.count() == 0:
        app.contact.creation(Contact(firstname="create_for_mod"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="first", middlename="middle", lastname="last", mobilephone="999999999")
    contact.id = old_contacts[index].id
    app.contact.mod_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
