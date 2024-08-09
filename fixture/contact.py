from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from model.contact import Contact
import re


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_contacts_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/index.php") and len(wd.find_elements("id", "maintable")) > 0):
            wd.get(self.app.base_url)

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

    def delete_contact_by_id(self, contact_id):
        self.open_contacts_page()
        wd = self.app.wd
        self.wait_for_main_table()
        self.select_contact_by_id(contact_id)
        # submit deletion
        wd.find_element("xpath", "//input[@value='Delete']").click()
        wd.find_element("id", "maintable")
        self.contact_cache = None

    def modify_first(self, contact):
        self.modify_contact_by_index(contact, 0)

    def modify_contact_by_index(self, contact, index):
        wd = self.app.wd
        self.open_edit_form_by_index(index)
        self.fill_contact_fields(contact)
        # submit contact update
        wd.find_element("name", "update").click()
        self.open_contacts_page()
        self.contact_cache = None

    def modify_contact_by_id(self, contact, contact_id):
        wd = self.app.wd
        self.open_edit_form_by_id(contact_id)
        self.fill_contact_fields(contact)
        # submit contact update
        wd.find_element("name", "update").click()
        self.open_contacts_page()
        self.contact_cache = None

    def open_edit_form_by_index(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        self.wait_for_main_table()
        wd.find_elements("xpath", "//img[@alt='Edit']")[index].click()

    def open_edit_form_by_id(self, contact_id):
        wd = self.app.wd
        self.open_contacts_page()
        self.wait_for_main_table()
        css_selector = f'a[href="edit.php?id={contact_id}"]'
        wd.find_element("css selector", css_selector).click()

    def wait_for_main_table(self):
        wd = self.app.wd
        wait = WebDriverWait(wd, 2)
        wait.until(ec.presence_of_element_located(("id", "maintable")))

    def fill_contact_fields(self, contact):
        fields_mapping = {
            "firstname": "firstname",
            "lastname": "lastname",
            "address": "address",
            "email": "email",
            "email2": "email2",
            "email3": "email3",
            "homephone": "home",
            "mobilephone": "mobile",
            "workphone": "work",
            "fax": "fax"
        }

        for attr, field_name in fields_mapping.items():
            value = getattr(contact, attr, None)
            if value is not None:
                self.fill_field_by_name(field_name, value)

    def fill_field_by_name(self, name, data):
        wd = self.app.wd
        wd.find_element("name", name).click()
        wd.find_element("name", name).clear()
        wd.find_element("name", name).send_keys(data)

    def select_first_contact(self):
        self.select_contact_by_index(0)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements("name", "selected[]")[index].click()

    def select_contact_by_id(self, contact_id):
        wd = self.app.wd
        wd.find_element("css selector", "input[value='%s']" % contact_id).click()

    def count(self):
        wd = self.app.wd
        self.open_contacts_page()
        return len(wd.find_elements("name", "entry"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contacts_page()
            self.contact_cache = []
            for element in wd.find_elements("name", "entry"):
                cells = element.find_elements("tag name", "td")
                last_name = cells[1].text
                first_name = cells[2].text
                contact_id = element.find_element("name", "selected[]").get_attribute("value")
                address = cells[3].text
                all_emails = cells[4].text
                all_phones = cells[5].text
                self.contact_cache.append(Contact(lastname=last_name, firstname=first_name, contact_id=contact_id,
                                                  address=address, all_emails_from_home_page=all_emails,
                                                  all_phones_from_home_page=all_phones))
        return list(self.contact_cache)

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        wd.find_elements("css selector", 'img[title="Details"]')[index].click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_edit_form_by_index(index)
        contact_id = wd.find_element("name", "id").get_attribute("value")
        lastname = wd.find_element("name", "lastname").get_attribute("value")
        firstname = wd.find_element("name", "firstname").get_attribute("value")
        address = wd.find_element("name", "address").get_attribute("value")
        homephone = wd.find_element("name", "home").get_attribute("value")
        mobilephone = wd.find_element("name", "mobile").get_attribute("value")
        workphone = wd.find_element("name", "work").get_attribute("value")
        fax = wd.find_element("name", "fax").get_attribute("value")
        email = wd.find_element("name", "email").get_attribute("value")
        email2 = wd.find_element("name", "email2").get_attribute("value")
        email3 = wd.find_element("name", "email3").get_attribute("value")
        return Contact(contact_id=contact_id, lastname=lastname, firstname=firstname, address=address,
                       homephone=homephone, mobilephone=mobilephone, workphone=workphone, fax=fax,
                       email=email, email2=email2, email3=email3)

    def get_contact_info_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element("id", "content").text
        homephone = re.search("H: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        fax = re.search("F: (.*)", text).group(1)
        return Contact(homephone=homephone,
                       mobilephone=mobilephone, workphone=workphone, fax=fax)
