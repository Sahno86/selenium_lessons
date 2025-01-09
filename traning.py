from selenium import webdriver
from selenium.webdriver.common.by import By

# Открываем браузер
driver = webdriver.Chrome()

# Переходим на страницу
driver.get("https://example.com")

# Находим элемент по ID
element_by_id = driver.find_element(By.ID, "my-id")

# Находим элемент по CSS-селектору
element_by_css_selector = driver.find_element(By.CSS_SELECTOR, ".my-class")

# Закрываем браузер
driver.quit()
