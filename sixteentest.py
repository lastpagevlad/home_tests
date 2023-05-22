import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
#Настройка ожидания появления элемента
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")
bax = WebDriverWait(browser,12).until(
    EC.text_to_be_present_in_element((By.ID,'price'),'$100')
)
#
btn = browser.find_element(By.ID,'book')
btn.click()

value = browser.find_element(By.ID,'input_value')
x = value.text
y = calc(x)
ans = browser.find_element(By.ID,'answer')
ans.send_keys(y)
time.sleep(30)
browser.quit()