import scrapy


class CarSpider(scrapy.Spider):
    name = "car"
    allowed_domains = ["www.autohome.com.cn"]
    start_urls = ["https://www.autohome.com.cn/rank/1-1-0-0_9000-x-x-x/2025-06.html"]

    def parse(self, response):
        name_list = response.xpath(
            '//div[@class="tw-text-nowrap tw-text-lg tw-font-medium hover:tw-text-[#ff6600]"]/text()').getall()
        price_list = response.xpath('//div[@class=" tw-font-medium tw-text-[#717887]"]/text()').getall()
        score_list = response.xpath('//strong[@class=" tw-font-bold"]/text()').getall()
        sold_list = response.xpath(
            '//span[@class="tw-relative tw-top-[1px] tw-ml-[3px] tw-text-[18px] tw-font-bold"]/text()').getall()
        print('=============================================================================================')
        index = 0
        for name in name_list:
            print(
                f"车名:{name:<20}\t评分:{score_list[index]  + '分':<10}\t价格:{price_list[index]:<15}\t销量:{sold_list[index]:>8}")
            index += 1
        print('=============================================================================================')

# scrapy crawl car
