from pages.base_page import BasePage
from locator.main_page_locator import MainPageLocator


class MainPage(BasePage):

    def open_login_page(self):
        sign_in_button = self.find_element(
            MainPageLocator.LOCATOR_SING_IN_BUTTON
        )
        sign_in_button.click()

    def get_closes_names_on_the_page(self):
        pass