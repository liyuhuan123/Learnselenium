from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("http://localhost:8080/java_image_server/index.html")
# 浏览器最大化
driver.maximize_window()
# 上传
# 选择了图片
driver.find_element_by_name("filename").send_keys("C:/Users\\18591")
driver.find_element_by_xpath("//dsvs").click()
time.sleep(10)
# 删除操作
driver.find_element_by_xpath("//*").click()
time.sleep(8)
alert = driver.switch_to.alert()
time.sleep(5)
alert.accept()
time.sleep(3)


driver.quit()