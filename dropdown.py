from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/selects2.html")
    num1 = browser.find_element(By.ID, "num1")
    num2 = browser.find_element(By.ID, "num2")
    num1 = num1.text
    num2 = num2.text
    sum = int(num1) + int(num2)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(sum))
    button = browser.find_element(By.CSS_SELECTOR, "button.btn-default")
    button.click()
finally:
    time.sleep(10)
    browser.quit()
