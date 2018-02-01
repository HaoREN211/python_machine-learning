import time
from scrapy.selector import Selector
from scrapy.http import Request
from scrapy.contrib.spiders import CrawlSpider
from scrapy.contrib.loader import ItemLoader
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from selenium import webdriver
from etao.items import EtaoItem


class etaoSpider(CrawlSpider):
    name = "etao"
    allow_domain = ['gouwu.sogou.com']
    start_urls = ['http://gouwu.sogou.com/shop?query=iphone6']
    link_extractor = {
        'page_down': SgmlLinkExtractor(allow='/shop\?query=.+', ),
        'page': SgmlLinkExtractor(allow='/detail/\d+\.html.+'),
    }
    _x_query = {
        'title': '//p[@class="title"]/a/@title',
        'price': '//span[@class="shopprice font17"]/text()',
        'name': '//span[@class="floatR hui61 mt1"]/text()',
    }

    def __init__(self):
        CrawlSpider.__init__(self)
        # use any browser you wish
        self.browser = webdriver.Firefox()

    def __del__(self):
        self.browser.close()

    def parse(self, response):
        # crawl all display page
        for link in self.link_extractor['page_down'].extract_links(response):
            yield Request(url=link.url, callback=self.parse)
        print response.url
        self.browser.get(response.url)
        time.sleep(5)
        url = str(response.url)
        etaoItem_loader = ItemLoader(item=EtaoItem(), response=response)
        etaoItem_loader.add_value('url', url)
        etaoItem_loader.add_xpath('title', self._x_query['title'])
        etaoItem_loader.add_xpath('name', self._x_query['name'])
        etaoItem_loader.add_xpath('price', self._x_query['price'])
        yield etaoItem_loader.load_item()