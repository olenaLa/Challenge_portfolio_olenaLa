import os
import time
import unittest
from selenium import webdriver

from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.dashboard import DashboardPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT



class TestLoginPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_login_to_the_system(self):
        user_login = LoginPage(self.driver)
        dashboard_page = DashboardPage(self.driver)
        user_login.check_title_of_page()
        user_login.check_title()
        user_login.type_in_email('user02@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_sign_in_button()
        dashboard_page.check_title_of_page()
        time.sleep(5)

    @classmethod
    def tearDown(self):
        self.driver.quit()