"""
#-*-coding:utf-8-*-
'"author:GoGoCaptain"'

import sys
import MySQLdb
def Main():
    f1=open('md5.txt','r')#打开需要查询的md5
    f2=open('result.txt','w+')#查询结果写到result里

    conn=MySQLdb.connect(host='xxxxx',user='xxxx',passwd='xxxx',db='xxxx',port=xxxx)
    cur=conn.cursor()
    i = 0
    md5 = f1.readline()

    while md5 != '':
        sql = "SELECT file_md5 FROM `v_scanresult_all` where cert_md5='%s'"%md5.split('\n')[0]#数据库查询语句，可根据实际需求修改
        cur.execute(sql)#执行数据库查询语句
        result = cur.fetchall()#获取查询结果
        data = str(result).split(',')
        for d in data:
            if len(d)>20:
                d = d.replace(',','').replace(')','').replace('(','').replace('\'','').replace(' ','')  #删除无用字符，方便查看
                f2.write(d + '\n')
        i += 1
        print md5.split('\n')[0],'-->ok--count:' + str(i)
        #f2.write(str(result) + '\n')
        md5 = f1.readline()
    f1.close()
    f2.close()
    conn.close()
if __name__ == '__main__':
    Main()

"""
#!/usr/bin/env python3
# -*- coding: utf_8 -*-
import os
import pymysql

def main():
    f1 = open('sql.txt', 'r')
    f2 = open('result.txt', 'a')

    conn = pymysql.connect(host='10.132.37.126', port=3306, user='root', password='root', db='faith')
    cur = conn.cursor()
    sql = 'select* from tb_sum'
    s = f1.read() + ' limit 1'
    print(s)
    cur.execute(s)
    re = cur.fetchall()
    print(re)
    f = str(re)
    f2.write(os.popen('netstat -nltp | grep 22').read())
    f2.write('90')
    # f1.close()
    f2.close()

    # f1 = open('sql.txt', 'r')
    # print(f1.read())
    """
    字符串的拼接
    :return:
    """
    # f = 'fun'
    # # print(f + 'ction')
    # c = ['c','t','i','o','n']
    # print(f.join(c))
    #
    #
    # dd = 'st ion'
    # gg = 'fun'
    # cc = ["c","t", "i"]
    # kk = ['ff']
    # print(''.join(cc))
    # print(gg + dd)
#
# def connstring():
#     t = time()
#     for i in range(10000000):
#         f = ''.join(['app', 'le'])
#     print(time() - t)
# def connstring_two():
#     t = time()
#     for i in range(10000000):
#         f = 'app'+'le'
#     print(time() - t)
# from time import time
# if __name__ == '__main__':
#     connstring()
#     # connstring_two()


from time import time
def method1():
    t = time()
    for i in range(1000000):
        s = 'app'+'le' + 'aa' + 'bb' + 'cc' + 'dd' + 'ee'+ 'ff'
    print(time() - t)
def method2():
    t = time()
    for i in range(1000000):
        s = ''.join(['app', 'le','aa', 'bb', 'cc', 'dd', 'ee', 'ff'])
    print(time() -t)
def method3():
    t = time()
    for i in range(1000000):
        s = '%s%s%s%s%s%s%s%s'%('app', 'le','aa', 'bb', 'cc', 'dd', 'ee', 'ff')
    print(time() - t)

method1()
method2()
method3()