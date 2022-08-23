from pages.base_page import BasePage


class LoginPage(BasePage):
   # title_scouts_panel_xpath = "//*[text()='Scouts Panel']"
   login_field_xpath = "//*[@id='login']"
   password_field_xpath = "//*[@id='password']"
   sign_in_button_xpath = "//*[@id='__next']/form/div/div[2]/button"
   login_url = 'https://scouts-test.futbolkolektyw.pl/en'
   expected_title = "Scouts panel - sign in"
   element_xpath = "//div/h5"
   expected_text = "Scouts Panel"


   def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)
   def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)
   def click_on_sign_in_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)

   def check_title_of_page(self):
       # actual_title = self.get_page_title()
       # assert actual_title == self.expected_title
       assert self.get_page_title(self.login_url) == self.expected_title

   def check_title(self):
        self.assert_element_text(self.element_xpath, self.expected_text)