# -*- coding: utf-8 -*-
#!/usr/bin/python

import StringIO
import pickle

class Person:
    def __init__(self,n,a):
        self.name=n
        self.age=a
    def show(self):
        print self.name+"_"+str(self.age);

aa = Person("JGood", 2) ;
aa.show() ;
fle = StringIO.StringIO();
pick = pickle.Pickler(fle);
pick.dump(aa) ;
val1=fle.getvalue();
print len(val1);
"""
python的pickle如果不clear_memo，则不会多次去序列化对象。
"""
# pick.clear_memo()
pick.dump(aa)
val2=fle.getvalue()
print len(val2)
fle.close()