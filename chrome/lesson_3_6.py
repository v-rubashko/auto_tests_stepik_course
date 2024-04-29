import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.parametrize("lk", ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1", "https://stepik.org/lesson/236897/step/1",
             "https://stepik.org/lesson/236898/step/1", "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1",
             "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"])
def test_stepik(browser, lk):
    link = f"{lk}"
    browser.get(link)
    browser.implicitly_wait(10)
    browser.find_element(By.CSS_SELECTOR, "#ember457").click()
    browser.find_element(By.CSS_SELECTOR, "#id_login_email").send_keys("")
    browser.find_element(By.CSS_SELECTOR, "#id_login_password").send_keys("")
    browser.find_element(By.CSS_SELECTOR, "#login_form > button").click()
    time.sleep(1)
    browser.find_element(By.CSS_SELECTOR, "textarea").send_keys(str(math.log(int(time.time()))))
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))).click()
    smart_hint = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint"))).text
    # WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "again-btn white"))).click()

    assert smart_hint == "Correct!", f"{smart_hint}"
