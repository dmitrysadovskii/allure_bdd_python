from selenium import webdriver
import pytest
import json
import os.path


def load_config(file_path):
    config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_path)
    with open(config_path) as f:
        target = json.load(f)
    return target


@pytest.fixture()
def browser(request):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    # driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://automationpractice.com/index.php")
    failed_before = request.session.testsfailed
    yield driver
    if request.session.testsfailed != failed_before:
        test_name = request.node.name
        take_screenshot(driver, test_name)
    driver.quit()


@pytest.fixture()
def user_config_data():
    config_data = load_config("recources/variables/user_data.json")
    return config_data['email'], config_data['passwd']


@pytest.fixture()
def get_db_config():
    db_config_data = load_config("recources/variables/db_config.json")
    return db_config_data


def take_screenshot(browser, test_name):
    screenshot_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                               "failure_screenshots")
    screenshot_file_path = f"{screenshot_dir}/{test_name}.png"
    browser.save_screenshot(screenshot_file_path)