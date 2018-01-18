#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
1. enter contents
2. scanning contents and documents, return result
3.







cynchanpin
Python扫描指定文件夹下(包含子文件夹)的文件


扫描指定文件夹下的文件。或者匹配指定后缀和前缀的函数。


假设要扫描指定文件夹下的文件，包含子文件夹，调用scan_files("/export/home/test/")

假设要扫描指定文件夹下的特定后缀的文件（比方jar包），包含子文件夹，调用scan_files("/export/home/test/", postfix=".jar")

假设要扫描指定文件夹下的特定前缀的文件（比方test_xxx.py）。包含子文件夹，调用scan_files("/export/home/test/", prefix="test_")


#!/usr/bin/env python
#coding=utf-8

import os

def scan_files(directory,prefix=None,postfix=None):
    files_list=[]

    for root, sub_dirs, files in os.walk(directory):
        for special_file in files:
            if postfix:
                if special_file.endswith(postfix):
                    files_list.append(os.path.join(root,special_file))
            elif prefix:
                if special_file.startswith(prefix):
                    files_list.append(os.path.join(root,special_file))
            else:
                files_list.append(os.path.join(root,special_file))

    return files_list

"""
import os
import time

def vic_scanfiles(v_dir):
    l_root = []
    l_sub = []
    l_doc = []
    if os.path.exists(v_dir) and os.path.isdir(v_dir):
        for root, sub_dir, file in os.walk(v_dir):
            l_root.append(root)
            l_sub.append(sub_dir)
            l_doc.append(file)
    else:
        print('error path!')
    return l_root, l_sub, l_doc

def vic_file_sum(file_list):#统计l_doc下有多少文件，即此目录下的总文件
    count = 0
    for i in file_list:
        if len(i):
            count += len(i)
    return count


def vic_list_t(v_list): # 递归遍历list  tuple  dict 的混合列表，直接打印出来
    for e in v_list:
        if isinstance(e, (list, tuple)):
            vic_list_t(e)
        elif isinstance(e, dict):
            for k, v in e.items():
                print('k: ', k, '\n', 'v: ', v)
        else:
            print(e)

v_d = []
def vic_list_sv(v_list): # 递归遍历list  tuple  dict 的混合列表，设置d=[]返回
    for e in v_list:
        if isinstance(e, (list, tuple)):
            vic_list_sv(e)
        elif isinstance(e, dict):
            for k, v in e.items():
                v_d.append(k)
        else:
            v_d.append(e)
    return v_d

def vic_list_y(v_list): # 不用第归 遍历list  tuple  dict 的混合列表, 用yield返回
    for e in v_list:
        if isinstance(e, (list, tuple)):
            for i in e:
                yield i
        elif isinstance(e, dict):
            for k, v in e.items():
                yield k
        else:
            yield e

"""
list去重复的方法
"""
def vic_no_fk():
    start = time.time()
    dd = ['b', 'c', 'd', 'b', 'c', 'a', 'a']
    for i in range(100000):
        {}.fromkeys(dd).keys()
    end = time.time()
    print(end - start)

def  vic_no_set():
    start = time.time()
    dd = ['b', 'c', 'd', 'b', 'c', 'a', 'a']
    for i in range(100000):
        set(dd)
    end = time.time()
    print(end - start)


def  vic_no_sort():#按顺序去重复
    start = time.time()
    dd = ['b', 'c', 'd', 'b', 'c', 'a', 'a']
    for i in range(100000):
        re = sorted(set(dd), key=dd.index)
    end = time.time()
    print(end - start)

def  vic_no_for():#按顺序去重复, for遍历 比sorted用时短
    start = time.time()
    dd = ['b', 'c', 'd', 'b', 'c', 'a', 'a']
    tt = []
    for i in range(100000):
        for i in dd:
            if not i in tt:
                tt.append(i)
    end = time.time()
    print(end - start)


if __name__ == '__main__':
    # vic_no_fk()
    # vic_no_set()
    # vic_no_sort()
    # vic_no_for()
    #
    # dd = ['b', 'c', 'd', 'b', 'c', 'a', 'a']
    # l = list(set(dd))
    #
    # v_k = sorted(set(dd), key=dd.index)
    # print(v_k)
    # pp = []
    # for i in dd:
    #     if not i in pp:
    #        pp.append(i)
    # print(pp)


    d = '/opt/vic'
    print(os.path.isdir(d))
    m1, m2, m3 = vic_scanfiles(d)
    print(
        m1, '\n',
        m2, '\n',
        m3, '\n',
        len(m3), '\n',
        )
    c = vic_file_sum(m3)
    print(c)

    d = [['r.c', 'm.c'], ['k.c'], {5: 'a', 2: 'b', 3: 'c'}, ['b.c'], ['c.c'], ('cc.c', 'dd.c'), ['b.c']]
    # d = [['k.c', 'm.c'], ['k.c'], ['b.c'], ['c.c'], ('c.c', 'dd.c'), ['c.c']]
    print(list(set(vic_list_y(d))))
    # print(list(set(vic_list_sv(m3))))