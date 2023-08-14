import pytest
from group import Group
from application import Application


@pytest.fixture()
def app(request):
    fixture = Application
    request.addfinalizer(fixture.destroy)
    return fixture


 def test_add_group(app):
    app.login("admin", "secret")
    app.init_group_creation()
    app.fill_group_form(Group("r23", "e32r", "r45"))
    app.submit_group_creation()
    app.logout()


def test_add_empty_group(app):
    app.login("admin", "secret")
    app.init_group_creation()
    app.fill_group_form(Group("", "", ""))
    app.submit_group_creation()
    app.logout()
