# -*- coding: utf-8 -*-
import pytest
from fixture.data_generators import *
from model.contact import Contact


testdata = [
    Contact(lastname=random_name(6), firstname=random_name(12), address=random_string(10),
            email=random_email(6, "bor.com"), email2=random_email(7, "@test"),
            email3=random_email(10, "@kom.biz"), homephone=random_phone("+381", 7),
            mobilephone=random_phone("+7(952)", 8), workphone=random_phone("+7-981", 4),
            fax=random_phone("9-1-2", 8))
    for i in range(3)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
