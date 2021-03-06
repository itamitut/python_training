from selenium import webdriver
from addressbook.fixture.session import SessionHelper


class Application:

    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(6)
        self.session = SessionHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get('http:\\localhost\\addressbook')

    def open_group_page(self):
        wd = self.wd
        wd.find_element_by_link_text('groups').click()


    def create_group(self, group):
        wd = self.wd
        self.open_group_page()
        wd.find_element_by_name('new').click()
        wd.find_element_by_name('group_name').click()
        wd.find_element_by_name('group_name').send_keys(group.name)
        wd.find_element_by_name('group_header').click()
        wd.find_element_by_name('group_header').send_keys(group.header)
        wd.find_element_by_name('group_footer').click()
        wd.find_element_by_name('group_footer').send_keys(group.footer)
        wd.find_element_by_name('submit').click()
        self.return_to_groups()

    def return_to_groups(self):
        wd = self.wd
        wd.find_element_by_link_text('groups').click()


    def destroy(self):
        wd = self.wd
        wd.quit()
