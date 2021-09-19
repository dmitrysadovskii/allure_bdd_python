from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.account_page import AccountPage
import allure


@allure.feature("Check valid user can login to the system")
def test_login_to_the_system(browser):
    with allure.step('Open login page'):
        main_page = MainPage(browser)
        main_page.open_login_page()
    with allure.step('Check login page displays'):
        login_page = LoginPage(browser)
        login_page.should_be_login_page()
    with allure.step('Login as a user "dmitry@gmail.com"'):
        login_page.login("dmitry@gmail.com", "11111")
    with allure.step('Check account page displays'):
        AccountPage(browser).should_be_account_page()
        
@allure.story("Check invalid user can login to the system")
def test_invalid_login_to_the_system(browser):
    with allure.step('Open login page'):
        main_page = MainPage(browser)
        main_page.open_login_page()
    with allure.step('Check login page displays'):
        login_page = LoginPage(browser)
        login_page.should_be_login_page()
    with allure.step('Login as a user "dmitry@gmail.com"'):
        login_page.login("dmitry@gmail.com", "111112")
    with allure.step('Check account page displays'):
        AccountPage(browser).should_be_account_page()
