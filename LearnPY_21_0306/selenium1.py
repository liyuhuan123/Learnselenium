# 层级定位
from selenium import webdriver
import time
import os

from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
file_path = 'file:///'+os.path.abspath("F:\selenium2html\selenium2html\level_locate.html")
driver.get(file_path)

# 定位link1
driver.find_element_by_link_text("Link1").click()
# 定位需要鼠标移动的目标元素
btn = driver.find_element_by_link_text("Another action")
# 将鼠标移动到目标元素
ActionChains(driver).move_to_element(btn).perform()

time.sleep(10)
driver.quit()