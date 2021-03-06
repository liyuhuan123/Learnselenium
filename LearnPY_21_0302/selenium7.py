# 键盘事件
from selenium import webdriver
import time

from selenium.webdriver.common import keys
from selenium.webdriver.common.action_chains import ActionChains
import os

driver = webdriver.Firefox()
driver.get("http://127.0.0.1:88/biz/user-login.html")
driver.maximize_window()
# 输入用户名
driver.find_element_by_name("account").send_keys("admin")
# 用Tab键把光标移动到密码输入框
driver.find_element_by_name("account").send_keys(keys.TAB)
time.sleep(6)
driver.find_element_by_name("password").send_keys("123456")
# 定位登录按钮,点击
driver.find_element_by_name("password").send_keys(keys.ENTER)
time.sleep(6)
# 注意:例如网易邮箱不能用id去定位,因为每次点击进去它的id是会发生变化的

# 键盘组合键的用法
# 复制
driver.find_element_by_id("kw").send_keys(keys.CONTROL,'a')
# 剪贴
driver.find_element_by_id("kw").send_keys(keys.CONTROL,'x')

driver.sleep(4)
driver.find_element_by_id("kw").send_keys("一點點")
driver.find_element_by_id("su").click()

time.sleep(6)
driver.quit()
