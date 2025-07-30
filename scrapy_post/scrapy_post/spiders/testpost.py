import json

import scrapy


class TestpostSpider(scrapy.Spider):
    name = "testpost"
    allowed_domains = ["fanyi.baidu.com"]

    # start_urls = ["https://fanyi.baidu.com/sug"]
    #
    # def parse(self, response):
    #     pass
    def start_requests(self):
        kw = input("请输入要查询的单词:")
        url = 'https://fanyi.baidu.com/sug'

        data = {
            'kw': kw
        }

        yield scrapy.FormRequest(url=url, formdata=data, callback=self.parse_second)

    def parse_second(self, response):
        content = response.text
        obj = json.loads(content)
        print(obj)
