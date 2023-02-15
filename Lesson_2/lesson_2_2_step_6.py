from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import math

try:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #Считать значение переменной x
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text

    #Посчитать математическую функцию от x
    res = str(math.log(abs(12*math.sin(int(x)))))

    #Проскроллить страницу вниз.
    textField = browser.find_element(By.ID, "answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", textField)

    #Ввести ответ в текстовое поле
    textField.send_keys(res)

    #Выбрать checkbox "I'm the robot"
    robotCheckbox = browser.find_element(By.ID, "robotCheckbox")
    robotCheckbox.click()

    #Переключить radiobutton "Robots rule!"
    radioRobotsRule = browser.find_element(By.CSS_SELECTOR, "[value='robots']")
    radioRobotsRule.click()

    # Нажать на кнопку Submit
    button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    button.click()

    # ждем загрузки страницы
    time.sleep(1)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

