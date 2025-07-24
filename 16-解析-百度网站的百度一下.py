import urllib.request

from lxml import etree

url = "https://www.baidu.com"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0'
}

# 请求对象的定制

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

# 解析网页源码,获取想要的数据
# 解析服务器响应的文件
tree = etree.HTML(content)
# xpath的返回值是一个列表类型的数据
result = tree.xpath('//input[@id="su"]/@value')[0]
# 百度一下
print(result)
