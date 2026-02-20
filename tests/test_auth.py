from time import time

from selenium.webdriver.chrome.webdriver import WebDriver
from pages import login_page
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage

def test_login_positive(driver: WebDriver):
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.enter_username("student")
    login_page.enter_password("Password123")
    login_page.click_login()
    assert "Logged In Successfully" in login_page.get_success_heading()

def test_login_wrongusername(driver: WebDriver):
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.enter_username("studendt")
    login_page.enter_password("Password123")
    login_page.click_login()
    assert "Your username is invalid!" in login_page.get_error_message() 


def test_login_wrongpassword(driver: WebDriver):
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.enter_username("student")
    login_page.enter_password("Password12")
    login_page.click_login()
    assert "Your password is invalid!"  in login_page.get_error_message()

def test_logout_flow(driver: WebDriver):
    # login again with correct credentials
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.enter_username("student")
    login_page.enter_password("Password123")
    login_page.click_login()

    # logout from dashboard
    dashboard = DashboardPage(driver)
    dashboard.click_logout()

    # verify login page opened again
    assert "practice-test-login" in driver.current_url











































































# import pytest
# from selenium.webdriver.chrome.webdriver import WebDriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# def test_login(driver: WebDriver):
#     """
#     TEST CASE:
#     Verify user can login successfully
#     """
#     driver.get("https://practicetestautomation.com/practice-test-login/")
#
#     driver.find_element(By.ID, "username").send_keys("student")
#     driver.find_element(By.ID, "password").send_keys("Password23")
#     driver.find_element(By.ID, "submit").click()
#
#     assert "Logged In Successfully" in driver.page_source


# def test_menu_navigation(driver: WebDriver):
#     """
#     TEST CASE:
#     Verify menu navigation works
#     """
#     driver.get("https://practicetestautomation.com/")
#
#     driver.find_element(By.ID, "menu-item-43").click()   # Home
#     driver.find_element(By.ID, "menu-item-20").click()   # Practice
#     driver.find_element(By.ID, "menu-item-21").click()   # Courses
#     driver.find_element(By.ID, "menu-item-19").click()   # Blog
#     driver.find_element(By.ID, "menu-item-18").click()   # Contact
#
#     assert "Contact" in driver.title


# def test_new_tab(driver: WebDriver):
#     """
#     TEST CASE:
#     Verify new tab opens and closes correctly
#     """
#     driver.get("https://practicetestautomation.com/")
#
#     main_window = driver.current_window_handle
#
#     driver.find_element(By.LINK_TEXT, "BestSeller XPath course").click()
#
#     WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
#
#     driver.switch_to.window(driver.window_handles[-1])
#     driver.close()
#
#     driver.switch_to.window(main_window)
#
#     assert driver.current_window_handle == main_window


# def test_subscription_form(driver: WebDriver):
#     """
#     TEST CASE:
#     Verify subscription form submission
#     """
#     driver.get("https://practicetestautomation.com/")
#
#     driver.find_element(By.ID, "form_first_name_7").send_keys("John")
#     driver.find_element(By.ID, "form_email_7").send_keys("abcgmail.com")
#
#     driver.find_element(
#         By.CSS_SELECTOR,
#         "[data-automation-id='subscribe-submit-button']"
#     ).click()
#
#     page_source = driver.page_source.lower()
#     assert "success" in page_source or "thank" in page_source





