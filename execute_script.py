import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("https://SunInJuly.github.io/execute_script.html")
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)
    button = browser.find_element(By.CLASS_NAME, "btn-primary")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    checkbox = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']").click()
    radiobutton = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']").click()
    button.click()
finally:
    time.sleep(10)
    browser.quit()
