# _*_ encoding: utf-8 _*_
"""
PyCharm 04-urllib-请求对象的定制
2025年07月19日 16时50分39秒
by LiXiaoYang
"""

import urllib.request

url = 'https://www.baidu.com'

# url的组成
# http/https        www.baidu.com           80/443         s        wd = 周杰伦        #
# 协议                    主机                端口号         路径          参数          锚点

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0"
}
# 因为urlopen中不能存储字典 所以headers不能传递进去
# 请求对象定制
request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

print(content)
