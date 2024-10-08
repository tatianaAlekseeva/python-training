from model.group import Group


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
        self.fill_group_fields(group)
        # submit group creation
        wd.find_element("name", "submit").click()
        self.return_to_groups_page()
        self.group_cache = None

    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        # submit deletion
        wd.find_element("name", "delete").click()
        self.return_to_groups_page()
        self.group_cache = None

    def delete_group_by_id(self, group_id):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_id(group_id)
        # submit deletion
        wd.find_element("name", "delete").click()
        self.return_to_groups_page()
        self.group_cache = None
    def delete_first_group(self):
        self.delete_group_by_index(0)

    def open_groups_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements("name", "new")) > 0):
            wd.find_element("link text", "groups").click()

    def modify_group_by_index(self, new_group_data, index):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        # update group data
        wd.find_element("name", "edit").click()
        self.fill_group_fields(new_group_data)
        # submit group update
        wd.find_element("name", "update").click()
        self.return_to_groups_page()
        self.group_cache = None

    def modify_group_by_id(self, new_group_data, group_id):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_id(group_id)
        # update group data
        wd.find_element("name", "edit").click()
        self.fill_group_fields(new_group_data)
        # submit group update
        wd.find_element("name", "update").click()
        self.return_to_groups_page()
        self.group_cache = None

    def modify_first(self, new_group_data):
        self.modify_group_by_index(new_group_data, 0)

    def select_first_group(self):
        self.select_group_by_index(0)

    def select_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements("name", "selected[]")[index].click()

    def fill_group_fields(self, group):
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element("name", field_name).click()
            wd.find_element("name", field_name).clear()
            wd.find_element("name", field_name).send_keys(text)

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements("name", "selected[]"))

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_groups_page()
            self.group_cache = []
            for element in wd.find_elements("css selector", "span.group"):
                text = element.text
                group_id = element.find_element("name", "selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, group_id=group_id))
        return list(self.group_cache)

    def select_group_by_id(self, group_id):
        wd = self.app.wd
        wd.find_element("css selector", "input[value='%s']" % group_id).click()

