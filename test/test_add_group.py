# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group.creation()
    app.group.fill_form(Group(name="r23", header="e32r", footer="r45"))
    app.group.submit_creation()


def test_add_empty_group(app):
    app.group.creation()
    app.group.fill_form(Group(name="", header="", footer=""))
    app.group.submit_creation()
