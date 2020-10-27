from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

browser = webdriver.Chrome()

link = "http://suninjuly.github.io/explicit_wait2.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    book_button = browser.find_element_by_id("book")

    price = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))

    book_button.click()

    x_element = browser.find_element_by_id("input_value")
    x = calc(int(x_element.text))

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(f"{x}")

    solve_button = browser.find_element_by_id("solve")

    solve_button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла