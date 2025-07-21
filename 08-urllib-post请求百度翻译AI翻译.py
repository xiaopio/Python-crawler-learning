# _*_ encoding: utf-8 _*_
"""
PyCharm 08-urllib-post请求百度翻译详细翻译
2025年07月19日 21时17分57秒
by LiXiaoYang
"""
import json
import time

import requests

word = input('请输入要翻译的单词:')

cookies = {
    'BAIDUID_BFESS': '2BBD3B22F423B61C4514D4C4E55993AC:FG=1',
    'BDUSS': 'Gh5Q2R6d3JpbHpHQUZtVm43WFZhVVJHYUJ1MEcwS2hvcnlzRmtOc0xNbFJLbkZvRVFBQUFBJCQAAAAAAQAAAAEAAADM3uRRbGl4aWFveWFuZzA1MDgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFGdSWhRnUloa',
    'BDUSS_BFESS': 'Gh5Q2R6d3JpbHpHQUZtVm43WFZhVVJHYUJ1MEcwS2hvcnlzRmtOc0xNbFJLbkZvRVFBQUFBJCQAAAAAAQAAAAEAAADM3uRRbGl4aWFveWFuZzA1MDgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFGdSWhRnUloa',
    'AIT_PERSONAL_VERSION': '1',
    'RT': '"z=1&dm=baidu.com&si=a2681223-77f3-46fa-ae93-0ffbcd1482bd&ss=mdb3wozd&sl=1&tt=1wf&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=2oo"',
}

headers = {
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Acs-Token': '1752948007050_1752981493496_vFoow/pfYE8dLfCC/h8OaHcMbZNn26ivjJwQKb8m2eCp3pKvHdDEl2bflYIbmlYIMn9gvtJ5qUvjQ7rtr+uAv3jjn+pNoHTYbiCrE62Uq6OSZfOj3eutpl+KvJeCA/GU4va9/vjqGmewyJdRgg+ZhLdAz/fFnhf/A1yRCwV6SWjbdYAPigv8rnKTGEP3fky4EUFu7ysKfhxm51yiRi/1Sb/D5MXxLegL1vnNjkOVd5SB9yMwDVVMGVPZCVENTkfqbm6tWeikNR7bWAauWauiV6ibCebNcyy8M877WxxyvK1HexGWcwxTlvuVrD2WClWDmX+PZEoKcwqpBWOheR0uc9VN6Ot94QCMi7qRzyFOlCaRJ/I7gLgRmGwTplW5Jtf7e7Zj2tkmayn/S4AsmUIsv1eD68++e1A6ZS7HS9/917ian8B1UcB/JZAxsUhO3PDJ',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Origin': 'https://fanyi.baidu.com',
    'Referer': 'https://fanyi.baidu.com/mtpe-individual/transText?query=hello&lang=en2zh',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
    'accept': 'text/event-stream',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Cookie': 'BAIDUID_BFESS=2BBD3B22F423B61C4514D4C4E55993AC:FG=1; BDUSS=Gh5Q2R6d3JpbHpHQUZtVm43WFZhVVJHYUJ1MEcwS2hvcnlzRmtOc0xNbFJLbkZvRVFBQUFBJCQAAAAAAQAAAAEAAADM3uRRbGl4aWFveWFuZzA1MDgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFGdSWhRnUloa; BDUSS_BFESS=Gh5Q2R6d3JpbHpHQUZtVm43WFZhVVJHYUJ1MEcwS2hvcnlzRmtOc0xNbFJLbkZvRVFBQUFBJCQAAAAAAQAAAAEAAADM3uRRbGl4aWFveWFuZzA1MDgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFGdSWhRnUloa; AIT_PERSONAL_VERSION=1; RT="z=1&dm=baidu.com&si=a2681223-77f3-46fa-ae93-0ffbcd1482bd&ss=mdb3wozd&sl=1&tt=1wf&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=2oo"',
}

json_data = {
    'query': f'{word}',
    'from': 'en',
    'to': 'zh',
    'reference': '',
    'corpusIds': [],
    'needPhonetic': False,
    'domain': 'ai_advanced',
    'milliTimestamp': int(time.time() * 1000),
}

response = requests.post('https://fanyi.baidu.com/ait/text/translate', cookies=cookies, headers=headers,
                         json=json_data)


def get_final_translation(response):
    for line in response.iter_lines():
        if line:
            data = line.decode('utf-8').strip()
            if data.startswith('data:'):
                event_data = json.loads(data[5:].strip())  # 移除"data:"前缀
                # print(event_data)
                # 捕获Translating事件
                # 检查是否为成功响应
                if event_data.get('errno') == 0:
                    event = event_data['data'].get('event')

                    # 提取Translating事件中的翻译结果
                    if event == 'Translating':
                        # 获取翻译结果（list[0]是第一个翻译项）
                        translation = event_data['data']['list'][0]['dst']
                        print(f"AI翻译结果: {translation}")  # 输出: 你好


get_final_translation(response)
