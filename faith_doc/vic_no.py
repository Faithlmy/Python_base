from datetime import *
import os
import time as t
import random

def vic_time():
    """
    用时间生成独一无二的文件名
    :return:
    """
    for i in range(0, 1):
        nowTime = datetime.now().strftime("%Y%m%d%H%M%S")#生成当前的时间
        randomNum = random.randint(0,100)#生成随机数n,其中0<=n<=100
        if randomNum <= 10:
            randomNum = str(0) + str(randomNum)
        uniqueNum = str(nowTime) + str(randomNum)
        return uniqueNum

def vic_createdir(v_path, dir_name):
    """
    创建目录，返回路径
    :param v_path:原始目录
    :param dir_name: 创建目录
    :return:
    """
    if os.path.exists(v_path):
        v_p = v_path +'/' + dir_name
        os.makedirs(v_p)
    else:
        print('dir is exits!')
    return v_p

def vic_createfile(v_path, file_name, f_suffix):
    """
    创建文件，返回路径
    :param v_path: 路径
    :param file_name: 文件名
    :param f_suffix: 文件后缀
    :return:
    """
    if os.path.exists(v_path):
        v_p = v_path + '/' + file_name + f_suffix
        os.mknod(v_p)
    else:
        print('file is exits!')

    return v_p

def vic_main():
    """
    调用上面三个个函数
    :return:
    """
    path = '/opt/faithvic'
    f_suffix = '.c'
    i = 0
    j = 0
    while j< 5:
        p = vic_createdir(path, vic_time())
        t.sleep(0.5)
        print(p)
        j = j+1
        while i < 5:
            p_f = vic_createfile(p, vic_time(), f_suffix)
            print('ok', p_f)
            t.sleep(0.5)
            i = i + 1
        i = 0



if __name__ == '__main__':
    vic_main()