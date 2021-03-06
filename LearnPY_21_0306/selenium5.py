# 上传文件操作
from selenium import webdriver
import time
import os

driver = webdriver.Firefox()
file_path = 'file:///'+os.path.abspath("F:\selenium2html\selenium2html\upload.html")
driver.get(file_path)
time.sleep(7)

# 定位上传文件按钮
driver.find_element_by_tag_name("input").send_keys("F:\String");

time.sleep(5)
driver.quit()