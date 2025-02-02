import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Keys


option = webdriver.ChromeOptions()
option.add_argument('--window-size=1920,1080')
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service,options=option)
wait = WebDriverWait(driver, 10, poll_frequency=1)

KETBOARD_INPUT = ("xpath", "//input[@id='target']")

driver.get("https://the-internet.herokuapp.com/key_presses")

time.sleep(2)

driver.find_element(*KETBOARD_INPUT).send_keys("asdfghjkldfghjcvbn")

time.sleep(2)

driver.find_element(*KETBOARD_INPUT).send_keys(Keys.CONTROL + "a")

time.sleep(2)

driver.find_element(*KETBOARD_INPUT).send_keys(Keys.BACKSPACE)

time.sleep(2)
