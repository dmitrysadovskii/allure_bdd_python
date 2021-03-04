from pytest_bdd import scenario
from bdd.steps.test_main_page import *



@scenario('../features/login_page.feature', 'Test user can open login page')
def test_login_page():
    print('test')