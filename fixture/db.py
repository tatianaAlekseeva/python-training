import pymysql.cursors

from model.contact import Contact
from model.group import Group
from model.link import Link
from utils import merge_phones_like_on_home_page, merge_emails_like_on_home_page


class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        group_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (group_id, name, header, footer) = row
                group_list.append(Group(group_id=str(group_id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return group_list

    def get_contact_list(self):
        contact_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address, home, mobile, work, fax, email, email2, "
                           "email3 from addressbook where deprecated is null")
            for row in cursor:
                (contact_id, firstname, lastname, address, homephone, mobilephone, workphone, fax, email, email2, email3) = row
                contact_list.append(Contact(contact_id=str(contact_id), lastname=lastname, firstname=firstname,
                                            address=address, homephone=homephone, mobilephone=mobilephone, workphone=workphone,
                                            fax=fax, email=email, email2=email2, email3=email3))
        finally:
            cursor.close()

        for contact in contact_list:
            phones = merge_phones_like_on_home_page(contact)
            emails = merge_emails_like_on_home_page(contact)
            contact.all_phones_from_home_page = phones
            contact.all_emails_from_home_page = emails

        return contact_list

    def get_link_list(self):
        link_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, group_id from address_in_groups")
            for row in cursor:
                (id, group_id) = row
                link_list.append(Link(contact_id=str(id), group_id=str(group_id)))
        finally:
            cursor.close()
        return link_list

    def destroy(self):
        self.connection.close()
