from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
#Изучаем получение значения аттрибута
link = "http://suninjuly.github.io/get_attribute.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    tres = browser.find_element(By.TAG_NAME, "img")
    valx = tres.get_attribute("valuex")
    y = calc(valx)
    input1 = browser.find_element(By.ID,"answer")
    input1.send_keys(y)
    check = browser.find_element(By.ID, "robotCheckbox")
    check.click()
    radio = browser.find_element(By.ID, "robotsRule")
    radio.click()
    button = browser.find_element(By.CLASS_NAME,"btn.btn-default")
    button.click()
finally:
    time.sleep(30)
    browser.quit()