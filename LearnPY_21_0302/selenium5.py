# 打印信息
from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("https://www.baidu.com/")
driver.find_element_by_id("kw").send_keys("奈雪の茶")
driver.find_element_by_id("su").submit()
# 如果不加等待的话会报错,因为代码执行的速率大于页面加载的速率
# 固定等待10秒
# time.sleep(10)
# 智能等待
driver.implicitly_wait(10)
driver.find_element_by_link_text("奈雪的茶 - 百度百科").click()

# 打印title
title = driver.title
print("title:" + title)
# 打印url
url = driver.current_url
print("url:" + url)




