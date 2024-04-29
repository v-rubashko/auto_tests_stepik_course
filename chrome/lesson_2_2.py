from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import os
import time


try:
    link = "https://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')

    first_name = browser.find_element(By.NAME, "firstname")
    first_name.send_keys("Alessandro")
    last_name = browser.find_element(By.NAME, "lastname")
    last_name.send_keys("Del Piero")
    email = browser.find_element(By.NAME, "email")
    email.send_keys("ADP@forza.juve")
    file = browser.find_element(By.ID, "file")
    file.send_keys(file_path)
    browser.find_element(By.CSS_SELECTOR, ".btn").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
