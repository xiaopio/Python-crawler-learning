# _*_ encoding: utf-8 _*_
"""
PyCharm 05-urllib-get请求和quote方法.py
2025年07月19日 17时10分15秒
by LiXiaoYang
"""

import urllib.request

import urllib.parse

# https://www.baidu.com/s?wd=%E5%91%A8%E6%9D%B0%E4%BC%A6
word = urllib.parse.quote("毛不易")
url = f'https://www.baidu.com/s?wd={word}'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0"
}

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

print(content)
