from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

service = Service('./chromedriver107.exe')
opt = Options()
opt.debugger_address = '127.0.0.1:8888'

browser = webdriver.Chrome(service=service, options=opt)

url = 'https://www.jd.com/'

browser.get(url)
