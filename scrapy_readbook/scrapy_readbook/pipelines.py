# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# useful for handling different item types with a single interface
import pymysql
from itemadapter import ItemAdapter


class ScrapyReadbookPipeline:
    def open_spider(self, spider):
        self.f = open('book.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        self.f.write(str(item))
        return item

    def close_spider(self, spider):
        self.f.close()

# 加载settings文件
from scrapy.utils.project import get_project_settings


class MysqlPipeline:
    def open_spider(self, spider):
        settings = get_project_settings()
        # DB_HOST = '192.168.1.7'
        # DB_PORT = 3306
        # DB_USER = 'root'
        # DB_PASSWORD = '123456'
        # DB_NAME = 'spiderbook'
        # DB_CHARSET = 'utf-8'
        # self.host =settings['DB_HOST']
        self.port =settings['DB_PORT']
        self.user =settings['DB_USER']
        self.password =settings['DB_PASSWORD']
        self.name =settings['DB_NAME']
        self.charset =settings['DB_CHARSET']

        self.connect()
    def connect(self):
        self.conn = pymysql.connect(
            # host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            db=self.name,
            charset=self.charset,
        )
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        sql = 'insert into book(name,src) values("{}","{}")'.format(item['name'],item['src'])
        self.cursor.execute(sql)
        self.conn.commit()
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()