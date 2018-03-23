#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
#-*-coding=gbk -*-
import os
import time

def listDir(fileDir):
     for eachFile in os.listdir(fileDir):
        if os.path.isfile(fileDir+"/"+eachFile):   #如果是文件，判断最后修改时间，符合条件进行删除
            ft = os.stat(fileDir+"/"+eachFile);
            ltime = int(ft.st_mtime); #获取文件最后修改时间
            #print "文件"+path+"/"+eachFile+"的最后修改时间为"+str(ltime);
            ntime = int(time.time())-3600*3; #获取现在时间减去3h
            if ltime<=ntime :
                print "我要删除文件"+fileDir+"/"+eachFile;
                os.remove(fileDir+"/"+eachFile);   #删除3小时前的文件

        elif os.path.isdir(fileDir+"/"+eachFile) :    #如果是文件夹，继续递归
            listDir(fileDir+"/"+eachFile);

if __name__ == '__main__':
    path = "E:/offlinefiles";   #规定目录
    while True :    #持续
        time.sleep(600);   #减少资源利用率  600s秒一次
        print "3600s  wake up";
        listDir(path);
"""
import os
import time

def delfilter(filepath, spacetime):
    """
    删除两小时之内修改过的文件
    :param filepath: 文件路径
    :return:
    """
    for f in os.listdir(filepath):
        newpath = filepath + '/' + f
        if os.path.isfile(newpath):
            ft = os.stat(newpath)
            last_time = int(ft.st_mtime)#文件最后修改时间
            t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(last_time))#時間格式轉化
            print('The last time of modify is : ', t)
            ntime = int(time.time()) - 30*spacetime #获取现在时间减去30*spacetime小时
            if ntime > last_time:
                print('Delete ' + newpath + ' file')
                os.remove(newpath)
            else:
                print('no')
        elif os.path.isdir(newpath):
            delfilter(newpath,spacetime)


if __name__ == '__main__':
    path = '/opt/faithlium'
    delfilter(path,1)
# f = os.getcwd()
# l = os.listdir(f)
# for i in l:
#     newpath = f + '/' + i
#     if os.path.isfile(newpath):
#         ft = os.stat(newpath)
#         last_time = int(ft.st_mtime)
#         ntime = int(time.time()) - 360
#         if ntime >= last_time:
#             os.remove(newpath)
#         # print(ft)
# # i = {i for i in l}
# # p = os.path.isfile(f + '/' + i)
#
# print(f)
# print(type(l))
# # print(p)