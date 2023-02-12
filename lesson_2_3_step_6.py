from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import math

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    troll_button = browser.find_element(By.CSS_SELECTOR, "button.trollface.btn.btn-primary")
    troll_button.click()

    #Переключиться на новую вкладку
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    #Пройти капчу для робота и получить число-ответ
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text

    res = str(math.log(abs(12*math.sin(int(x)))))

    test_field = browser.find_element(By.ID, "answer")
    test_field.send_keys(res)

    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    submit_button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()