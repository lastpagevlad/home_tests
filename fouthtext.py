import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = 'http://suninjuly.github.io/find_link_text'
try:
    browser = webdriver.Chrome()
    browser.get(link)
    inputlink = browser.find_element(By.PARTIAL_LINK_TEXT, value=str(math.ceil(math.pow(math.pi, math.e)*10000)))
    inputlink.click()
    input1 = browser.find_element(By.NAME, value='first_name')
    input1.send_keys('Test')
    input2 = browser.find_element(By.NAME, value='last_name')
    input2.send_keys('Test')
    input3 = browser.find_element(By.CLASS_NAME, "form-control.city")
    input3.send_keys('Test')
    input4 = browser.find_element(By.ID, 'country')
    input4.send_keys('Test')
    button = browser.find_element(By.CLASS_NAME, "btn.btn-default")
    button.click()
finally:
    time.sleep(30)
    browser.quit()