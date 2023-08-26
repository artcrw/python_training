from model.contact import Contact


def test_delete_first_contract(app):
    if app.contact.count() == 0:
        app.contact.creation(Contact(firstname="name_del"))
    app.contact.delete_first_contract()
