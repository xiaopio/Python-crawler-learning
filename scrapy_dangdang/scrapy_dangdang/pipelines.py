# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


# 先在 settings中开启管道
class ScrapyDangdangPipeline:
    # 在爬虫文件执行之前就执行的方法
    def open_spider(self, spider):
        print('+++++++++++++++++++++++++++++++++')
        self.f = open('book.json', 'w', encoding='utf-8')

    # item 就是yield后面的对象
    def process_item(self, item, spider):
        # with open('book.json', 'a', encoding='utf-8') as f:
        #     # TypeError: write() argument must be str, not ScrapyDangdangItem
        #     f.write(str(item))
        self.f.write(str(item))
        return item

    # 在爬虫文件执行完后执行的方法
    def close_spider(self, spider):
        print('--------------------------------')
        self.f.close()


import urllib.request

# 多条管道同时开启
#   定义管道类
#   在settings中开启管道
class DangDangDownloadPipeline:
    def process_item(self, item, spider):
        url = 'https:' + item.get('src')
        filename = './books/' + item.get('name') + '.jpg'
        urllib.request.urlretrieve(url=url, filename=filename)

        return item
