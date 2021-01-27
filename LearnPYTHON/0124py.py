from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("https://www.baidu.com/")
# 浏览器的最大化
# driver.maximize_window()
#
# driver.find_element_by_id("kw").send_keys("蜜雪冰城")
# # submit 提交 == 点击 (前提条件:元素里面有submit这个属性)
# driver.find_element_by_id("su").submit()
#
# time.sleep(6)
#
# # 清除百度搜索框的内容
# driver.find_element_by_id("kw").clear()
# 输出元素的文本信息
# text = driver.find_element_by_id("s-bottom-layer-right")
# print("text:"+text)
driver.find_element_by_id("kw").send_keys("益禾堂")
driver.find_element_by_id("su").submit()
# 脚本执行的速度要比页面加载速度快,所以如果不加就会报错
# 固定等待
# time.sleep(10)
# 智能等待
driver.implicitly_wait(10)
driver.find_element_by_link_text("益禾堂 - 百度百科").click()


driver.find_element_by_id("kw").send_keys("书亦烧仙草")
driver.find_element_by_id("su").click()

# 打印title
title = driver.title
print("title:"+title)

# 打印current url  注意:打印的是上一个页面的url
url = driver.current_url
print("url="+url)

# 浏览器的缩小
driver.minimize_window()
time.sleep(6)
# 浏览器的放大
driver.maximize_window()
time.sleep(6)
# 设置浏览器的宽和高(宽,高)
driver.set_window_size(400,800)
time.sleep(6)
# 控制浏览器的滚动条:是通过js控制的
# 浏览器的滚动条拖动到最底端
js = "var q=document.documentElement.scrollTop=100000"
time.sleep(6)
driver.execute_script(js)
# 浏览器的滚动条拖动到最顶端
js0 = "var q=document.documentElement.scrollTop=0"
driver.execute_script(js0)

time.sleep(6)
driver.quit()

