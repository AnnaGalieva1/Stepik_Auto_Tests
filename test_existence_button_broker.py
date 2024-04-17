import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait


def test_button():
    try:
        browser = webdriver.Chrome()
        browser.implicitly_wait(10)
        browser.get("https://broker.digideed.ae/login")
        assert browser.find_elements(
            By.TAG_NAME, "button"
        ), "No element"  # поиск по elements для создания списка, если элементы не найдены, вернется пустой список и отобразится указанное сообщение об ошибке. При поиске через element тест падает с ошибкой NoSuchElementException
    finally:
        time.sleep(5)
        browser.quit()
