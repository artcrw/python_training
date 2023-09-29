from model.contact import Contact
import random


def test_mod_come_contact(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.creation(Contact(firstname="create_for_mod"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    contact.firstname = Contact(firstname="first").firstname
    app.contact.mod_contact_by_id(contact)
    assert len(old_contacts) == len(db.get_contact_list())
    new_contacts = db.get_contact_list()
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
