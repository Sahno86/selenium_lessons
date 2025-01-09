import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://info-hit.ru/")

time.sleep(2)

driver.find_element('class name', 'header__nav__menu-actions__item').click()

time.sleep(2)
