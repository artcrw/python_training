# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.creation(Contact(firstname="name", middlename="name2", lastname="name3", mobile="98394838498"))


def test_add_empty_contact(app):
    app.contact.creation(Contact(firstname="", middlename="", lastname="", mobile=""))
