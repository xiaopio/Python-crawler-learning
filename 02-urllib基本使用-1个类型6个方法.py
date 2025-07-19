# _*_ encoding: utf-8 _*_
"""
PyCharm 01-urllib基本使用
2025年07月19日 16时16分44秒
by LiXiaoYang
"""
import urllib.request

# 定义url
url = "http://www.baidu.com"

# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(url)
# 将二进制数据转换为字符串
# decode(编码格式)
content = response.read().decode("UTF_8")

print(content)
