def fill_contact_fields(contact, wd):
    # edit contact form
    wd.find_element("name", "firstname").click()
    wd.find_element("name", "firstname").clear()
    wd.find_element("name", "firstname").send_keys(contact.firstname)
    wd.find_element("name", "lastname").click()
    wd.find_element("name", "lastname").clear()
    wd.find_element("name", "lastname").send_keys(contact.lastname)
    wd.find_element("name", "email").click()
    wd.find_element("name", "email").clear()
    wd.find_element("name", "email").send_keys(contact.email)


def select_first_contact(wd):
    wd.find_element("name", "selected[]").click()


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_contacts_page(self):
        wd = self.app.wd
        wd.get("http://localhost/addressbook/")
        # wd.find_element("link text", "home page").click()

    def create(self, contact):
        wd = self.app.wd
        # init contact creation
        wd.find_element("link text", "add new").click()
        # fill contact form
        fill_contact_fields(contact, wd)
        # submit contact creation
        wd.find_element("name", "submit").click()
        self.open_contacts_page()

    def delete_first_contact(self):
        self.open_contacts_page()
        wd = self.app.wd
        select_first_contact(wd)
        # submit deletion
        wd.find_element("xpath", "//input[@value='Delete']").click()
        wd.find_element("id", "maintable")

    def modify_first(self, contact):
        self.open_contacts_page()
        wd = self.app.wd
        select_first_contact(wd)
        wd.find_element("xpath", "//img[@alt='Edit']").click()
        fill_contact_fields(contact, wd)
        # submit contact update
        wd.find_element("name", "update").click()
        self.open_contacts_page()
