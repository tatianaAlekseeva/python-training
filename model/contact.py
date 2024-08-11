from sys import maxsize


class Contact:

    def __init__(self, lastname=None, firstname=None, email=None, email2=None, email3=None,
                 contact_id=None, address=None, homephone=None, mobilephone=None, workphone=None,
                 fax=None, all_phones_from_home_page=None, all_emails_from_home_page=None):
        self.firstname = firstname
        self.lastname = lastname
        self.address = address
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.contact_id = contact_id
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.fax = fax
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page

    def __repr__(self):
        return (f"{self.contact_id}: {self.lastname} {self.firstname} {self.address} "
                f"{self.all_phones_from_home_page} {self.all_emails_from_home_page}")

    def __eq__(self, other):
        return ((self.contact_id is None or other.contact_id is None or self.contact_id == other.contact_id)
                and self.lastname == other.lastname and self.firstname == other.firstname
                and self.address == other.address
                and (self.all_phones_from_home_page is None or other.all_phones_from_home_page is None or
                     self.all_phones_from_home_page == other.all_phones_from_home_page)
                and (self.all_emails_from_home_page is None or other.all_emails_from_home_page is None or
                     self.all_emails_from_home_page == other.all_emails_from_home_page))

    def id_or_max(self):
        if self.contact_id:
            return int(self.contact_id)
        else:
            return maxsize
