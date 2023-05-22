from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
#Использование Java-Script для прокрутки страницы вниз, так как если элемент перегорожен, то по нему нельзя кликнуть
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    xel = browser.find_element(By.ID, "input_value" )
    x = xel.text
    y = calc(x)
    inputans = browser.find_element(By.ID, "answer")
    inputans.send_keys(y)
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    check = browser.find_element(By.ID, "robotCheckbox")
    check.click()
    radio = browser.find_element(By.ID, "robotsRule")
    radio.click()
    button.click()
finally:
    time.sleep(30)
    browser.quit()