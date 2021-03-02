# 操作测试对象
from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("https://www.baidu.com/")
driver.find_element_by_id("kw").send_keys("奈雪の茶")
# submit 提交 == 点击
# 注意:只有当元素中的type属性里面有submit的时候才能用submit
# driver.find_element_by_id("su").submit()
# time.sleep(6)
# 清除百度搜索框的内容,如果可以的话
# driver.find_element_by_id("kw").clear()
# send_keys在对象上模拟按键输入
# driver.find_element_by_id("kw").send_keys("鹿角巷")
# click:点击对象
# driver.find_element_by_id("su").click()
# text:获取文本信息
text = driver.find_element_by_id("s-bottom-layer-right").text
print("text:"+text)
