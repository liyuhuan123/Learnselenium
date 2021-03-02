# coding = UTF-8
from selenium import webdriver
import time
browser = webdriver.Firefox()
time.sleep(3)
browser.get("http://www.baidu.com")
time.sleep(3)
browser.find_element_by_id("kw").send_keys("益禾堂")
time.sleep(3)
browser.find_element_by_id("su").click()
browser.quit()