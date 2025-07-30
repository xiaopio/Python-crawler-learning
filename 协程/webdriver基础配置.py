from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
import time


# 配置Chrome选项
chrome_options = Options()

# 基础配置
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-infobars")
chrome_options.add_experimental_option("detach", True)

# 隐藏自动化控制特征
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option("useAutomationExtension", False)

# 禁用自动化扩展
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")

# 配置用户代理，模拟真实浏览器
ua = UserAgent(platforms='desktop').random
chrome_options.add_argument(f"user-agent={ua}")
service = Service(r'../chromedriver.exe')

browser = webdriver.Chrome(service=service, options=chrome_options)

url = 'https://www.jd.com/'

browser.get(url)
time.sleep(2)
browser.refresh()
