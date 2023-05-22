from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#Отработка тестов только для обязательных полей ввода
try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    element1 = browser.find_element(By.XPATH, "//input[contains(@class, 'first') and @required]")
    element1.send_keys('test')
    element2 = browser.find_element(By.XPATH, "//input[contains(@class, 'second') and @required]")
    element2.send_keys('test')
    element3 = browser.find_element(By.XPATH, "//input[contains(@class, 'third') and @required]")
    element3.send_keys('test')

    button = browser.find_element(By.CLASS_NAME, "btn.btn-default")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")

    welcome_text = welcome_text_elt.text


    assert "Congratulations! You have successfully registered!" == welcome_text

finally:

    time.sleep(10)

    browser.quit()