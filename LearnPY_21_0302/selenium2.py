# 元素的定位
from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("https://www.baidu.com/")
# 最大化浏览器
# driver.maximize_window()
# id定位
# driver.find_element_by_id("kw").send_keys("蜜雪冰城")
# driver.find_element_by_id("su").click()
# name定位
# driver.find_element_by_name("wd").send_keys("益禾堂")
# driver.find_element_by_id("su").click()
# class name定位
# driver.find_element_by_class_name("s_ipt").send_keys("一點點")
# driver.find_element_by_id("su").click()
# link text定位
# driver.find_element_by_link_text(u"视频").click()
# 部分链接定位
# driver.find_element_by_partial_link_text(u"澳大利亚").click()
# tag name定位(因为input标签不唯一,所以定位不到)
# driver.find_element_by_tag_name("input").send_keys("书亦烧仙草")
# driver.find_element_by_id("su").click()
# xpath定位(找xpath:右击搜索框,右击选择copy,选择xpath复制粘贴即可)
# driver.find_element_by_xpath("//*[@id='kw']").send_keys("喜茶")
# driver.find_element_by_xpath("//*[@id='su']").click()
# css定位
driver.find_element_by_css_selector("#kw").send_keys("星巴克")
driver.find_element_by_css_selector("#su").click()









