from selenium import webdriver
import time

    # первоначальный адрес
base_url = ("http://yclients.com")
    # запуск браузера
driver = webdriver.Chrome("/Users/robotyr/Documents/chromedriver")
    # переход на первоначальный адрес
driver.get(base_url)
    # разворачиваем окно на весь экран
driver.maximize_window()

login_field = driver.find_element_by_name('email')

login_field.send_keys("a.panov@yclients.com")

password_field = driver.find_element_by_name('password')
password_field.send_keys("apanov")

driver.find_element_by_link_text('Login').click()

time.sleep(5)

print(driver.current_url)


driver.find_element_by_xpath('//*[@id="header"]/div[2]/a[2]')

driver.find