import scrapy


class MdlSpider(scrapy.Spider):
    name = "mdl"
    allowed_domains = ["www.mcdonalds.com.cn"]
    start_urls = ["https://www.mcdonalds.com.cn/index/Food/menu/burger"]

    def parse(self, response):
        content = response.text
        print('===========================================')
        print(content)
        print('===========================================')
        name_list = response.xpath('//div[@class="col-md-3 col-sm-4 col-xs-6"]//span[@class="name"]/text()').getall()
        for name in name_list:
            print(name + ' ', end='')
        print('\n' + '===========================================')
