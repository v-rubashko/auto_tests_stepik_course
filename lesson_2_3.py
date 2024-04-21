from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

try:
    link = ("https://suninjuly.github.io/redirect_accept.html")
    browser = webdriver.Chrome()
    browser.get(link)

    button_1 = browser.find_element(By.CSS_SELECTOR, ".trollface")
    button_1.click()
    second_window = browser.window_handles[1]
    browser.switch_to.window(second_window)
    number = int(browser.find_element(By.ID, "input_value").text)
    res = str(math.log(abs(12 * math.sin(number))))
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(res)
    button_2 = browser.find_element(By.CSS_SELECTOR, ".btn")
    button_2.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()