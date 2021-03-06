# 下拉框定位
from selenium import webdriver
import os
import time

driver = webdriver.Firefox()
file_path = 'file:///'+os.path.abspath("F:\selenium2html\selenium2html\drop_down.html")
driver.get(file_path)

# # xpath定位
# driver.find_element_by_xpath("//*[@id='ShippingMethod']/option[4]").click()

# 用option定位
# lists = driver.find_element_by_tag_name("option")
# for list in lists:
#     if list.get_attribute("value") == '9.03':
#         list.click()

# 数组定位
lists = driver.find_element_by_tag_name("option")
lists[3].click()

time.sleep(8)
driver.quit()

