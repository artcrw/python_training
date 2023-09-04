from model.contact import Contact


def test_mod_first_contact(app):
    if app.contact.count() == 0:
        app.contact.creation(Contact(firstname="create_for_mod"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="first", middlename="middle", lastname="last", mobile="999999999")
    app.contact.mod_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
