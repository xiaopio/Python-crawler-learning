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

button = browser.find_element(By.ID, 'su')

print(button)
