import scrapy
from scrapy.http import Request
from webedu.items import ArticleItemLoader, ChenyuItem


class ChenyuSpider(scrapy.Spider):
    name = 'chenyu'
    allowed_domains = ['www.diyifanwen.com']
    start_urls = ['https://www.diyifanwen.com/chengyu/sizichengyu/']

    def parse(self, response):
        nav = response.css("#ClassNaviTxt a")
        for nav_node in nav:
            url = nav_node.css("a::attr(href)").extract_first("")
            if url.find('s.') < 0:
                title = nav_node.css("a::text").extract_first("")
                request_url = "https:" + url
                yield Request(request_url, meta={'title': title}, callback=self.parse_item)

    def parse_item(self, response):
        title = response.meta['title']
        next_page = response.css("#CutPage a:nth-last-child(2)::attr(href)").extract_first("")
        if next_page:
            request_url = 'https:' + next_page
            yield Request(request_url, meta={'title': title}, callback=self.parse_item)
        item_loader = ArticleItemLoader(item=ChenyuItem(), response=response)
        item_loader.add_value('title', title)
        item_loader.add_css('words', "#cylist tr td[class='title'] a::text")
        item_loader.add_css('description', "#cylist tr td[class='detail'] a::text")
        yield item_loader.load_item()
