# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group.creation(Group(name="r23", header="e32r", footer="r45"))


def test_add_empty_group(app):
    app.group.creation(Group(name="", header="", footer=""))
