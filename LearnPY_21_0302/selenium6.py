# 浏览器的操作
from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("https://www.baidu.com/")
driver.find_element_by_id("kw").send_keys("奈雪の茶")
driver.find_element_by_id("su").submit()

# 浏览器的缩小
# driver.minimize_window()
# time.sleep(6)
# 浏览器的放大
# driver.maximize_window()
# time.sleep(6)
# 设置浏览器的宽和高(第一个参数是宽,第二个参数是高)
# driver.set_window_size(400,800)
# 控制浏览器的滚动条:通过js控制
# 控制浏览器的滚动条(最底端)
js = "var q=document.documentElement.scrollTop=100000"
driver.execute_script(js)
time.sleep(6)
# 控制浏览器的滚动条(最顶端)
js0 = "var q=document.documentElement.scrollTop=0"
driver.execute_script(js0)

