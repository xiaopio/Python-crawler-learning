import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

path = './chromedriver.exe'
service = Service(path)
options = Options()
options.add_experimental_option("detach", True)
browser = webdriver.Chrome(service=service, options=options)

url = 'https://baidu.com'

browser.get(url)

time.sleep(2)

_input = browser.find_element(By.ID, 'kw')
# 文本框输入周杰伦
_input.send_keys('周杰伦')

button = browser.find_element(By.ID, 'su')

button.click()

time.sleep(2)

# 滑到底部
js_bottom = 'document.documentElement.scrollTop=100000'

browser.execute_script(js_bottom)

time.sleep(2)

# 获取下一页的按钮
_next = browser.find_element(By.CLASS_NAME, 'n')

_next.click()

time.sleep(2)

browser.execute_script(js_bottom)

time.sleep(2)

browser.back()

time.sleep(2)

browser.forward()

browser.quit()
