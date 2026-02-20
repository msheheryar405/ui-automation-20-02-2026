from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DashboardPage:
    def __init__(self, driver):
        self.driver = driver

    heading = (By.TAG_NAME, "h1")
    logout_link = (By.LINK_TEXT, "Log out")

    def wait_visible(self, locator):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        )

    def get_heading(self):
        self.wait_visible(self.heading)
        return self.driver.find_element(*self.heading).text

    def click_logout(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.logout_link)
        ).click()
