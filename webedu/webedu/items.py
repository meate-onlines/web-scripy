# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst, Join, Identity


def content_txt(content_list):
    return content_list


class WebeduItem(scrapy.Item):
    title = scrapy.Field()
    keywords = scrapy.Field()
    description = scrapy.Field()
    content_text = scrapy.Field(
        input_processor=MapCompose(content_txt)
    )
    html = scrapy.Field()
    url = scrapy.Field()

    def get_insert_sql(self):
        insert_sql = """
            insert into xuexila_article(title, keywords, description, content_text, html, url) values (%s, %s, %s, %s, %s, %s)
        """
        params = {
            self.get('title', " "),
            self.get('keywords', " "),
            self.get('description', " "),
            self.get('content_text', "获取失败"),
            self.get('html', "获取失败"),
            self.get('url', " "),
        }
        return insert_sql, params


class ArticleItemLoader(ItemLoader):
    default_output_processor = TakeFirst()
