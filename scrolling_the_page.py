from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/execute_script.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("input_value")
    x = calc(int(x_element.text))

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(f"{x}")

    browser.execute_script("window.scrollBy(0, 100);")

    checkbox1 = browser.find_element_by_xpath('//input[@id="robotCheckbox"]')
    checkbox1.click()

    radiobuttton = browser.find_element_by_xpath('//input[@id="robotsRule"]')
    radiobuttton.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла