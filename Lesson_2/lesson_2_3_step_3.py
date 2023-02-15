from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import math

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #Нажать на кнопку
    open_button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    open_button.click()

    #Принять confirm
    confirm = browser.switch_to.alert
    confirm.accept()

    #На новой странице решить капчу для роботов, чтобы получить число с ответом
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text

    res = str(math.log(abs(12*math.sin(int(x)))))

    text_field = browser.find_element(By.ID, "answer")
    text_field.send_keys(res)

    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    submit_button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()