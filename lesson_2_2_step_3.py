from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #Посчитать сумму заданных чисел
    x_element = browser.find_element(By.ID, "num1")
    x = x_element.text

    y_element = browser.find_element(By.ID, "num2")
    y = y_element.text

    sum = str(int(x)+int(y))

    # Выбрать в выпадающем списке значение равное расчитанной сумме
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    #select.select_by_visible_text("10")
    select.select_by_value(sum)
    #browser.find_element(By.TAG_NAME, "select").click()
    #browser.find_element(By.CSS_SELECTOR, "[value = sum]").click()

    # Нажать на кнопку Submit
    button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-default")
    button.click()

    # ждем загрузки страницы
    time.sleep(1)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

