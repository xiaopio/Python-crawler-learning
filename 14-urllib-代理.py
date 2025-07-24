import urllib.request

url = 'http://www.baidu.com/s?wd=ip'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36'
}

request = urllib.request.Request(url=url, headers=headers)

proxies = {
    'http': '43.156.183.112:1080'
}

# 获取handler对象
handler = urllib.request.ProxyHandler(proxies=proxies)

# 获取opener对象
opener = urllib.request.build_opener(handler)

# 调用open方法
response = opener.open(request)

content = response.read().decode('utf-8')

with open('ip.html', 'w', encoding='utf-8') as fd:
    fd.write(content)
