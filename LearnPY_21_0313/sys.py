from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("http://localhost:8080/sds/public/index.html")
# 浏览器最大化
driver.maximize_window()
# 登录
driver.find_element_by_name("username").send_keys("abc")
driver.find_element_by_name("password").send_keys("123")

div1 = driver.find_element_by_class_name("modal-content")
time.sleep(5)

div2 = driver.find_element_by_class_name("modal-footer")
buttons = div2.find_element_by_class_name("btn btn-secondary mr-auto").click()


driver.quit()
