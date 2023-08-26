from model.contact import Contact


def test_mod_first_contact(app):
    if app.contact.count() == 0:
        app.contact.creation(Contact(firstname="create_for_mod"))
    app.contact.mod_first_contact(Contact(firstname="first", middlename="middle", lastname="last", mobile="999999999"))
