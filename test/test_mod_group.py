from model.group import Group


def test_mod_first_group(app):
    app.group.mod_first_group(Group(name="new", header="new2", footer="new3"))