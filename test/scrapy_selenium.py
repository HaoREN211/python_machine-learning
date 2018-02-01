#-*- coding: utf-8 -*-
'''
gouwu.sogou.com Spider, Created on Dec, 2014
#version: 1.0
#author: chenqx @http://chenqx.github.com
See more: http://doc.scrapy.org/en/latest/index.html
'''
import time
from scrapy.selector import Selector
from scrapy.http import  Request
from scrapy.spiders import CrawlSpider
from scrapy.loader import ItemLoader
from scrapy.linkextractors import LinkExtractor as SgmlLinkExtractor
from lib.etao.items  import EtaoItem
from selenium import webdriver

class etaoSpider(CrawlSpider):
    # name of spiders
    name = 'Spider'
    browser = webdriver.Chrome()
    allow_domain = ['gouwu.sogou.com']
    start_urls = [ (' ')]
    link_extractor = {
        'page':  SgmlLinkExtractor(allow = '/detail/\d+\.html.+'),
        'page_down':  SgmlLinkExtractor(allow = '/shop\?query=.+',),#restrict_xpaths = '//a[@class = "pagination-next"]'
    }
    _x_query = {
        'title':   '//p[@class="title"]/a/@title',
        'name':    '//span[@class="floatR hui61 mt1"]/text()',#//li[2]/a/div[@class="ruyitao-market-name ruyitao-market-name-hightlight"]/text()
        'price'    :    '//span[@class="shopprice font17"]/text()', # 'price'    :    '//span[@class = "price"]/text()',
    }
    def __init__(self):
        CrawlSpider.__init__(self)
        # use any browser you wish
        # self.browser = webdriver.Firefox()
        self.browser = webdriver.Chrome();
    def __del__(self):
        self.browser.close()
    def parse(self, response):
        #crawl all display page
        for link in self.link_extractor['page_down'].extract_links(response):
            yield Request(url = link.url, callback=self.parse)
        #start browser
        self.browser.get(response.url)
        #loading time interval
        time.sleep(5)
        # get the data and write it to scrapy items
        etaoItem_loader = ItemLoader(item=EtaoItem(), response = response)
        url = str(response.url)
        etaoItem_loader.add_value('url', url)
        etaoItem_loader.add_xpath('title', self._x_query['title'])
        etaoItem_loader.add_xpath('name', self._x_query['name'])
        etaoItem_loader.add_xpath('price', self._x_query['price'])
        yield etaoItem_loader.load_item()


teste = etaoSpider();
