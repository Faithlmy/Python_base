import os
#查看当前所在路径
s1 = os.getcwd()
#print(s1)

#列举目录下的所有文件。返回的是列表类型
#s2 = os.listdir(s1)
s2 = os.listdir('D:\\pro')
#print(s2)

#返回绝对路径
#s3 = os.path.abspath('.')
s3 = os.path.abspath('..')
#print(s3)

#将文件夹和文件名分开(注意分别看效果，注意理解)
#s4 = os.path.split( 'D:\\pro\\mm\\test_os.py')
s4 = os.path.split( 'D:\\pro\\mm\\test_os.py\\')
#s4 = os.path.split( 'D:\\pro\\mm')
#s4 = os.path.split( 'D:\\pro\\faith_os\\')
#print(s4)

#将两条路径合并(后面的路径覆盖前面的路径)
s5 = os.path.join('D:\\faith_os\\myblog', 'D:\\mm', 'test_os.py')
#print(s5)

#返回文件夹中的路径，不包含最终结果
#s6 = os.path.dirname('D:\\pro\\faith_os\\test_os.py')
s6 = os.path.dirname('D:\\pro\\faith_os\\test_os.py\\')
#print(s6)

#查看文件时间
#最后修改时间
#s7 = os.path.getmtime('D:\\pro\\faith_os\\test_os.py')
#s7 = os.path.getmtime('D:\\pro\\faith_os\\')
#最后访问时间
#s7 = os.path.getatime('D:\\pro\\faith_os\\test_os.py')
#最后创建时间
s7 = os.path.getctime('D:\\pro\\faith_os\\test_os.py')
#print(s7)

#查看文件大小
s8 = os.path.getsize('D:\\pro\\faith_os\\test_os.py')
#print(s8)

#查看文件是否存在
#s9 = os.path.exists('D:\\pro\\faith_os\\test_os.py')
#s9 = os.path.exists('D:\\pro\\faith_os\\')
#s9 = os.path.exists('D:\\pro\\faith_os')
s9 = os.path.exists('D:\\faith_os')
#print(s9)

#判断现在使用平台(windows --> nt  linux --> posix)
s10 = os.name
#print(s10)

#s11 = os.remove('D:\\8.txt')
#s11 = os.rmdir('D:\\hello\\')
#s11 = os.mkdir('D:\\hello')
#print(s11)


#查看当前路径
#print(os.getcwd())
#改变路径
#os.chdir('D:\\hello')
#查看现在路径
#print(os.getcwd())