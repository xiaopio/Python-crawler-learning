# _*_ encoding: utf-8 _*_
"""
PyCharm 07-urllib-post请求百度翻译
2025年07月19日 20时45分22秒
by LiXiaoYang
"""
import json
import urllib.request
import urllib.parse

url = 'https://fanyi.baidu.com/sug'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0'
}

word = input('请输入要查询的单词:')

data = {
    'kw': word
}

# post请求的参数必须要进行编码
data = urllib.parse.urlencode(data).encode('utf-8')
# post请求的参数 不会拼接到url的后面 而是要放在请求对象定制的参数中
# post请求的参数必须进行编码
request = urllib.request.Request(url=url, data=data, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

# print(content)

json_obj = json.loads(content)

print(json_obj)
