from pages.base_page import BasePage
from locator.login_page_locator import LoginPageLocator


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.login_form_is_present()
        self.auth_text_is_present()

    def login_form_is_present(self):
        self.find_element(LoginPageLocator.LOCATOR_LOGIN_FORM)

    def auth_text_is_present(self):
        auth_text = self.find_element(LoginPageLocator.LOCATOR_AUTH_TEXT).text
        check_text = 'AUTHENTICATION'
        assert auth_text == check_text, f'{auth_text} is not eq {check_text}'

    def login(self, email, passwd):
        email_field = self.find_element(LoginPageLocator.LOCATOR_EMAIL_FIELD)
        email_field.send_keys(email)
        passwd_field = self.find_element(LoginPageLocator.LOCATOR_PASSWD_FIELD)
        passwd_field.send_keys(passwd)
        sing_in_button = self.find_element(LoginPageLocator.LOCATOR_SING_IN_BUTTON)
        sing_in_button.click()