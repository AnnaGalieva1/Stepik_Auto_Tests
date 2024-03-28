from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")
    x_element = browser.find_element(By.XPATH, "//img[@src='images/chest.png']")
    x = x_element.get_attribute("valuex")
    y = calc(x)
    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()
    radiobutton = browser.find_element(By.ID, "robotsRule")
    radiobutton.click()
    button = browser.find_element(By.CSS_SELECTOR, "button.btn-default")
    button.click()
finally:
    time.sleep(10)
    browser.quit()
