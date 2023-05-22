from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
#подтверждение всплывающего окна и нажатие кнопки на другой странице
link = "http://suninjuly.github.io/alert_accept.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    firstbtn = browser.find_element(By.CLASS_NAME,"btn.btn-primary")
    firstbtn.click()
    confirm = browser.switch_to.alert
    confirm.accept()
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