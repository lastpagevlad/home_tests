from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time
#Работа с загружаемыми файлами, с помощью получения пути к файлу и указания этого пути в передачу sendKeys
link = "http://suninjuly.github.io/file_input.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    inputname = browser.find_element(By.NAME,"firstname")
    inputname.send_keys('test')
    inputsurname = browser.find_element(By.NAME, "lastname")
    inputsurname.send_keys("test")
    inputmail = browser.find_element(By.NAME,"email")
    inputmail.send_keys('test')
    currentdir = os.path.abspath(os.path.dirname(__file__))
    filep = os.path.join(currentdir,'12.txt')
    filecheck = browser.find_element(By.NAME,'file')
    filecheck.send_keys(filep)
    btn = browser.find_element(By.CLASS_NAME,"btn.btn-default")
    btn.click()
finally:
    time.sleep(30)
    browser.quit()