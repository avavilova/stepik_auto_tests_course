from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.implicitly_wait(5)
browser.get("http://suninjuly.github.io/cats.html")

button = browser.find_element(By.ID, "button")
message = browser.find_element(By.ID, "verify_message")

assert "successful" in message.text