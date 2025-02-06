import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)

driver.switch_to.new_window("window")
time.sleep(3)

driver.get("https://ya.ru")
time.sleep(3)
