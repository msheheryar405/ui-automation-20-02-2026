import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
from datetime import datetime


@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()


def pytest_runtest_makereport(item, call):
    if call.when == "call" and call.excinfo is not None:
        driver = item.funcargs.get('driver')
        if driver:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")[:-3]
            screenshot_path = os.path.join(os.getcwd(), f"login-1-failed_{timestamp}.png")
            driver.save_screenshot(screenshot_path)

