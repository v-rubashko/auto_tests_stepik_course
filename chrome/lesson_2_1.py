from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    treasure_img = browser.find_element(By.CSS_SELECTOR, "#treasure")
    treasure_val = treasure_img.get_attribute("valuex")
    y = calc(treasure_val)
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)
    checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    checkbox.click()
    checkbox = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    checkbox.click()
    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()