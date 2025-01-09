import os
import time
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--window-size=1920,1080')
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://the-internet.herokuapp.com/upload")

time.sleep(3)

upload_field = driver.find_element("xpath", '//input[@type="file"]')

upload_field.send_keys(f'{os.getcwd()}//downloads//DocFile.doc')

time.sleep(3)

# если загрузка на сайте реализована через кнопку, искать "xpath", '//input[@type="file"]'
