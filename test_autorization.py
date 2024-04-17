import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    print("\nquit browser..")
    browser.quit()


# запустится 2 теста, для страницы на русском языке и на английском


class TestMainPage1:
    @pytest.mark.parametrize(
        "link",
        [
            "https://stepik.org/lesson/236895/step/1",
            "https://stepik.org/lesson/236896/step/1",
            # "https://stepik.org/lesson/236897/step/1",
            # "https://stepik.org/lesson/236898/step/1",
            # "https://stepik.org/lesson/236899/step/1",
            # "https://stepik.org/lesson/236903/step/1",
            # "https://stepik.org/lesson/236904/step/1",
            # "https://stepik.org/lesson/236905/step/1",
        ],
    )
    def test_autorization(self, browser, link):
        click_on_links = f"{link}/"
        browser.get(click_on_links)
        browser.find_element(
            By.CLASS_NAME,
            "navbar__auth_login",
        ).click()
        browser.find_element(By.NAME, "login").send_keys("a.galiyeva@globerce.capital")
        browser.find_element(By.NAME, "password").send_keys("A123098!")
        browser.find_element(By.CLASS_NAME, "sign-form__btn").click()
        answer = str(math.log(int(time.time())))
        browser.find_element(By.CLASS_NAME, "ember-text-area").send_keys(answer)
        browser.implicitly_wait(30)
        browser.find_element(By.CLASS_NAME, "submit-submission").click()
