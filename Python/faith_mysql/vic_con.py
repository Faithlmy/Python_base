#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import requests
import re
import pymysql


def getHTMLtext(url):
    try:
       r=requests.get(url,timeout=100)
       r.raise_for_status()
       r.encoding=r.apparent_encoding
       return r.text
    except:
        return ""
def getpage(itl,html):
    try:
        #plt=re.findall(r'"view_price":"[\d.]*"',html)
        #nlt=re.findall(r'"raw_title":".*?"',html)
        s=eval(html)
        for i in range(len(s)):
            #price = eval(plt[i].split(':')[1])
            #title = eval(nlt[i].split(':')[1])
            itl.append([s[i].get('app'),s[i].get('name'),s[i].get('applied')])
    except:
       print("")


def printgoods(itl):
    tplt = "{:2}\t{:8}\t{:8}\t{:16}"
    print(tplt.format("序号", "功能", "APP名称","创建时间"))

    count = 0
    conn = pymysql.connect(host='localhost', user='root', password='root', db='myapp',charset="utf8")

    cur = conn.cursor()

    sqlc = '''
                CREATE TABLE iapp (
                id int(11) NOT NULL AUTO_INCREMENT,
                app varchar(255) NOT NULL,
                name varchar(255) NOT NULL,
                applied varchar(255) NOT NULL,
                PRIMARY KEY (id)
                ) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
                '''

    try:
        A = cur.execute(sqlc)
        conn.commit()
        print('成功')
    except:
        print("错误")
    for g in itl:
        count = count + 1
        b=tplt.format(count, g[0], g[1],g[2])
        print(b)



        sqla = '''
        insert into  iapp(app,name,applied)
        values(%s,%s,%s);
       '''
        try:
            B = cur.execute(sqla,(g[0],g[1],g[2]))
            conn.commit()
            print('成功')
        except:
            print("错误")

        # save_path = 'D:/taobao.txt'
        # f=open(save_path,'a')
        #
        # f.write(b+'\n')
        # f.close()

    conn.commit()
    cur.close()
    conn.close()


def main():
    #goods="咖啡"

    start_url='http://127.0.0.1:8000/api/tasks3/'
    List =[]

    try:
        #url =start_url +"&s="+ str(i*44)
        html=getHTMLtext(start_url)
        getpage(List,html)
    except:
        print("ss")


    print(printgoods(List))
    # savefiles(data)




main()