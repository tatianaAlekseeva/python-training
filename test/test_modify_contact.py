# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact("Test", "Maria", "test@bor.com"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact("Smith", "Elena", "test24@rest.biz")
    contact.contact_id = old_contacts[0].contact_id
    app.contact.modify_first(contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.remove(old_contacts[0])
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
