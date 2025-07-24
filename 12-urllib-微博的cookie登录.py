# 适用场景:数据采集的时候需要绕过登录 然后进入到某个页面

import urllib.request

url = 'https://weibo.cn/7636718951/info'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0',
    'cookie': '_T_WM=11136315052; SCF=AmD-T_m6V75D-Zmaumf8dDQlOCtWc7Fbja4pLIHpGPZ8I9TP-P0seppbNTzdXahDVwdz0H3cjTddG4HboFPy9xM.; SUB=_2A25Fem1tDeRhGeFI6FQW8SbFzj2IHXVm9uClrDV6PUJbktANLVinkW1NfTMBRWoT5fWywryDZUm823SVpqsgO1C5; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5ohUKBETAQsPZq2_4j2Rg-5NHD95QNSoecS02R1K-pWs4Dqcjni--NiKyhi-8Wi--fi-88iKL2i--fi-88iKL2qgifMc-t; SSOLoginState=1753095485; ALF=1755687485; MLOGIN=1; M_WEIBOCN_PARAMS=lfid%3D102803%26luicode%3D20000174',
}

requset = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(requset)

content = response.read().decode('utf-8')
# 报错:HTTP Error 403
# print(content)

with open('weibo.html', 'w', encoding='utf-8') as fd:
    fd.write(content)

# import requests
#
# headers = {
#     'sec-ch-ua-platform': '"Windows"',
#     'X-XSRF-TOKEN': 'fb9337',
#     'Referer': 'https://m.weibo.cn/profile/6384589361?user_token=a0.MTg1ZGEwZWU0OWVhNGQyY9g6uRE06Vo6gD7L0RFmTuRAdkGtxB1JR0FfcEVCqxFC',
#     'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Microsoft Edge";v="138"',
#     'sec-ch-ua-mobile': '?0',
#     'MWeibo-Pwa': '1',
#     'X-Requested-With': 'XMLHttpRequest',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0',
#     'Accept': 'application/json, text/plain, */*',
#     'x-h5-user-token': 'a0.MTg1ZGEwZWU0OWVhNGQyY9g6uRE06Vo6gD7L0RFmTuRAdkGtxB1JR0FfcEVCqxFC',
# }
#
# params = {
#     'uid': '6384589361',
# }
#
# response = requests.get('https://m.weibo.cn/profile/info', params=params, headers=headers).json()
# # {'ok': 0, 'errno': '100006', 'msg': '请求非法', 'extra': None}
# print(response)
