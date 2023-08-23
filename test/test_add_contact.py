# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.init_contact_creation()
    app.contact.fill_contact_form(Contact(firstname="name", middlename="name2", lastname="name3", mobile="98394838498"))
    app.contact.submit_contact_creation()


def test_add_empty_contact(app):
    app.contact.init_contact_creation()
    app.contact.fill_contact_form(Contact(firstname="", middlename="", lastname="", mobile=""))
    app.contact.submit_contact_creation()
