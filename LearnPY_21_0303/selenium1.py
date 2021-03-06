from selenium import webdriver
import time
import os
driver = webdriver.Firefox()
file_path = 'file:///'+os.path.abspath("F:\selenium2html\selenium2html\checkbox.html")
driver.get(file_path)
# driver.maximize_window()
# 定位一组元素
inputs = driver.find_elements_by_tag_name("input")
time.sleep(6)
for input in inputs:
    if input.get_attribute('type') == "checkbox":
        input.click()
time.sleep(6)

driver.quit()