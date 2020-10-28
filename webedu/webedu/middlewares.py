# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import json

from scrapy import signals
import requests
import redis
import time
# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


def get_proxy_ip():
    redis_key = 'proxy_ip_key'
    r = redis.Redis(host='127.0.0.1', port=6379, db=0)
    if r.get(redis_key):
        ip_list = json.loads(r.get(redis_key))
        proxy_ip = 'https://{0}:{1}'.format(ip_list['ip'], ip_list['port'])
        return proxy_ip
    else:
        ip = requests.get('http://api.shenlongip.com/ip?key=i0o3z6gv&pattern=json&count=1&need=1100&protocol=2')
        ip_list = ip.json()['data'][0]
        proxy_ip = 'https://{0}:{1}'.format(ip_list['ip'], ip_list['port'])
        time_array = time.strptime(ip_list['expire'], "%Y-%m-%d %H:%M:%S")
        stamp = int(time.mktime(time_array))
        now = int(time.mktime(time.localtime()))
        des = stamp - now - 20
        r.set(redis_key, json.dumps(ip_list), des)
        return proxy_ip


class WebeduSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class WebeduDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class ProxyMiddleware:
    def process_request(self, request, spider):
        request.meta['proxy'] = get_proxy_ip()


if __name__ == '__main__':
    print(get_proxy_ip())