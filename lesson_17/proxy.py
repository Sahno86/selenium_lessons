import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

PROXY_SERVER = "username:password@37.19.220.129:8443"

options = Options()
options.add_argument(f"--proxy-server-={PROXY_SERVER}")
driver = webdriver.Chrome(options=options)


driver.get("https://2ip.ru") # 188.226.3.158 188.226.3.158

time.sleep(5)

