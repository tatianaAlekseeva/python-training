def fill_group_fields(group, wd):
    wd.find_element("name", "group_name").click()
    wd.find_element("name", "group_name").clear()
    wd.find_element("name", "group_name").send_keys(group.name)
    wd.find_element("name", "group_header").click()
    wd.find_element("name", "group_header").clear()
    wd.find_element("name", "group_header").send_keys(group.header)
    wd.find_element("name", "group_footer").click()
    wd.find_element("name", "group_footer").clear()
    wd.find_element("name", "group_footer").send_keys(group.footer)


def select_first_group(wd):
    # select first group
    wd.find_element("name", "selected[]").click()


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element("link text", "group page").click()

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # init group creation
        wd.find_element("name", "new").click()
        # fill group form
        fill_group_fields(group, wd)
        # submit group creation
        wd.find_element("name", "submit").click()
        self.return_to_groups_page()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        select_first_group(wd)
        # submit deletion
        wd.find_element("name", "delete").click()
        self.return_to_groups_page()

    def open_groups_page(self):
        wd = self.app.wd
        wd.find_element("link text", "groups").click()

    def modify_first(self, group):
        wd = self.app.wd
        self.open_groups_page()
        select_first_group(wd)
        # update group data
        wd.find_element("name", "edit").click()
        fill_group_fields(group, wd)
        # submit group update
        wd.find_element("name", "update").click()
        self.return_to_groups_page()
