from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
# -------------------------
# Browser setup
# -------------------------
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(10)          # Global wait for elements
driver.maximize_window()

# -------------------------
# Open site
# -------------------------
driver.get("https://practicetestautomation.com/practice-test-login/")

# -------------------------
# Login
# -------------------------
try:
    driver.find_element(By.ID, "username").send_keys("student")
    driver.find_element(By.ID, "password").send_keys("Password12")
    driver.find_element(By.ID, "submit").click()
    
    assert "Logged In Successfully" in driver.page_source
    print("✅ Login successful")
except Exception as e:
    screenshot_dir = os.path.join(os.path.expanduser("~"), "Desktop", "Sheheryar")
    os.makedirs(screenshot_dir, exist_ok=True)
    screenshot_path = os.path.join(screenshot_dir, "login_failed.png")
    driver.save_screenshot(screenshot_path)
    print(f"❌ Login failed: {e}")
    print(f"📸 Screenshot saved at: {screenshot_path}")
    
    
    

# -------------------------
#driver.find_element(By.ID, "username").send_keys("student")
#driver.find_element(By.ID, "password").send_keys("Password12")
#driver.find_element(By.ID, "submit").click()

#assert "Logged In Successfully" in driver.page_source
#print("✅ Login successful")
# -------------------------
# Note on waits
# once at beginning
#driver.implicitly_wait(10)
# normal actions
#driver.find_element(By.ID, "username").send_keys("student")
# special case
#WebDriverWait(driver, 10).until(
#EC.element_to_be_clickable((By.ID, "submit"))).click()

# -------------------------
# Menu navigation (implicit wait is enough)
# -------------------------
driver.find_element(By.ID, "menu-item-43").click()   # Home
driver.find_element(By.ID, "menu-item-20").click()   # Practice
driver.find_element(By.ID, "menu-item-21").click()   # Courses
driver.find_element(By.ID, "menu-item-19").click()   # Blog
driver.find_element(By.ID, "menu-item-18").click()   # Contact
driver.find_element(By.ID, "menu-item-43").click()   # Back to Home

# -------------------------
# Handle link that opens NEW TAB
# -------------------------
main_window = driver.current_window_handle

driver.find_element(By.LINK_TEXT, "BestSeller XPath course").click()

# wait for new tab
WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))

# switch to new tab
driver.switch_to.window(driver.window_handles[-1])

# close new tab
driver.close()

# switch back to main tab
driver.switch_to.window(main_window)

# -------------------------
# Navigate to courses using link text
# -------------------------
current_url = driver.current_url
driver.find_element(By.LINK_TEXT, "COURSES").click()
WebDriverWait(driver, 5).until(EC.url_changes(current_url))
driver.find_element(By.ID, "menu-item-43").click()   # Home again

# -------------------------
# Fill subscription form (explicit wait needed)
# -------------------------
driver.find_element(By.ID, "form_first_name_7").send_keys("John")
driver.find_element(By.ID, "form_email_7").send_keys("abc@gmail.com")

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-automation-id='subscribe-submit-button']"))).click()

assert "success" in driver.page_source.lower() or "thank" in driver.page_source.lower(), "Form submission should be successful"

# -------------------------
# Close browser
# -------------------------
driver.quit()
