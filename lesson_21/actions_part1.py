import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
action = ActionChains(driver)

LEFT_CLICK_BUTTON_LOCATOR = ("xpath", "//button[@name='leftClick']")
DOUBLE_CLICK_BUTTON_LOCATOR = ("xpath", "//button[@name='doubleClick']")
RIGHT_CLICK_BUTTON_LOCATOR = ("xpath", "//button[@name='rightClick']")
COLOR_CHANGE_BUTTON_LOCATOR = ("xpath", "//button[@name='colorChangeOnHover']")


driver.get("https://testkru.com/Elements/Buttons")

left_button = driver.find_element(*LEFT_CLICK_BUTTON_LOCATOR)
double_click_button = driver.find_element(*DOUBLE_CLICK_BUTTON_LOCATOR)
right_click_button = driver.find_element(*RIGHT_CLICK_BUTTON_LOCATOR)
hover_button = driver.find_element(*COLOR_CHANGE_BUTTON_LOCATOR)

# action.click(left_button).perform()
# action.double_click(double_click_button).perform()
# action.context_click(right_click_button).perform()

action.click(left_button).pause(2) \
    .double_click(double_click_button).pause(2) \
    .context_click(right_click_button).pause(2) \
    .perform()

time.sleep(3)

action.move_to_element(hover_button).pause(2).perform()
