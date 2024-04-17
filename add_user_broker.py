from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("https://digideed-broker.trafficwave.kz/login")
    password = browser.find_element(By.XPATH, "//input[@type='password']")
    password.send_keys("dev")
    username = browser.find_element(
        By.CLASS_NAME,
        "div.mb-8.flex.flex-col.gap-y-4 .relative .relative.flex.flex-col :nth-child(2)",
    )
    username.send_keys("dev_supervisor@dev.com")
    button = browser.find_element(By.XPATH, "//button[text()='Login']").click()


finally:
    time.sleep(10)
    browser.quit()
