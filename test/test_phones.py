import re
from model.contact import Contact


def test_phones_on_home_page(app):
    if app.contact.count() == 0:
        app.contact.creation(Contact(firstname="firstname", lastname="lastname", id="id", homephone="homephone",
                                     mobilephone="mobilephone", workphone="workphone", secondaryphone="secondaryphone",
                                     address="address", email="email", email2="email2", email3="email3"))
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)


def test_phones_on_contact_view_page(app):
    if app.contact.count() == 0:
        app.contact.creation(Contact(firstname="firstname", lastname="lastname", id="id", homephone="homephone",
                                     mobilephone="mobilephone", workphone="workphone", secondaryphone="secondaryphone",
                                     address="address", email="email", email2="email2", email3="email3"))
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.homephone == contact_from_edit_page.homephone
    assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone
    assert contact_from_view_page.workphone == contact_from_edit_page.workphone
    assert contact_from_view_page.secondaryphone == contact_from_edit_page.secondaryphone


def test_all_info_on_home_page(app, db):
    if app.contact.count() == 0:
        app.contact.creation(Contact(firstname="firstname", lastname="lastname", id="id", homephone="homephone",
                                     mobilephone="mobilephone", workphone="workphone", secondaryphone="secondaryphone",
                                     address="address", email="email", email2="email2", email3="email3"))
    contacts_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    contacts_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    for i in range(len(contacts_from_db)):
        assert contacts_from_home_page[i].lastname.replace(" ", "") == contacts_from_db[i].lastname.replace(" ", "")
        assert contacts_from_home_page[i].firstname.replace(" ", "") == contacts_from_db[i].firstname.replace(" ", "")
        assert contacts_from_home_page[i].all_emails_from_home_page == merge_emails_like_on_home_page(contacts_from_db[i])
        assert contacts_from_home_page[i].all_phones_from_home_page == merge_phones_like_on_home_page(contacts_from_db[i])


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone,
                                        contact.workphone, contact.secondaryphone]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None,
                                   [contact.email, contact.email2, contact.email3])))
