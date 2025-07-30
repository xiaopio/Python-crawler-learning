import os.path
import random
import time

import requests
from lxml import etree

headers = {
    'Referer': 'https://www.hongxiu.com/book/22292070000065702',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
    'Cookie': '_csrfToken=O3VGt7YDJwalKUslvVpMfyovX5ogE2ej2TYxDNSl; newstatisticUUID=1753621715_884316790; fuid=688624d3807ff; traffic_utm_referer=; landing_page=/; qdrs=0%7C3%7C0%7C0%7C2; qdgd=1',
}

response = requests.get('https://www.hongxiu.com/book/23319469809201404', headers=headers).text
tree = etree.HTML(response)
url_list = tree.xpath('//div[@class="volume"]/ul/li/a/@href')
book_title = tree.xpath('//h1/text()')[0]
if not os.path.exists(f'./{book_title}'):
    os.makedirs(f'./{book_title}')
# print(url_list)
index = 1
for url in url_list:
    url = 'https://www.hongxiu.com' + url
    # print(url)
    time.sleep(random.randint(1, 3))
    re = requests.get(url, headers=headers).text
    tree = etree.HTML(re)

    result = tree.xpath('//div[@class="ywskythunderfont"]/p/text()')
    title = tree.xpath('//h1[@class="j_chapterName"]/text()')[0]
    with open(f'./{book_title}/{index}_{title}.txt', 'a', encoding='utf-8') as f:
        for r in result:
            r = r.replace('\u3000\u3000', '')
            f.write(r)
            f.write('\n')
    index += 1
    print(result)
