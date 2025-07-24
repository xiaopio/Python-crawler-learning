import requests
from bs4 import BeautifulSoup

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Referer': 'https://www.mcdonalds.com.cn/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Cookie': 'ARRAffinity=fdc7d01ba77124143f2abb7a519902f451a3c5edf28da525b2ec8cdada4adeff; ARRAffinitySameSite=fdc7d01ba77124143f2abb7a519902f451a3c5edf28da525b2ec8cdada4adeff',
}

response = requests.get('https://www.mcdonalds.com.cn/index/Food/menu/burger', headers=headers).text

soup = BeautifulSoup(response, 'lxml')

food_list = soup.select('div[class="col-md-3 col-sm-4 col-xs-6"] a span')

for name in food_list:
    print(name.get_text())
