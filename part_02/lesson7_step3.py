from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

num1 = browser.find_element_by_css_selector("#num1")
num1 = int(num1.text)

num2 = browser.find_element_by_css_selector("#num2")
num2 = int(num2.text)

sum_num = str(num1 + num2)

select = Select(browser.find_element_by_css_selector(".custom-select"))
select.select_by_value(sum_num)  # ищем элемент с текстом "Python"

# Отправляем заполненную форму
button = browser.find_element_by_css_selector("button.btn.btn-default")
button.click()
