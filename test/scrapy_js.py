# -*-coding:utf-8-*-
#!/usr/bin/python
from selenium import webdriver
from scrapy.http import HtmlResponse
import time
import scrapy;

class JavaScriptMiddleware(object):

    def process_request(self, request, spider):
        if spider.name == "jd":
            print "PhantomJS is starting..."
            # driver = webdriver.PhantomJS() #指定使用的浏览器
            driver = webdriver.Firefox()
            driver.get(request.url)
            time.sleep(1)
            js = "var q=document.documentElement.scrollTop=10000"
            driver.execute_script(js) #可执行js，模仿用户操作。此处为将页面拉至最底端。
            time.sleep(3)
            body = driver.page_source
            print ("访问"+request.url)
            return HtmlResponse(driver.current_url, body=body, encoding='utf-8', request=request)
        else:
            return "failed";

class JdSpider(scrapy.Spider):
    name = ""
    allowed_domains = [' ' ]
    start_urls = (
    )

    def parse(self, response):
        print response.body;

