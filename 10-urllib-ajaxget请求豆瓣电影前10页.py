# https://movie.douban.com/j/chart/top_list?
# type=17&interval_id=100%3A90&action=&start=0&limit=20
# _*_ encoding: utf-8 _*_
"""
PyCharm 09-urllib-ajaxget请求豆瓣电影第一页
2025年07月21日 09时17分11秒
by LiXiaoYang
"""
import time
import urllib.parse
import urllib.request


def create_request(page):
    url = f"https://movie.douban.com/j/chart/top_list?"
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
    }

    data = {
        'type': '17',
        'interval_id': '100:90',
        'action': '',
        'start': (page - 1) * 20,
        'limit': '20',
    }
    data = urllib.parse.urlencode(data)
    url = url + data
    return urllib.request.Request(url=url, headers=headers)


def get_content(request):
    response = urllib.request.urlopen(request)
    return response.read().decode('utf-8')


def down_load(page, content):
    with open('douban_' + str(page) + '.json', 'w', encoding='utf-8') as fp:
        fp.write(content)


if __name__ == '__main__':
    start = int(input("请输入起始页码:"))
    end = int(input("请输入结束页码:"))
    for page in range(start, end + 1):
        # print(page)
        request = create_request(page)
        content = get_content(request)

        time.sleep(2)
        down_load(page, content)
