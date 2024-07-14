# -*- coding: utf-8 -*-
from model.group import Group


def test_modify_group_name(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first(Group(name="New Group", header="New header", footer="New footer"))
    app.session.logout()
