from selenium.webdriver.common.by import By


class LoginPageLocator:

    LOCATOR_AUTH_TEXT = (By.CLASS_NAME, 'page-heading')
    LOCATOR_LOGIN_FORM = (By.ID, 'login_form')
    LOCATOR_EMAIL_FIELD = (By.ID, 'email')
    LOCATOR_PASSWD_FIELD = (By.ID, 'passwd')
    LOCATOR_SING_IN_BUTTON = (By.ID, 'SubmitLogin')