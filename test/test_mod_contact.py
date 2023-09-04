from model.contact import Contact


def test_mod_first_contact(app):
    if app.contact.count() == 0:
        app.contact.creation(Contact(firstname="create_for_mod"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="first", middlename="middle", lastname="last", mobile="999999999")
    contact.id = old_contacts[0].id
    app.contact.mod_first_contact(contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
