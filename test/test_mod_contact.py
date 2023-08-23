from model.contact import Contact


def test_mod_first_contact(app):
    app.contact.mod_first_contact(Contact(firstname="first", middlename="middle", lastname="last", mobile="999999999"))
