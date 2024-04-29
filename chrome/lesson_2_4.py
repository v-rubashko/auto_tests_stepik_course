from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

try:
    link = ("http://suninjuly.github.io/explicit_wait2.html")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)
    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    book_button = browser.find_element(By.ID, "book")
    book_button.click()
    number = int(browser.find_element(By.ID, "input_value").text)
    res = str(math.log(abs(12 * math.sin(number))))
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(res)
    button_2 = browser.find_element(By.ID, "solve")
    button_2.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()