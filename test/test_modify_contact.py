# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_contact(app):
    app.contact.modify_first(Contact("John", "Tweet", "word200002@bor.com"))
