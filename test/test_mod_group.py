from model.group import Group


def test_mod_first_group(app):
    if app.group.count() == 0:
        app.group.creation(Group(name="create_for_mod"))
    app.group.mod_first_group(Group(name="new", header="new2", footer="new3"))
