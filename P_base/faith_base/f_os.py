import os
"""
os.listdir(dirname)：列出dirname下的目录和文件

os.getcwd()：获得当前工作目录

os.curdir:返回当前目录（'.')

os.chdir(dirname):改变工作目录到dirname

os.path.isdir(name):判断name是不是一个目录，name不是目录就返回false

os.path.isfile(name):判断name是不是一个文件，不存在name也返回false

os.path.exists(name):判断是否存在文件或目录name

os.path.getsize(name):获得文件大小，如果name是目录返回0

os.path.abspath(name):获得绝对路径

os.path.normpath(path):规范path字符串形式

os.path.split(name):分割文件名与目录（事实上，如果你完全使用目录，它也会将最后一个目录作为文件名而分离，
                    同时它不会判断文件或目录是否存在）

os.path.splitext():分离文件名与扩展名

os.path.join(path,name):连接目录与文件名或目录

os.path.basename(path):返回文件名

os.path.dirname(path):返回文件路径 
"""

def faith_os():
    print(os.getcwd())
    print(dir(os.path))


if __name__=='__main__':
    faith_os()