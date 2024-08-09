# -*- coding: utf-8 -*-
import random
from model.contact import Contact


def test_modify_contact(app, db, check_ui, data_contacts):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact("Test", "Maria", "test@bor.com"))
    old_contacts = db.get_contact_list()
    modified_contact = random.choice(old_contacts)
    index = find_index_by_contact_id(old_contacts, modified_contact.contact_id)
    contact = data_contacts
    contact.contact_id = modified_contact.contact_id
    app.contact.modify_contact_by_id(contact, contact.contact_id)
    old_contacts[index] = contact
    new_contacts = db.get_contact_list()
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


def find_index_by_contact_id(contacts, target_id):
    for index, contact in enumerate(contacts):
        if contact.contact_id == target_id:
            return index
    return None
