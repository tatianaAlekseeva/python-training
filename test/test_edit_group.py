# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first(Group(name="TestGroup22", header="test22", footer="test299"))
    app.session.logout()
