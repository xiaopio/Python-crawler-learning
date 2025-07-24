# _*_ encoding: utf-8 _*_
"""
PyCharm 搜狗翻译-带加密
2025年07月20日 09时33分54秒
by LiXiaoYang
"""
import hashlib
import requests

headers = {
    "Accept": "application/json, text/plain, */*",
    # "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Content-Length": "188",
    "Content-Type": "application/json;charset=UTF-8",
    "Cookie": "ABTEST=8|1752973182|v17; SNUID=71F604ADA6A09DF678791C96A7E7C374; SUID=D651A20B3D50A20B00000000687C3F7E; wuid=1752973182942; FQV=56879fb92d3fc2b3ad0986199957355c; translate.sess=f3fa023e-2ac6-4b9e-90ed-59f858db3cb4; SUV=1752973183311; SGINPUT_UPSCREEN=1752973183325",
    "Host": "fanyi.sogou.com",
    "Origin": "https://fanyi.sogou.com",
    "Referer": "https://fanyi.sogou.com/text?keyword=&transfrom=auto&transto=zh-CHS&model=general",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
    "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Google Chrome\";v=\"138\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}

url = 'https://fanyi.sogou.com/api/transpc/text/result'
word = input('请输入要查询的单词:')
key = f'autozh-CHS{word}109984457'

sign = hashlib.md5(key.encode('utf-8')).hexdigest()

json_data = {
    "from": "auto",
    "to": "zh-CHS",
    "text": word,
    "client": "pc",
    "fr": "browser_pc",
    "needQc": 1,
    "s": sign,
    "uuid": "9b06d349-d652-434f-b76f-05cec5a3503a",
    "exchange": False
}

response = requests.post(url=url, headers=headers, json=json_data).json()


# print(response)

def display_optimized_translation_result(data_dict):
    """显示优化后的翻译结果
    参数:
        data_dict (dict): 原始翻译结果字典
    """
    # 提取核心翻译信息
    translate = data_dict['data']['translate']
    print("\n=== 核心翻译结果 ===")
    print(f"翻译文本: {translate['text']}")
    print(f"中文释义: {translate['dit']}")
    print(f"来源语言: {translate['from']}")
    print(f"目标语言: {translate['to']}")
    # 提取音标与发音
    voice = data_dict['data']['voice']['phonetic']
    print("\n=== 音标与发音 ===")
    uk_phonetic = next((item for item in voice if item['type'] == 'uk'), {'text': 'N/A'})
    us_phonetic = next((item for item in voice if item['type'] == 'usa'), {'text': 'N/A'})
    print(f"英式音标: {uk_phonetic['text']}")
    print(f"美式音标: {us_phonetic['text']}")
    print(f"英式发音: {uk_phonetic.get('filename', 'N/A')}")
    print(f"美式发音: {us_phonetic.get('filename', 'N/A')}")
    # 提取基础释义
    word_card = data_dict['data']['wordCard']
    print("\n=== 基础释义 ===")
    for entry in word_card['usualDict']:
        pos = entry['pos']
        meanings = "; ".join(entry['values'])
        print(f"{pos}: {meanings}")


display_optimized_translation_result(response)
