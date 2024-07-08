# -*- coding: utf-8 -*-
from application import Application
from contact import Contact
import pytest


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact("Anna", "Green", "word22@bor.com"))
    app.logout()
