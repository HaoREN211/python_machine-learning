# -*- coding: utf-8 -*-
#!/usr/bin/python

from numpy import *;
from re import *;

import re

line = "40920.1234123   "

matchObj = re.search(r'([0-9]+\.)?([0-9]+)', line)

if matchObj:
    print "matchObj.group() : ", matchObj.group()
    print "matchObj.group(1) : ", matchObj.group(1)
    print "matchObj.group(2) : ", matchObj.group(2)
else:
    print "No match!!"