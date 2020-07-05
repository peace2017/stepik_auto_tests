import os
from selenium import webdriver

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)


First_name = browser.find_element_by_css_selector('[placeholder="Enter first name"]')
First_name.send_keys("Ivan")

Last_name = browser.find_element_by_css_selector('[placeholder="Enter last name"]')
Last_name.send_keys("Ivan")

Email = browser.find_element_by_css_selector('[placeholder="Enter email"]')
Email.send_keys("Ivan@ivan.ru")

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
File = browser.find_element_by_css_selector("#file")
File.send_keys(file_path)

button = browser.find_element_by_tag_name("button")
button.click()

