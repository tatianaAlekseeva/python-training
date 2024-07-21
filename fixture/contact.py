from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
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
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        self.open_contacts_page()
        wd = self.app.wd
        self.wait_for_main_table()
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element("xpath", "//input[@value='Delete']").click()
        wd.find_element("id", "maintable")
        self.contact_cache = None

    def modify_first(self, contact):
        self.modify_contact_by_index(contact, 0)

    def modify_contact_by_index(self, contact, index):
        self.open_contacts_page()
        wd = self.app.wd
        self.wait_for_main_table()
        wd.find_elements("xpath", "//img[@alt='Edit']")[index].click()
        self.fill_contact_fields(contact)
        # submit contact update
        wd.find_element("name", "update").click()
        self.open_contacts_page()
        self.contact_cache = None

    def wait_for_main_table(self):
        wd = self.app.wd
        wait = WebDriverWait(wd, 2)
        wait.until(ec.presence_of_element_located(("id", "maintable")))

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
        self.select_contact_by_index(0)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements("name", "selected[]")[index].click()

    def count(self):
        wd = self.app.wd
        self.open_contacts_page()
        return len(wd.find_elements("name", "selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contacts_page()
            self.contact_cache = []
            for element in wd.find_elements("name", "entry"):
                initial_string = element.find_element("name", "selected[]").get_attribute("title")
                start = initial_string.find('(') + 1
                end = initial_string.find(')')
                full_name = initial_string[start:end]
                first_name, last_name = full_name.split()
                contact_id = element.find_element("name", "selected[]").get_attribute("value")
                self.contact_cache.append(Contact(lastname=last_name, firstname=first_name, contact_id=contact_id))
        return list(self.contact_cache)
