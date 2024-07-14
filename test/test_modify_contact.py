# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first(Contact("John", "Tweet", "word200002@bor.com"))
    app.session.logout()
