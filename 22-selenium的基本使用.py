

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# 配置浏览器选项
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
# 创建浏览器操作对象
path = 'chromedriver.exe'

service = Service(path)

browser = webdriver.Chrome(service=service, options=chrome_options)
# browser = webdriver.Chrome(service=service)

# 访问网站
url = 'https://miaosha.jd.com/'

browser.get(url)

content = browser.page_source

print(content)

