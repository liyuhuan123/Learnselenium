import time

from selenium import webdriver
import os
# 处理弹出框

driver = webdriver.Firefox()
file_path = 'file:///'+os.path.abspath("F:\selenium2html\selenium2html\Alert.html")
driver.get(file_path)
time.sleep(3)

# 定位点击按钮
driver.find_element_by_id("tooltip").click()
time.sleep(10)
# 得到操作alert弹出框的句柄
alert = driver.switch_to.alert()
# 输出弹出框的内容
text = alert.text
print("text="+text)
time.sleep()
# 关闭alert
alert.accept()

time.sleep(6)
driver.quit()