from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element_by_css_selector("#input_value")
x = x_element.text
y = calc(x)

answer = browser.find_element_by_css_selector("#answer")
answer.send_keys(y)

robotCheckbox = browser.find_element_by_css_selector('[id="robotCheckbox"]')
robotCheckbox.click()

robotsRule = browser.find_element_by_css_selector('[id="robotsRule"]')
robotsRule.click()

# Отправляем заполненную форму
button = browser.find_element_by_css_selector("button.btn.btn-default")
button.click()
