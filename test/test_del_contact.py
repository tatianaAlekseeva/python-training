# -*- coding: utf-8 -*-
from random import randrange
from model.contact import Contact


def test_delete_any_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact("Maria", "Test", "test@bor.com"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts
