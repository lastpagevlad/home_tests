from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
#Переход на другую страницу
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")
    btn = browser.find_element(By.CLASS_NAME,"trollface.btn.btn-primary")
    btn.click()
    n2browser = browser.window_handles[1]
    browser.switch_to.window(n2browser)
    xel = browser.find_element(By.ID, "input_value")
    x = xel.text
    y = calc(x)
    inputans = browser.find_element(By.ID, "answer")
    inputans.send_keys(y)
    firstbtn = browser.find_element(By.CLASS_NAME,"btn.btn-primary")
    firstbtn.click()
finally:
    time.sleep(30)
    browser.quit()