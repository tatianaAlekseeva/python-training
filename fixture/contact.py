class ContactHelper:

    def __init__(self, app):
        self.app = app

    def return_to_contacts_page(self):
        wd = self.app.wd
        wd.find_element("link text", "home page").click()

    def create(self, contact):
        wd = self.app.wd
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