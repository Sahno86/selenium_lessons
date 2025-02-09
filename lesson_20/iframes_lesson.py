import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)

FORM_NAME_FIELD_LOCATOR = ("xpath", "//input[@id='RESULT_TextField-0']")

driver.get("https://testautomationpractice.blogspot.com/")

# переход на frame
driver.switch_to.frame("frame-one796456169")
time.sleep(3)
driver.find_element(*FORM_NAME_FIELD_LOCATOR).send_keys("Aleksei")
time.sleep(3)

# переход к дефолтной части страницы
driver.switch_to.default_content()

# если во фрейме есть вложенные фреймы, переключаться нужно последовательно
# для перехода на ступень выше используем следующий метод:
# driver.switch_to.parent_frame()