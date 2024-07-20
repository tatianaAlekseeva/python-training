from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_contacts_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/index.php") and len(wd.find_elements("id", "maintable")) > 0):
            wd.get("http://localhost/addressbook/")

    def create(self, contact):
        wd = self.app.wd
        self.open_contacts_page()
        # init contact creation
        wd.find_element("link text", "add new").click()
        # fill contact form
        self.fill_contact_fields(contact)
        # submit contact creation
        wd.find_element("name", "submit").click()
        self.open_contacts_page()

    def delete_first_contact(self):
        self.open_contacts_page()
        wd = self.app.wd
        self.select_first_contact()
        # submit deletion
        wd.find_element("xpath", "//input[@value='Delete']").click()
        wd.find_element("id", "maintable")

    def modify_first(self, contact):
        self.open_contacts_page()
        wd = self.app.wd
        self.select_first_contact()
        wd.find_element("xpath", "//img[@alt='Edit']").click()
        self.fill_contact_fields(contact)
        # submit contact update
        wd.find_element("name", "update").click()
        self.open_contacts_page()

    def fill_contact_fields(self, contact):
        wd = self.app.wd
        wd.find_element("name", "firstname").click()
        wd.find_element("name", "firstname").clear()
        wd.find_element("name", "firstname").send_keys(contact.firstname)
        wd.find_element("name", "lastname").click()
        wd.find_element("name", "lastname").clear()
        wd.find_element("name", "lastname").send_keys(contact.lastname)
        wd.find_element("name", "email").click()
        wd.find_element("name", "email").clear()
        wd.find_element("name", "email").send_keys(contact.email)

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element("name", "selected[]").click()

    def count(self):
        wd = self.app.wd
        self.open_contacts_page()
        return len(wd.find_elements("name", "selected[]"))

    def get_contact_list(self):
        wd = self.app.wd
        self.open_contacts_page()
        contacts_list = []
        for element in wd.find_elements("name", "entry"):
            initial_string = element.find_element("name", "selected[]").get_attribute("title")
            start = initial_string.find('(') + 1
            end = initial_string.find(')')
            full_name = initial_string[start:end]
            first_name, last_name = full_name.split()
            contact_id = element.find_element("name", "selected[]").get_attribute("value")
            contacts_list.append(Contact(lastname=last_name, firstname=first_name, contact_id=contact_id))
        return contacts_list
