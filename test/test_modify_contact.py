# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact("Maria", "Test", "test@bor.com"))
    app.contact.modify_first(Contact("John", "Tweet", "word200002@bor.com"))
