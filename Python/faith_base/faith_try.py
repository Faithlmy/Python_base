#!/usr/bin/python
# -*- coding: UTF-8 -*-

# try:
#     fh = open("testfile", "w")
#     fh.write("这是一个测试文件，用于测试异常!!")
# except IOError:
#     print ("Error: 没有找到文件或读取文件失败")
# else:
#     print ("内容写入文件成功")
#     fh.close()
def f_try(fileName):
    try:
        f = open(fileName, "w")
        f.write("test file")
        a = 3+8
    except IOError:
        print("Error")
    else:
        print("success! ")
    return a

def f_try_zero(fileName):
    try:
        open(fileName)
        # a = 2/0
        # print(a)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    fileName = "faithte"
    # d = f_try(fileName)
    # print(d)
    f_try_zero(fileName)