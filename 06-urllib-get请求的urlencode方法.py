# _*_ encoding: utf-8 _*_
"""
PyCharm 06-urllib-get请求的urlencode方法
2025年07月19日 20时28分54秒
by LiXiaoYang
"""
import urllib.parse
import urllib.request
import urllib.response

# 应用场景, 多个参数

# https://www.baidu.com/s?wd=周杰伦&sex=男

data = {
    'wd': '周杰伦',
    'sex': '男',
    'location': '中国台湾'
}

# wd=%E5%91%A8%E6%9D%B0%E4%BC%A6&sex=%E7%94%B7&location=%E4%B8%AD%E5%9B%BD%E5%8F%B0%E6%B9%BE
url = f'https://www.baidu.com/s?{urllib.parse.urlencode(data)}'

print(url)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0"
}

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

print(content)
