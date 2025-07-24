import json

import jsonpath
import requests

headers = {
    'referer': 'https://dianying.taobao.com/?spm=a1z21.3046609.city.11.5e55112aTR54TQ&city=610100',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
    'cookie': 't=f8008c73df4bf54c916181b30d246d6a; cookie2=1f5e492f2b23050ac5b66c3e10cb8e4c; v=0; _tb_token_=537e057f3e13; cna=Ey0GIdMV7X4BASQJikSgQI/J; tb_city=610100; tb_cityName="zvewsg=="; isg=BMfHK_-sYyGjseettvcK8M9zVnuRzJuuS-txyZm0PNZ9COfKoZ3w_krGqshW53Mm',
}

# response = requests.get(
#     'https://dianying.taobao.com/cityAction.json?activityId&_ksTS=1753171553110_104&jsoncallback=jsonp105&action=cityAction&n_s=new&event_submit_doGetAllRegion=true',
#     headers=headers,
# ).text
# result = response.split('(')[1].split(")")[0]

# with open('taopiaopiao.json', 'w', encoding='utf-8') as fp:
#     fp.write(result)

obj = json.load(open('./taopiaopiao.json', 'r', encoding='utf-8'))

regionName_list = jsonpath.jsonpath(obj, '$..regionName')

print(regionName_list)
