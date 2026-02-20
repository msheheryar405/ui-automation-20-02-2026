
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
# Step 1: Start Chrome
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# Step 2: Open website
driver.get("https://practicetestautomation.com/practice-test-login/")
time.sleep(5)
driver.find_element(By.XPATH, "//*[@id='username']").send_keys("student")
driver.find_element(By.XPATH, "//input[@name='password']").send_keys("Password123")

driver.find_element(By.XPATH, '//*[@id="submit"]').click()
time.sleep(5)
# Step 4: Close browser
driver.find_element(By.XPATH, '//*[@id="menu-item-20"]/a').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="menu-item-21"]/a').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="menu-item-19"]/a').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="menu-item-43"]/a').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="loop-container"]/div/article/div[2]/p[8]/strong[2]/a').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="menu-item-43"]/a').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="menu-item-18"]/a').click()#contact page. After opening the url on home page.
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="menu-item-20"]/a').click()# render to practice page
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="loop-container"]/div/article/div[2]/div[1]/div[1]/p/a').click()
time.sleep(2)# test login url on  practice page
driver.execute_script("window.scrollTo(3, document.body.scrollHeight);")
time.sleep(3)
driver.find_element(By.XPATH, "//*[@id='username']").send_keys("student")
driver.find_element(By.XPATH, "//*[@id='password']").send_keys("Password123")
driver.find_element(By.XPATH, '//*[@id="submit"]').click()
time.sleep(3)# login form on practice page, these 3 lines 
driver.find_element(By.XPATH, '//*[@id="menu-item-20"]/a').click()# render to practice page from login again
time.sleep(2)
driver.execute_script("window.scrollTo(3, document.body.scrollHeight);")
driver.find_element(By.XPATH, '//*[@id="loop-container"]/div/article/div[2]/div[3]/div[1]/p/a').click()# render to test table page
time.sleep(2)
driver.execute_script("window.scrollTo({top: document.body.scrollHeight, behavior: 'smooth'});")
time.sleep(5)



driver.quit()







from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
# Step 1: Start Chrome
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://practicetestautomation.com/practice-test-login/")

driver.find_element(By.ID, "username").send_keys("student")
driver.find_element(By.ID, "password").send_keys("Password123")
driver.find_element(By.ID, "submit").click()
assert"Logged In Successfully" in driver.page_source
print("yes pass login")
driver.find_element(By.ID, "menu-item-43").click()# home page
driver.find_element(By.ID,  "menu-item-20").click()# practice page
driver.find_element(By.ID, "menu-item-21").click()# course  page
driver.find_element(By.ID, "menu-item-19").click()# blog  page
driver.find_element(By.ID, "menu-item-18").click()#contact page
driver.find_element(By.ID, "menu-item-43").click()# home page
main_window = driver.current_window_handle
driver.find_element(By.LINK_TEXT, "BestSeller XPath course").click()
time.sleep(2)
# switch to new tab
driver.switch_to.window(driver.window_handles[1])
assert len(driver.window_handles) >= 2, "New tab should be opened"
# close new tab
driver.close()
# switch back to main tab
driver.switch_to.window(main_window)
assert driver.current_window_handle == main_window, "Should be back on main window"
driver.find_element(By.LINK_TEXT,"COURSES").click()
time.sleep(5)
driver.find_element(By.ID, "menu-item-43").click()# home page
time.sleep(5)
assert "practicetestautomation.com" in driver.current_url, "Home page should be loaded"
driver.find_element(By.ID, "form_first_name_7").send_keys("John")# namebox on home page
time.sleep(5)
driver.find_element(By.ID, "form_email_7").send_keys("abc@gmail.com")# email box on home page
time.sleep(5)
driver.find_element(By.CSS_SELECTOR, "[data-automation-id='subscribe-submit-button']").click()
time.sleep(5)

driver.quit()
