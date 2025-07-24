# _*_ encoding: utf-8 _*_
"""
PyCharm 搜狗翻译
2025年07月20日 09时00分53秒
by LiXiaoYang
"""
import json
import urllib.request
import urllib.parse

word = input('请输入你要查询的单词:')

url = 'https://fanyi.sogou.com/reventondc/suggV3'

data = {
    'from': 'auto',
    'to': 'zh-CHS',
    'client': 'web',
    'text': f'{word}',
    'uuid': '9b06d349-d652-434f-b76f-05cec5a3503a',
    'pid': 'sogou-dict-vr',
    'addSugg': 'on'
}

headers = {
    "Cookie": "ABTEST=8|1752973182|v17; SNUID=71F604ADA6A09DF678791C96A7E7C374; SUID=D651A20B3D50A20B00000000687C3F7E; wuid=1752973182942; FQV=56879fb92d3fc2b3ad0986199957355c; translate.sess=f3fa023e-2ac6-4b9e-90ed-59f858db3cb4; SUV=1752973183311; SGINPUT_UPSCREEN=1752973183325",
    "Host": "fanyi.sogou.com",
    "Origin": "https://fanyi.sogou.com",
    "Referer": "https://fanyi.sogou.com/text?keyword=&transfrom=auto&transto=zh-CHS&model=general",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",

}

data = urllib.parse.urlencode(data).encode('utf-8')

request = urllib.request.Request(url=url, data=data, headers=headers)
response = urllib.request.urlopen(request)
# {"zly":"zly","message":"success","code":0,"uuid":"9b06d349-d652-434f-b76f-05cec5a3503a","sugg":[{"k":"love","v":"n.爱；爱情；恋爱；喜爱；热爱；爱好；喜好；所爱之物；所爱之人；（昵称）亲爱的；（网球等运动中）零分；无分"},{"k":"loved","v":"vt.爱；爱慕；喜欢；热爱；（love的过去式和过去分词）"},{"k":"loves","v":"vt.爱；爱慕；喜欢；热爱；（love的第三人称单数）"},{"k":"lovely","v":"adj.可爱的；迷人的；美丽的；优美的；美好的；令人愉快的；令人喜悦的；悦目的；令人赏心悦目的；有吸引力的；吸引人的；极好的；宜人的；动人的"},{"k":"lover","v":"n.情人；恋人；爱人；热爱者；爱好者；嗜好者；迷；粉丝；拥护者；支持者"},{"k":"lovers","v":"n.情侣；情人；（lover的复数）"},{"k":"loved ones","v":"亲人；爱人；心爱的人"},{"k":"love story","v":"n.爱情故事（指小说、电影等）；恋爱故事"},{"k":"love life","v":"n.爱情生活；情感生活；感情经历"},{"k":"love affair","v":"n.风流韵事；恋爱关系；风流事；私情；婚外情；情事"}],"direction":"en#zh-CHS"}
content = response.read().decode('utf-8')


def parse_and_display_translation(json_data):
    """解析并美观地展示翻译结果"""
    try:
        # 解析JSON数据
        data = json.loads(json_data)

        # 检查是否有建议翻译
        if 'sugg' in data and len(data['sugg']) > 0:
            print("\n===== 搜狗翻译结果 =====")
            print(f"翻译方向: {data['direction'].replace('#', ' → ')}\n")

            # 计算最长的英文单词长度，用于对齐显示
            max_key_length = max(len(item['k']) for item in data['sugg'])

            # 遍历每个建议翻译并格式化输出
            for item in data['sugg']:
                word = item['k']
                definition = item['v']

                # 按中文分号分割多个释义
                meanings = definition.split('；')

                # 打印英文单词和词性
                print(f"{word.ljust(max_key_length)}  {meanings[0]}")

                # 打印其他释义（缩进对齐）
                for meaning in meanings[1:]:
                    print(f"{'':{max_key_length}}  {meaning}")

                print()  # 空行分隔不同单词
        else:
            print("未找到翻译结果。")

    except json.JSONDecodeError as e:
        print(f"JSON解析错误: {e}")
    except Exception as e:
        print(f"处理结果时出错: {e}")


parse_and_display_translation(content)
