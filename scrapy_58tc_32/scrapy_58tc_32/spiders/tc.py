import scrapy


class TcSpider(scrapy.Spider):
    name = "tc"
    allowed_domains = ["sh.58.com"]
    start_urls = ["https://sh.58.com/sou/jh_%E5%89%8D%E7%AB%AF%E5%BC%80%E5%8F%91/"]

    def start_requests(self):
        # 定义要添加的cookies
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Referer': 'https://ay.58.com/',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-site',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'Cookie': 'f=n; commontopbar_new_city_info=2%7C%E4%B8%8A%E6%B5%B7%7Csh; commontopbar_ipcity=ay%7C%E5%AE%89%E9%98%B3%7C0; f=n; spm=u-2gn98s8wb98zccv46g.2gn99j5y23vhwqfjjkg; 58home=ay; id58=d6HMAmiBjtZHb8MECADdAg==; 58tj_uuid=25db220a-08cc-49b5-8c33-c71867c8f856; new_uv=1; utm_source=; init_refer=https%253A%252F%252Fwww.google.com%252F; als=0; sessionid=a7558381-5f5e-43a0-ae0b-32a309edee26; new_session=0; hots=%5B%7B%22d%22%3A0%2C%22s1%22%3A%22%E5%89%8D%E7%AB%AF%E5%BC%80%E5%8F%91%22%2C%22s2%22%3A%22%22%2C%22n%22%3A%22sou%22%7D%5D; city=sh; f=n',
        }

        for url in self.start_urls:
            yield scrapy.Request(
                url=url,
                headers=headers,
                callback=self.parse
            )

    def parse(self, response):
        content = response.text
        print('=================================================================')
        print(content)
        print('=================================================================')
