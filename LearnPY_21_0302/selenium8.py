# 鼠标事件
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Firefox()
driver.get("https://www.baidu.com/")

driver.find_element_by_id("kw").send_keys("书亦烧仙草")
driver.find_element_by_id("su").click()
# 键盘组合键的用法
# 复制
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'a')
# 剪贴
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'x')

time.sleep(6)
driver.find_element_by_id("kw").send_keys("茶颜悦色")
driver.find_element_by_id("su").click()

# 右击
# 第一步,先定位到要右击的元素
# 定位百度一下按钮
sul = driver.find_element_by_id("su")
# 右击
ActionChains(driver).context_click(sul).perform()
time.sleep(6)

# 双击(网页上双击和单击的效果是一样的)
ActionChains(driver).double_click(sul).perform()
time.sleep(6)

title = driver.find_element_by_id("su")
target = driver.find_element_by_link_text("茶颜悦色 - 百度百科")
# 拖动
ActionChains(driver).drag_and_drop(title, target).perform()

# 移动
ActionChains(driver).move_to_element(target).perform()


time.sleep(6)
driver.quit()