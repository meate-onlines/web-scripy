import scrapy
from scrapy.http import Request

class XuexilaSpider(scrapy.Spider):
    name = 'xuexila'
    allowed_domains = ['www.xuexila.com']
    start_urls = ['https://www.xuexila.com/']

    def parse(self, response):
        url_list = response.css('.nav_box .wrap .link_top a')
        for url_nods in url_list:
            url = url_nods.css('a::attr(href)').extract_first("")
            request_url = 'https:' + url
            yield Request(request_url, callback=self.parse_item)

    def parse_item(self, response):
        box = response.css('.wrap .box')
        for box_node in box:
            url = box_node.css('.c11 .h_title a::attr(href)').extract_first("")
            request_url = "https:" + url
            yield Request(request_url, callback=self.parse_item_detail)


    def parse_item_detail(self, response):
        content = response.css('.main_box .wrap .content_main')
        print(content.css('.con_top h1'))
        pass