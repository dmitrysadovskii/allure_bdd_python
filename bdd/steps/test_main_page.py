from pytest_bdd import given, when, then
from pages.main_page import MainPage
from pages.login_page import LoginPage


@given('open main page')
def open(browser):
    main_page = MainPage(browser)
    main_page.open_main_page()
    return main_page


@when('click on the sing in button')
def click_sing_in_button(browser):
    main_page = MainPage(browser)
    main_page.open_login_page()


@then('user is on login page')
def login_page_validation(browser):
    login_page = LoginPage(browser)
    login_page.should_be_login_page()