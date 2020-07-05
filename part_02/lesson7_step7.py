import math
from selenium import webdriver

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

button = browser.find_element_by_tag_name("button")
button.click()

first_window = browser.window_handles[0]
second_window = browser.window_handles[1]
browser.switch_to.window(second_window)

x_element = browser.find_element_by_css_selector("#input_value")
x = x_element.text
y = calc(x)

answer = browser.find_element_by_css_selector("#answer")
answer.send_keys(y)

button = browser.find_element_by_tag_name("button")
button.click()
