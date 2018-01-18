#!/usr/bin/python3
# -*- coding: UTF-8 -*-
dict = {}
dict['one'] = "1 - 教程"
dict[2]     = "2 - 工具"

tinydict = {'name': 'runoob','code':1, 'site': 'www.runoob.com'}


for c in tinydict:
    print(c , ':' , tinydict(c) )

print (dict['one'])       # 输出键为 'one' 的值
print (dict[2])           # 输出键为 2 的值
print (tinydict)          # 输出完整的字典
print (tinydict.keys())   # 输出所有键
print (tinydict.values()) # 输出所有值