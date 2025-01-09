from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.page_load_strategy = 'eager'
driver = webdriver.Chrome(options=chrome_options)


driver.implicitly_wait(10)
driver.get('https://demoqa.com/dynamic-properties')

VISIBLE_AFTER_BUTTON = ("xpath", "//button[@id='visibleAfter']")
driver.find_element(*VISIBLE_AFTER_BUTTON).click()
