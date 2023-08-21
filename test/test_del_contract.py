def test_delete_first_contract(app):
    app.session.login(username="admin", password="secret")
    app.group.delete_first_contract()
    app.session.logout()
