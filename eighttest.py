from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

#Изучаем работу чекбокс и радиобаттон
link = "https://suninjuly.github.io/math.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    xel = browser.find_element(By.ID, "input_value" )
    x = xel.text
    y = calc(x)
    inputans = browser.find_element(By.ID, "answer")
    inputans.send_keys(y)
    check = browser.find_element(By.ID, "robotCheckbox")
    check.click()
    radio = browser.find_element(By.ID, "robotsRule")
    radio.click()
    button = browser.find_element(By.CLASS_NAME,"btn.btn-default")
    button.click()
finally:
    time.sleep(30)
    browser.quit()