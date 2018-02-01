# -*- coding: utf-8 -*-

# Scrapy settings for etao project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
# http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'etao'

SPIDER_MODULES = ['etao.spiders']
NEWSPIDER_MODULE = 'etao.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'etao (+http://www.yourdomain.com)'
ITEM_PIPELINES = [
    'scrapy_mongodb.MongoDBPipeline',
]

MONGODB_URI = 'mongodb://localhost:27017'
MONGODB_DATABASE = 'company'
MONGODB_COLLECTION = 'etao'