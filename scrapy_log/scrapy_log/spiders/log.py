import scrapy


class LogSpider(scrapy.Spider):
    name = "log"
    allowed_domains = ["www.baidu.com"]
    start_urls = ["https://www.baidu.com"]

    def parse(self, response):
        print('++++++++++++++++++++++++++++')
