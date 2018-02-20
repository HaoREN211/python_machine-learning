# -*- coding: utf-8 -*-
#!/usr/bin/python

import re

my_sent = "This book is the best book on Python or M.L I have ever laid eyes upon."
reg_ex = re.compile('\\W*')
my_sent_split = my_sent.split();
my_sent_split_re = reg_ex.split(my_sent)
my_sent_split_re_len = [token for token in my_sent_split_re if len(token)>0]
my_sent_split_re_len_lower = [token.lower() for token in my_sent_split_re_len]

print my_sent_split_re_len_lower;