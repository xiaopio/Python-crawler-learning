# __VIEWSTATE: /wEPDwUKLTU5OTg0MDIwNw8WAh4TVmFsaWRhdGVSZXF1ZXN0TW9kZQIBZGQGi0FCmPHMP+KelvQVsoBoqE2Axg==
# __VIEWSTATEGENERATOR: C93BE1AE
# from: http://www.gushiwen.cn/user/collect.aspx
# email: xxxxxxxxxx@qq.com
# pwd: 123456789
# code: 555
# denglu: 登录
import urllib.request

import requests
from bs4 import BeautifulSoup

# url = 'https://www.gushiwen.cn/user/login.aspx'
# post


url = 'https://www.gushiwen.cn/user/login.aspx?from=http://www.gushiwen.cn/user/collect.aspx'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36'
}

response = requests.get(url=url, headers=headers).text

soup = BeautifulSoup(response, 'lxml')

__VIEWSTATE = soup.select('#__VIEWSTATE')[0].attrs.get('value')

__VIEWSTATEGENERATOR = soup.select('#__VIEWSTATEGENERATOR')[0].attrs.get('value')

# print(__VIEWSTATE, __VIEWSTATEGENERATOR)

# 获取验证码图片
end = soup.select('#imgCode')[0].attrs.get('src')

code_url = 'https://www.gushiwen.cn' + end
print(code_url)

# urllib.request.urlretrieve(url=code_url, filename='code.jpg')
session = requests.session()
response_code = session.get(code_url)
content_code = response_code.content
with open('code.jpg', 'wb') as f:
    f.write(content_code)

import ddddocr

ocr = ddddocr.DdddOcr()

with open('code.jpg', 'rb') as f:
    img_bytes = f.read()

code = ocr.classification(img_bytes)
print(code)

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://www.gushiwen.cn',
    'priority': 'u=0, i',
    'referer': 'https://www.gushiwen.cn/user/login.aspx?from=http://www.gushiwen.cn/user/collect.aspx',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
    'cookie': 'ASP.NET_SessionId=lex5ujh204evvjvagorhypcc; wsEmail=xxxxxxxxxx%40qq.com; login=flase; gswZhanghao=xxxxxxxxxx%40qq.com; ticketStr=202934336%7cgQHX8DwAAAAAAAAAAS5odHRwOi8vd2VpeGluLnFxLmNvbS9xLzAyZkJNblJXbGVkN2kxd3ZfRXhFMVQAAgQfsoBoAwQAjScA; codeyz=661bb4d0bac398d6',
}

data = {
    '__VIEWSTATE': __VIEWSTATE,
    '__VIEWSTATEGENERATOR': __VIEWSTATEGENERATOR,
    'from': 'http://www.gushiwen.cn/user/collect.aspx',
    'email': 'xxxxxxxxx@qq.com',
    'pwd': '123456789',
    'code': code,
    'denglu': '登录',
}
print(data)
response_login = session.post(
    'https://www.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fwww.gushiwen.cn%2fuser%2fcollect.aspx',
    headers=headers,
    data=data,
)
content_login = response_login.text

with open('gushiwen.html', 'w', encoding='utf-8') as f:
    f.write(content_login)
