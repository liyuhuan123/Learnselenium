# 多层框架中的元素定位
from selenium import webdriver
import time
import os
driver = webdriver.Firefox()
file_path = 'file:///'+os.path.abspath("F:\selenium2html\selenium2html\Frame.html")
driver.get(file_path)
# driver.maximize_window()
# 从默认页面跳转到id=f2页面
driver.switch_to.frame("f1")
driver.switch_to.frame("f2")
driver.find_element_by_id("kw").send_keys("鼓浪屿")
driver.find_element_by_id("su").click()
time.sleep(5)

# 定位click元素,跳转到默认页面

driver.switch_to.default_content()  # 跳转到默认页面
driver.switch_to.frame("f1")  # 跳转到f1页面
driver.find_element_by_link_text("click").click()
time.sleep(6)
driver.quit()