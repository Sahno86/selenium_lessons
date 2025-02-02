import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
#необходимо импортировать select
from selenium.webdriver.support.select import Select


option = webdriver.ChromeOptions()
option.add_argument('--window-size=1920,1080')
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service,options=option)
wait = WebDriverWait(driver, 10, poll_frequency=1)

SELECT_LOCATOR = ("xpath", "//select[@id='dropdown']")

driver.get('https://the-internet.herokuapp.com/dropdown')

DROPDOWN = Select(driver.find_element(*SELECT_LOCATOR))

# time.sleep(1)
# DROPDOWN.select_by_visible_text("Option 1")
# time.sleep(1)
# DROPDOWN.select_by_value("2")
# time.sleep(1)
# DROPDOWN.select_by_index(1)
# time.sleep(1)

all_options = DROPDOWN.options

# for option in all_options:
#     time.sleep(1)
#     if "Option 1" in option.text:
#         print("Опция присутствует")
#     DROPDOWN.select_by_visible_text(option.text)

# for option in all_options:
#     time.sleep(1)
#     DROPDOWN.select_by_index(all_options.index(option))

for option in all_options:
    time.sleep(1)
    DROPDOWN.select_by_value(option.get_attribute("value"))
