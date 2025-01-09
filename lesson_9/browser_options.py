import time

from selenium import webdriver

options = webdriver.ChromeOptions()
#загрузка только DOM
options.page_load_strategy = 'eager'
# options.add_argument('--headless')
# options.add_argument('--incognito')
# options.add_argument('--ignore-sertificate-errors')
options.add_argument('--window-size=1920,1080')
# options.add_argument('--disable-cache')

driver = webdriver.Chrome(options=options)
# driver.set_window_size(300, 300)

start_time = time.time()

driver.get('https://whatismyipaddress.com/')

end_time = time.time()
result_time = end_time - start_time
print(result_time)
