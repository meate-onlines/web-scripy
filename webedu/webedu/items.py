# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst, Join, Identity


class WebeduItem(scrapy.Item):
    title = scrapy.Field()
    keywords = scrapy.Field()
    description = scrapy.Field()
    content_text = scrapy.Field()
    html = scrapy.Field()

    def get_insert_sql(self):
        pass


class ArticleItemLoader(ItemLoader):
    default_output_processor = TakeFirst()
