from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

service = Service(executable_path='./chromedriver.exe')
opt = Options()

driver = webdriver.Chrome(options=opt, service=service)

with open('./stealth.min.js') as f:
    js = f.read()
driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
    'source': js
})

url = 'https://bot.sannysoft.com/'

driver.get(url)
