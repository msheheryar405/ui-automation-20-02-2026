from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    username_input = (By.ID, "username")
    password_input = (By.ID, "password")
    login_button = (By.ID, "submit")
    success_heading = (By.TAG_NAME, "h1")
    error_message = (By.ID, "error")
   
    def wait_for_text(self, locator, text):
     wait = WebDriverWait(self.driver, 10)
     wait.until(EC.visibility_of_element_located(locator))
     wait.until(EC.text_to_be_present_in_element(locator, text))
   
    def open_login_page(self):
        self.driver.get("https://practicetestautomation.com/practice-test-login/")

    def enter_username(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def get_success_heading(self):
     self.wait_for_text(self.success_heading, "Logged In Successfully")
     return self.driver.find_element(*self.success_heading).text

    def get_error_message(self):
     self.wait_for_text(self.error_message, "invalid")
     return self.driver.find_element(*self.error_message).text
   #hashtag comment to check commit and push functionality