from selenium.webdriver.chrome.webdriver import WebDriver
from pages.navigations import NavigationPage


def test_full_site_navigation(driver: WebDriver):
    driver.get("https://practicetestautomation.com/")

    nav = NavigationPage(driver)

    # HOME (already on home)
    nav.scroll_to_bottom()

    # PRACTICE
    nav.click_practice()
    nav.scroll_to_bottom()

    # COURSES
    nav.click_courses()
    nav.scroll_to_bottom()

    # BLOG
    nav.click_blog()
    nav.scroll_to_bottom()

    # CONTACT
    nav.click_contact()
    nav.scroll_to_bottom()

    assert "contact" in driver.current_url.lower()
