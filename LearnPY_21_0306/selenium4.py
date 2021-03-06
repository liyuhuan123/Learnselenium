# div对话框的处理
from selenium import webdriver
import time
import os
driver = webdriver.Firefox()
file_path = 'file:///'+os.path.abspath("F:\selenium2html\selenium2html\modal.html")
driver.get(file_path)
# 点击click
driver.find_element_by_id("show_modal").click()
time.sleep(10)
# 定位modal-body
div1 = driver.find_element_by_class_name("modal-body")
driver.find_element_by_link_text("click me").click()
time.sleep(5)
# 定位modal-footer
div2 = driver.find_element_by_class_name("modal-footer")
buttons = div2.find_element_by_tag_name("button")
buttons[0].click()

driver.quit()