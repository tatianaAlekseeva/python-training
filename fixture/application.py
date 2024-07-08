from selenium.webdriver.firefox.webdriver import WebDriver

from fixture.session import SessionHelper


class Application:
    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)

    def return_to_groups_page(self):
        wd = self.wd
        wd.find_element("link text", "group page").click()

    def create_group(self, group):
        wd = self.wd
        self.open_groups_page()
        # init group creation
        wd.find_element("name", "new").click()
        # fill group form
        wd.find_element("name", "group_name").click()
        wd.find_element("name", "group_name").clear()
        wd.find_element("name", "group_name").send_keys(group.name)
        wd.find_element("name", "group_header").click()
        wd.find_element("name", "group_header").clear()
        wd.find_element("name", "group_header").send_keys(group.header)
        wd.find_element("name", "group_footer").click()
        wd.find_element("name", "group_footer").clear()
        wd.find_element("name", "group_footer").send_keys(group.footer)
        # submit group creation
        wd.find_element("name", "submit").click()
        self.return_to_groups_page()

    def open_groups_page(self):
        wd = self.wd
        wd.find_element("link text", "groups").click()

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/index.php")

    def return_to_contacts_page(self):
        wd = self.wd
        wd.find_element("link text", "home page").click()

    def create_contact(self, contact):
        wd = self.wd
        # init contact creation
        wd.find_element("link text", "add new").click()
        # fill group form
        wd.find_element("name", "firstname").click()
        wd.find_element("name", "firstname").clear()
        wd.find_element("name", "firstname").send_keys(contact.firstname)
        wd.find_element("name", "lastname").click()
        wd.find_element("name", "lastname").clear()
        wd.find_element("name", "lastname").send_keys(contact.lastname)
        wd.find_element("name", "email").click()
        wd.find_element("name", "email").clear()
        wd.find_element("name", "email").send_keys(contact.email)
        # submit contact creation
        wd.find_element("name", "submit").click()
        self.return_to_contacts_page()

    def destroy(self):
        self.wd.quit()
