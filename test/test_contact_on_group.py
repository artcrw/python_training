import random
from fixture.contact import Contact
from fixture.group import Group
from fixture.orm import ORMFixture


def test_add_contact_to_group(app):

    orm = ORMFixture(host="127.0.0.1", database="addressbook", user="root", password="", port=3307)

    if len(orm.get_group_list()) == 0:
        app.group.creation(Group(name="create_group_for_edd"))
    if len(orm.get_contact_list()) == 0:
        app.contact.creation(Contact(firstname="create_contact_for_edd"))
    groups_orm = orm.get_group_list()
    rand_gr = random.choice(groups_orm)
    contacts_not_in_group_list = orm.get_contacts_not_in_group(rand_gr)
    if len(contacts_not_in_group_list) == 0:
        app.contact.creation(Contact(firstname="create_contact_for_edd"))
        contacts_not_in_group_list = orm.get_contacts_not_in_group(rand_gr)
    rand_cont = random.choice(contacts_not_in_group_list)
    app.contact.add_contact_to_group_by_id(rand_cont.id, rand_gr.id)
    assert rand_cont in orm.get_contacts_in_group(rand_gr)
    assert rand_cont not in orm.get_contacts_not_in_group(rand_gr)


def test_del_con_from_group(app):

    orm = ORMFixture(host="127.0.0.1", database="addressbook", user="root", password="", port=3307)

    if len(orm.get_group_list()) == 0:
        app.group.creation(Group(name="create_group_for_edd"))
    if len(orm.get_contact_list()) == 0:
        app.contact.creation(Contact(firstname="create_contact_for_edd"))
    groups_orm = orm.get_group_list()
    rand_gr = random.choice(groups_orm)
    rand_cont = random.choice(orm.get_contacts_not_in_group(rand_gr))
    if len(orm.get_contacts_in_group(rand_gr)) == 0:
        app.contact.add_contact_to_group_by_id(rand_cont.id, rand_gr.id)
        assert rand_cont in orm.get_contacts_in_group(rand_gr)
    rand_cont_for_del = random.choice(orm.get_contacts_in_group(rand_gr))
    app.contact.delete_contact_from_group_by_id(rand_cont_for_del.id, rand_gr.id)
    assert rand_cont_for_del not in orm.get_contacts_in_group(rand_gr)
    assert rand_cont_for_del in orm.get_contacts_not_in_group(rand_gr)