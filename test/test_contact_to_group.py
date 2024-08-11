import random
from model.contact import Contact
from model.group import Group


def test_add_contact_to_group(app, db, orm):
    if len(db.get_group_list()) == 0:
        add_group(app)
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact("Test", "Maria", "test@bor.com"))
    group = random_non_empty_unique_group(app, db)
    contact = random.choice(db.get_contact_list())
    app.contact.add_contact_to_group(contact, group)
    contacts_in_group = orm.get_contacts_in_group(group)
    assert contact in contacts_in_group


def test_del_contact_from_group(app, db, orm):
    if len(db.get_group_list()) == 0:
        add_group(app)
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact("Test", "Maria", "test@bor.com"))
    if len(db.get_link_list()) == 0:
        group = random_non_empty_unique_group(app, db)
        contact = random.choice(db.get_contact_list())
        app.contact.add_contact_to_group(contact, group)
    link = db.get_link_list()[0]
    contacts = db.get_contact_list()
    contact = next(contact for contact in contacts if contact.contact_id == link.contact_id)
    groups = db.get_group_list()
    group = next(group for group in groups if group.group_id == link.group_id)
    app.contact.del_contact_from_group(contact, group)
    contacts_not_in_group = orm.get_contacts_not_in_group(group)
    assert contact in contacts_not_in_group


def add_group(app):
    app.group.create(Group(name="For test"))


def random_non_empty_unique_group(app, db):
    groups = db.get_group_list()

    non_empty_groups = [group for group in groups if group.name]

    seen_names = set()
    unique_non_empty_groups = []
    for group in non_empty_groups:
        if group.name not in seen_names:
            unique_non_empty_groups.append(group)
            seen_names.add(group.name)

    if unique_non_empty_groups:
        return random.choice(unique_non_empty_groups)
    else:
        add_group(app)
        groups = db.get_group_list()
        non_empty_groups = [group for group in groups if group.name]
        unique_non_empty_groups = []
        for group in non_empty_groups:
            if group.name not in seen_names:
                unique_non_empty_groups.append(group)
                seen_names.add(group.name)
        if unique_non_empty_groups:
            return random.choice(unique_non_empty_groups)
        else:
            add_group(app)
