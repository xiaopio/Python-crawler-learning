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

# 一个类型和六个方法
# HTTPResponse类型
# <class 'http.client.HTTPResponse'>
print(type(response))

# 按照一个字节一个字节去读
content = response.read()     # read方法数字代表返回多少个字节

print(response.readline())      # 读取一行

print(response.readlines())     # 读取全部

print(response.getcode())       # 返回状态码

print(response.geturl())        # 返回url地址

print(response.getheaders())    # 返回响应头，状态信息
