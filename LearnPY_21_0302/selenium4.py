# 添加等待
# 固定等待:time.sleep(5) 设置几秒钟等待几秒钟
# 智能等待:implicitly_wait(6)等待的时间为0~6秒
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




