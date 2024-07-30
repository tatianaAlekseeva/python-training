# -*- coding: utf-8 -*-
import pytest
from fixture.data_generators import random_string_with_prefix
from model.group import Group


testdata = [
    Group(name=name, header=header, footer=footer)
    for name in ["", random_string_with_prefix("name", 10)]
    for header in ["", random_string_with_prefix("header", 15)]
    for footer in ["", random_string_with_prefix("footer", 15)]
]


@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, group):
    old_groups = app.group.get_group_list()
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
