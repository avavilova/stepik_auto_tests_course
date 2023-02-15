import os.path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import math

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)



    #Заполнить текстовые поля: имя, фамилия, email
    first_name = browser.find_element(By.NAME, "firstname")
    first_name.send_keys("Aryna")

    last_name = browser.find_element(By.NAME, "lastname")
    last_name.send_keys("Vavilava")

    email = browser.find_element(By.NAME, "email")
    email.send_keys("avtest29@gmail.com")

    #Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, "test228.txt")

    add_button = browser.find_element(By.ID, "file")
    add_button.send_keys(file_path)


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

