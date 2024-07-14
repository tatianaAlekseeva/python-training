# -*- coding: utf-8 -*-
from model.group import Group


def test_modify_group_name(app):
    app.group.modify_first(Group(name="New Group"))


def test_modify_group_header(app):
    app.group.modify_first(Group(header="New header"))
