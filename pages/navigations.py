from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class NavigationPage:
    def __init__(self, driver):
        self.driver = driver

    # IMPORTANT: header menu only (more specific than LINK_TEXT)
    # This targets top nav bar links
    home_menu = (By.CSS_SELECTOR, "nav a[href='https://practicetestautomation.com/']")
    practice_menu = (By.CSS_SELECTOR, "nav a[href*='/practice']")
    courses_menu = (By.CSS_SELECTOR, "nav a[href*='/courses']")
    blog_menu = (By.CSS_SELECTOR, "nav a[href*='/blog']")
    contact_menu = (By.CSS_SELECTOR, "nav a[href*='/contact']")

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_to_top(self):
        self.driver.execute_script("window.scrollTo(0, 0);")

    def wait_click(self, locator):
        self.scroll_to_top()  # key line
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        ).click()

    def click_home(self):
        self.wait_click(self.home_menu)

    def click_practice(self):
        self.wait_click(self.practice_menu)

    def click_courses(self):
        self.wait_click(self.courses_menu)

    def click_blog(self):
        self.wait_click(self.blog_menu)

    def click_contact(self):
        self.wait_click(self.contact_menu)
