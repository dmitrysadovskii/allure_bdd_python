from pages.base_page import BasePage
from locator.account_page_locator import AccountPageLocator


class AccountPage(BasePage):

    def should_be_account_page(self):
        account_text = self.find_element(AccountPageLocator.LOCATOR_MY_ACCOUNT_TEXT).text
        check_text = 'my account'
        assert account_text.lower() == check_text, f'Text on UI {account_text} is not eq {check_text}'
