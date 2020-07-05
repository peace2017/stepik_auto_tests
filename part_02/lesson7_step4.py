from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)
browser.execute_script("window.scrollBy(0, 100);")

x_element = browser.find_element_by_css_selector("#input_value")
x = x_element.text
y = calc(x)

button = browser.find_element_by_tag_name("button")
#browser.execute_script("return arguments[0].scrollIntoView(true);", button)


answer = browser.find_element_by_css_selector("#answer")
answer.send_keys(y)

robotCheckbox = browser.find_element_by_css_selector('[id="robotCheckbox"]')
robotCheckbox.click()

robotsRule = browser.find_element_by_css_selector('[id="robotsRule"]')
robotsRule.click()

button.click()
