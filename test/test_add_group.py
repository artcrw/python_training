import pytest
from model.group import Group
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.creation()
    app.group.fill_form(Group(name="r23", header="e32r", footer="r45"))
    app.group.submit_creation()
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.creation()
    app.group.fill_form(Group(name="", header="", footer=""))
    app.group.submit_creation()
    app.session.logout()
