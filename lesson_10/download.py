import os
import time
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": f"{os.getcwd()}\\downloads"
}
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(options=chrome_options)

driver.get('https://the-internet.herokuapp.com/download')
driver.find_element('xpath', '//a[@href="download/DocFile.doc"]').click()
time.sleep(5)
