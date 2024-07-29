# -*- coding: utf-8 -*-
from random import randrange
from model.contact import Contact


def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact("Test", "Maria", "test@bor.com"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact("Malyshev33", "Igor", "test00024@rest.biz")
    contact.contact_id = old_contacts[index].contact_id
    app.contact.modify_contact_by_index(contact, index)
    assert len(old_contacts) == app.contact.count()
    old_contacts[index] = contact
    new_contacts = app.contact.get_contact_list()
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
