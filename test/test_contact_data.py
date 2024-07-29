import re
from random import randrange

from model.contact import Contact


def test_random_contact_data_on_home_page(app):
    if app.contact.count() == 0:
        add_contact_for_test(app)
    contacts_count = app.contact.get_contact_list()
    index = randrange(len(contacts_count))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)


def test_phones_on_contact_view_page(app):
    if app.contact.count() == 0:
        add_contact_for_test(app)
    contact_from_view_page = app.contact.get_contact_info_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.homephone == contact_from_edit_page.homephone
    assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone
    assert contact_from_view_page.workphone == contact_from_edit_page.workphone
    assert contact_from_view_page.fax == contact_from_edit_page.fax


def add_contact_for_test(app):
    app.contact.create(Contact("Test", "Anna", address="Neverland, Dreamcity",
                               email="test202@bor.com", email2="test44@test", email3="test44@kom.biz",
                               homephone="+3818765", mobilephone="8765657743", workphone="+7(812)110-77",
                               fax="9995666"))


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None, [contact.homephone, contact.mobilephone,
                                                                 contact.workphone]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None, [contact.email, contact.email2,
                                                                 contact.email3]))))
