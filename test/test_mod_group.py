from model.group import Group
import random


def test_mod_come_group(app, db, check_ui):
    if app.group.count() == 0:
        app.group.creation(Group(name="create_for_mod"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    group.name = Group(name="name").name
    app.group.mod_group_by_id(group)
    assert len(old_groups) == len(db.get_group_list())
    new_groups = db.get_group_list()
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
