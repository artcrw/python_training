from model.contact import Contact


def test_delete_first_contract(app):
    if app.contact.count() == 0:
        app.contact.creation(Contact(firstname="name_del"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first_contract()
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0:1] = []
    assert old_contacts == new_contacts
