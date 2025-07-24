# _*_ encoding: utf-8 _*_
"""
PyCharm test
2025年07月20日 11时08分41秒
by LiXiaoYang
"""
import hashlib

import requests

word = input('请输入要查询的单词:')
key = f'autozh-CHS{word}109984457'

sign = hashlib.md5(key.encode('utf-8')).hexdigest()

cookies = {
    'ABTEST': '8|1752973182|v17',
    'SNUID': '71F604ADA6A09DF678791C96A7E7C374',
    'SUID': 'D651A20B3D50A20B00000000687C3F7E',
    'wuid': '1752973182942',
    'FQV': '56879fb92d3fc2b3ad0986199957355c',
    'translate.sess': 'f3fa023e-2ac6-4b9e-90ed-59f858db3cb4',
    'SUV': '1752973183311',
    'SGINPUT_UPSCREEN': '1752973183325',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=UTF-8',
    'Origin': 'https://fanyi.sogou.com',
    'Referer': 'https://fanyi.sogou.com/text',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Cookie': 'ABTEST=8|1752973182|v17; SNUID=71F604ADA6A09DF678791C96A7E7C374; SUID=D651A20B3D50A20B00000000687C3F7E; wuid=1752973182942; FQV=56879fb92d3fc2b3ad0986199957355c; translate.sess=f3fa023e-2ac6-4b9e-90ed-59f858db3cb4; SUV=1752973183311; SGINPUT_UPSCREEN=1752973183325',
}

json_data = {
    'from': 'auto',
    'to': 'zh-CHS',
    'text': 'hello',
    'client': 'pc',
    'fr': 'browser_pc',
    'needQc': 1,
    's': sign,
    'uuid': '95ba0951-8bbc-48e4-a0c8-b33558d11df8',
    'exchange': False,
}



response = requests.post('https://fanyi.sogou.com/api/transpc/text/result', cookies=cookies, headers=headers,
                         json=json_data).json()

print(type(response))
