from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_argument('--window-size=1920,1080')
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service,options=options)
wait = WebDriverWait(driver, 10, poll_frequency=1)

driver.get('https://www.freeconferencecall.com/ru/pl/login')

# print(driver.get_cookie("country_code"))
print(driver.get_cookies())

driver.add_cookie({
    "name": "Example",
    "value": "Kukushka"
})

print(driver.get_cookie("Example"))

before = driver.get_cookie("split")
print(before)

driver.delete_cookie("split")
driver.add_cookie({
    "name": "split",
    "value": "QWERTY"
    })

after = driver.get_cookie("split")
print(after)

# driver.delete_all_cookies()