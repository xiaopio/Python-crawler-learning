import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

path = './phantomjs.exe'
service = Service(path)
# options = Options()
# options.add_experimental_option("detach", True)
browser = webdriver.PhantomJS(path)

url = 'https://baidu.com'

browser.get(url)

