# _*_ encoding: utf-8 _*_
"""
PyCharm 11-urllib-ajaxpost请求肯德基官网
2025年07月21日 14时55分54秒
by LiXiaoYang
"""

import urllib.request
import urllib.parse


def create_request(page):
    base_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
    data = {
        'cname': '北京',
        'pid': '',
        'pageIndex': page,
        'pageSize': '10'
    }

    data = urllib.parse.urlencode(data).encode('utf-8')

    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
    }

    request = urllib.request.Request(data=data, headers=headers, url=base_url)
    return request


def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content


def down_load(content, page):
    with open('KFC门店信息_' + str(page) + '.json', 'w', encoding='utf-8') as fd:
        fd.write(content)


if __name__ == '__main__':
    start_page = int(input("请输入起始页码:"))
    end_page = int(input("请输入结束页码:"))
    for page in range(start_page, end_page + 1):
        request = create_request(page)
        content = get_content(request)
        down_load(content, page)
