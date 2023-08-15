# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.contact_application import Capplication


@pytest.fixture
def app(request):
    fixture = Capplication()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.init_contact_creation()
    app.fill_contect_form(Contact(firstname="name", middlename="name2", lastname="name3", mobile="98394838498"))
    app.submit_contact_creation()
    app.logout()


def test_add_empty_contact(app):
    app.login(username="admin", password="secret")
    app.init_contact_creation()
    app.fill_contect_form(Contact(firstname="", middlename="", lastname="", mobile=""))
    app.submit_contact_creation()
    app.logout()
