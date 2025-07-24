# _*_ encoding: utf-8 _*_
"""
PyCharm 09-urllib-ajaxget请求豆瓣电影第一页
2025年07月21日 09时17分11秒
by LiXiaoYang
"""

import urllib.request

url = "https://movie.douban.com/j/chart/top_list?type=17&interval_id=100%3A90&action=&start=0&limit=20"

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
}

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode("utf-8")

print(content)

# open方法默认使用GBK编码，所以需要指定utf-8编码来正确写入中文内容
# fp = open("douban.json", "w", encoding="utf-8")

# fp.write(content)

with open("./douban.json", "w", encoding="utf-8") as fp:
    fp.write(content)
