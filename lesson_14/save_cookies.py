import os
import pickle
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_argument('--window-size=1920,1080')
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service,options=options)
wait = WebDriverWait(driver, 10, poll_frequency=1)

# LOGIN_FIELD = ("xpath", "//input[@id='login_email']")
# PASSWORD_FIELD = ("xpath", "//input[@id='password']")
# SUBMIT_BUUTON = ("xpath", "//button[@id='loginformsubmit']")

driver.get('https://www.freeconferencecall.com/ru/pl/login')

# driver.find_element(*LOGIN_FIELD).send_keys("mishenkinav@gmail.com")
# driver.find_element(*PASSWORD_FIELD).send_keys("qaz")
# time.sleep(5)
# driver.find_element(*SUBMIT_BUUTON).click()

# pickle.dump(driver.get_cookies(), open(os.getcwd()+"\\lesson_14\\cookies\\cookies.pkl", "wb"))

#чтобы добавить новые куки, сначала удаляем старые
driver.delete_all_cookies()

cookies = pickle.load(open(os.getcwd()+"\\lesson_14\\cookies\\cookies.pkl", "rb"))

for cookie in cookies:
    driver.add_cookie(cookie)

#чтобы куки применились обновляем страницу
driver.refresh()

time.sleep(5)
