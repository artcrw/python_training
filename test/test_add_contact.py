# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.group.init_contact_creation()
    app.group.fill_contect_form(Contact(firstname="name", middlename="name2", lastname="name3", mobile="98394838498"))
    app.group.submit_contact_creation()
    app.session.logout()


def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.group.init_contact_creation()
    app.group.fill_contect_form(Contact(firstname="", middlename="", lastname="", mobile=""))
    app.group.submit_contact_creation()
    app.session.logout()
