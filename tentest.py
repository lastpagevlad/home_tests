from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math
#Использование селектов у выпадающих списков
#Использование библиотеки Select
try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element(By.ID, "num1")
    y = browser.find_element(By.ID,"num2")
    x1 = x.text
    y1 = y.text
    f = int(x1)+int(y1)
    print(f)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(f))
    button = browser.find_element(By.CLASS_NAME,"btn.btn-default")
    button.click()
finally:
    time.sleep(30)
    browser.quit()