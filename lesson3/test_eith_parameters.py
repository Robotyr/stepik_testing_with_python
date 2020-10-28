import pytest
from selenium import webdriver
import time
import math


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


list_of_sites = [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"
    ]


@pytest.mark.parametrize('link', list_of_sites)
def test_lets_collect_phrase(browser, language):
    url = f"{link}/"
    browser.get(url)
    input = browser.find_element_by_id("ember103")
    answer = math.log(int(time.time()))
    input.sendkeys(f"answer")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    answer = browser.findelement_by_class_name("smart-hints__feedback hints__component hints__component_showed ember-view")
    print
