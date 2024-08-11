from model.contact import Contact
from model.group import Group
from pony.orm import Database, Optional, Set, PrimaryKey, db_session, select
from datetime import datetime

from utils import merge_phones_like_on_home_page, merge_emails_like_on_home_page


class ORMFixture:
    db = Database()

    class ORMGroup(db.Entity):
        _table_ = 'group_list'
        id = PrimaryKey(int, column='group_id')
        name = Optional(str, column='group_name')
        header = Optional(str, column='group_header')
        footer = Optional(str, column='group_footer')
        contacts = Set(lambda: ORMFixture.ORMContact, table='address_in_groups', column='id', reverse='groups',
                       lazy=True)

    class ORMContact(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int, column='id')
        firstname = Optional(str, column='firstname')
        lastname = Optional(str, column='lastname')
        address = Optional(str, column='address')
        home = Optional(str, column='home')
        mobile = Optional(str, column='mobile')
        work = Optional(str, column='work')
        fax = Optional(str, column='fax')
        email = Optional(str, column='email')
        email2 = Optional(str, column='email2')
        email3 = Optional(str, column='email3')
        deprecated = Optional(datetime, column='deprecated')
        groups = Set(lambda: ORMFixture.ORMGroup, table='address_in_groups', column='group_id', reverse='contacts',
                     lazy=True)

    def __init__(self, host, name, user, password):
        self.db.bind('mysql', host=host, database=name, user=user, password=password)
        self.db.generate_mapping(create_tables=True)

    @db_session
    def get_group_list(self):
        return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup)[:])

    def convert_groups_to_model(self, groups):
        def convert(group):
            return Group(group_id=str(group.id), name=group.name, header=group.header, footer=group.footer)

        return list(map(convert, groups))

    @db_session
    def get_contact_list(self):
        return self.convert_contacts_to_model(select(c for c in ORMFixture.ORMContact if c.deprecated is None)[:])

    def convert_contacts_to_model(self, contacts):
        def convert(contact):
            return Contact(contact_id=str(contact.id), lastname=contact.lastname, firstname=contact.firstname,
                           address=contact.address, homephone=contact.home, mobilephone=contact.mobile,
                           workphone=contact.work, fax=contact.fax, email=contact.email, email2=contact.email2,
                           email3=contact.email3)
        contact_list = list(map(convert, contacts))

        for contact in contact_list:
            phones = merge_phones_like_on_home_page(contact)
            emails = merge_emails_like_on_home_page(contact)
            contact.all_phones_from_home_page = phones
            contact.all_emails_from_home_page = emails

        return contact_list

    @db_session
    def get_contacts_in_group(self, group):
        orm_group = select(g for g in ORMFixture.ORMGroup if g.id == group.group_id).first()
        if orm_group:
            return self.convert_contacts_to_model(orm_group.contacts)
        return []

    @db_session
    def get_contacts_not_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.group_id))[0]
        return self.convert_contacts_to_model(
            select(c for c in ORMFixture.ORMContact if c.deprecated is None and orm_group not in c.groups))
