import time

from selenium import webdriver
from selenium.webdriver.common.by import By
link = "http://suninjuly.github.io/find_xpath_form"
#Работа с XPATH
try:
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element(By.XPATH,'//input[@name="first_name"]')
    input1.send_keys('Test')
    input2 = browser.find_element(By.XPATH,'//input[@name="last_name"]')
    input2.send_keys('Test')
    input3 = browser.find_element(By.XPATH,'//input[@class="form-control city"]')
    input3.send_keys('Test')
    input4 = browser.find_element(By.XPATH,'//input[@id="country"]')
    input4.send_keys('Test')
    button = browser.find_element(By.XPATH,'//button[contains(text(),"Submit")]')
    button.click()
finally:
    time.sleep(30)
    browser.quit()