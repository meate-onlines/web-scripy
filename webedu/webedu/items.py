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
        output_processor=Join(separator="$$")
        # input_processor=MapCompose(content_txt)
    )
    html = scrapy.Field()
    url = scrapy.Field()

    def get_insert_sql(self):
        insert_sql = """
            insert into xuexila_article(title, keywords, description, content_text, html, url) values (%s, %s, %s, %s, %s, %s)
        """
        params = (
            self.get('title', " "),
            self.get('keywords', " "),
            self.get('description', " "),
            self.get('content_text', "获取失败"),
            self.get('html', ' '),
            self.get('url', " "),
        )
        return insert_sql, params


class ArticleItemLoader(ItemLoader):
    default_output_processor = TakeFirst()


class ChenyuItem(scrapy.Item):
    words = scrapy.Field(
        output_processor=Join(separator="$$")
    )
    description = scrapy.Field(
        output_processor=Join(separator="$$")
    )
    title = scrapy.Field()

    def pass_item(self):
        description = self.get('description', 0)
        words = self.get('words', 0)
        title = self.get('title', '')
        description_list = description.split('$$')
        words_list = words.split('$$')
        yu_list = []
        if words:
            for index, word in enumerate(words_list):
                child_dict = {
                    'word': word,
                    'description': description_list[index],
                    'title': title
                }
                yu_list.append(child_dict)
        return yu_list
