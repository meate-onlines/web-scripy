import scrapy


class XuexilaSpider(scrapy.Spider):
    name = 'xuexila'
    allowed_domains = ['www.xuexila.com']
    start_urls = ['https://www.xuexila.com/']

    def parse(self, response):
        pass

    def parse_item(self, response):
        pass