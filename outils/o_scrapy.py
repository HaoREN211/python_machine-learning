# -*- coding: utf-8 -*-
#!/usr/bin/python
# https://cuiqingcai.com/1052.html
import urllib
import urllib2
import time
import lxml;
import twisted;
import OpenSSL;
import zope.interface;


page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page);
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)';
headers = { 'User-Agent' : user_agent };
try:
    request = urllib2.Request(url, headers=headers);
    response = urllib2.urlopen(request)
    time.sleep(5)
    print response.read()
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason