import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://www.freeconferencecall.com/global/pl')

time.sleep(2)

login_button = driver.find_element('xpath', "//a[@id='login-desktop']")

login_button.click()

time.sleep(2)

email_field = driver.find_element('xpath', "//input[@id='login_email']")
email_field.send_keys('mishenkinav@gmail.com')
print(email_field.get_attribute("value"))

time.sleep(5)

email_field.clear()

time.sleep(5)


driver.quit()