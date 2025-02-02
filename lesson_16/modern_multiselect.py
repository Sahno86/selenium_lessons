import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Keys

options = webdriver.ChromeOptions()
options.page_load_strategy = 'eager'
options.add_argument('--window-size=1920,1080')
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service,options=options)
wait = WebDriverWait(driver, 10, poll_frequency=1)

SELECT_LOCATOR = ("xpath", "//input[@id='react-select-3-input']")

driver.get("https://demoqa.com/select-menu")

time.sleep(3)

driver.find_element(*SELECT_LOCATOR).send_keys("Ms.")
driver.find_element(*SELECT_LOCATOR).send_keys(Keys.ENTER)

time.sleep(3)

MULTISELECT_LOCATOR = ("xpath", "//input[@id='react-select-4-input']")

time.sleep(2)
driver.find_element(*MULTISELECT_LOCATOR).send_keys("gre")
time.sleep(2)
driver.find_element(*MULTISELECT_LOCATOR).send_keys(Keys.TAB)
time.sleep(2)
driver.find_element(*MULTISELECT_LOCATOR).send_keys("Black")
time.sleep(2)
driver.find_element(*MULTISELECT_LOCATOR).send_keys(Keys.ENTER)
time.sleep(2)