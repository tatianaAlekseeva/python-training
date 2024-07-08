class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element("name", "user").click()
        wd.find_element("name", "user").clear()
        wd.find_element("name", "user").send_keys(username)
        wd.find_element("id", "LoginForm").click()
        wd.find_element("name", "pass").click()
        wd.find_element("name", "pass").clear()
        wd.find_element("name", "pass").send_keys(password)
        wd.find_element("css selector", "input[type=\"submit\"]").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element("link text", "Logout").click()
