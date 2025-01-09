import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.wikipedia.org/")

url = driver.current_url

print('URL страницы: ', url)

assert url == "https://www.wikipedia.org/", 'Ошибка в URL'

current_title = driver.title

print('Текущий заголовок: ', current_title)

assert current_title == 'Wikipedia', 'Некоректный заголовок'

print(driver.page_source)

time.sleep(1)
