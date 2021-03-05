from pages.base_page import BasePage
from locator.account_page_locator import AccountPageLocator


class AccountPage(BasePage):

    def should_be_account_page(self):
        account_text = self.find_element(AccountPageLocator.LOCATOR_MY_ACCOUNT_TEXT).text
