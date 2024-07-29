# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(lastname="Matjevic", firstname="Edgar", address="Serbia, Nis, Konstantina 5",
                      email="word202@bor.com", email2="test44@test", email3="rest44@kom.biz",
                      homephone="+381-64-66", mobilephone="87656543", workphone="+7(981)110-77",
                      fax="5555666")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

