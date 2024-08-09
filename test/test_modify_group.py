# -*- coding: utf-8 -*-
from model.group import Group
import random


def test_modify_any_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="For test"))
    old_groups = db.get_group_list()
    modified_group = random.choice(old_groups)
    index = find_index_by_group_id(old_groups, modified_group.group_id)
    group = Group(name="New Group " + str(random.randrange(100)))
    group.group_id = modified_group.group_id
    app.group.modify_group_by_id(group, group.group_id)
    new_groups = db.get_group_list()
    old_groups[index] = group
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


def find_index_by_group_id(groups, target_id):
    for index, group in enumerate(groups):
        if group.group_id == target_id:
            return index
    return None


"""
def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="For test"))
    old_groups = app.group.get_group_list()
    app.group.modify_first(Group(header="New header"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
"""
