# -*- coding: utf-8 -*-
from fixture.application import Application
from model.contact import Contact
import pytest


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact("Anna", "Green", "word22@bor.com"))
    app.session.logout()
