import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestSearchLink(unittest.TestCase):
    def test1(self):
        try:
            link = "http://suninjuly.github.io/registration1.html"
            browser = webdriver.Chrome()
            browser.get(link)

            input1 = browser.find_element(
                By.XPATH, "//input[@placeholder='Input your first name']"
            )
            input1.send_keys("test")
            input2 = browser.find_element(
                By.XPATH, "//input[@placeholder='Input your last name']"
            )
            input2.send_keys("test")
            input3 = browser.find_element(
                By.XPATH, "//input[@placeholder='Input your email']"
            )
            input3.send_keys("test")
            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            time.sleep(1)

            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual(
                "Congratulations! You have successfully registered!",
                welcome_text,
                msg=None,
            )

        finally:
            browser.quit()

    def test2(self):
        try:
            link = "http://suninjuly.github.io/registration2.html"
            browser = webdriver.Chrome()
            browser.get(link)

            input1 = browser.find_element(
                By.XPATH, "//input[@placeholder='Input your first name']"
            )
            input1.send_keys("test")
            input2 = browser.find_element(
                By.XPATH, "//input[@placeholder='Input your last name']"
            )
            input2.send_keys("test")
            input3 = browser.find_element(
                By.XPATH, "//input[@placeholder='Input your email']"
            )
            input3.send_keys("test")
            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            time.sleep(1)

            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual(
                "Congratulations! You have successfully registered!",
                welcome_text,
                msg=None,
            )
        finally:
            browser.quit()


if __name__ == "__main__":
    unittest.main()
