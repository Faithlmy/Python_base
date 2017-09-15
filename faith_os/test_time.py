import time
from datetime import datetime

#python中有三种方式表示时间：
#1、UTC 世界标准时间
#2、时间戳（timestamp）
#3、元组(struct_time)

#struct_time
print(time.localtime())
#转化UTC时间
print(time.gmtime())
#时间戳
print(time.time())
#将strct_time转化成时间戳

#print(time.mktime(time.localtime()))

#time.sleep(10)
#print(time.clock())

print(time.asctime())

print(time.ctime())
#把时间戳转化为ctime
print(time.ctime(time.time()))

print('*'*200)
#datetime
#
a = datetime.now()
print(a)
print(a.timestamp())
print(a.ctime())