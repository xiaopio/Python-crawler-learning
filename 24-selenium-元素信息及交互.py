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

input = browser.find_element(By.ID, 'su')

print(input.get_attribute('class'))

print(input.tag_name)

a = browser.find_element(By.LINK_TEXT, '新闻')
# 获取尖括号里面的内容
# 新闻
print(a.text)


