# -*- coding: utf-8 -*-
from model.group import Group


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="For test"))
    app.group.modify_first(Group(name="New Group"))


def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="For test"))
    app.group.modify_first(Group(header="New header"))
