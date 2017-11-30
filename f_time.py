import threading
from time import sleep, ctime
import os
import random
import stat as s
import time
import datetime

def hello(name):
    print("hello %s\n" % name)

    global timer
    timer = threading.Timer(2.0, hello, ["Hawk"])
    timer.start()


def loop1():
    """
    how to use sleep() and ctime()
    :return:
    """
    print("h", ctime())
    sleep(3)
    print('3c', ctime())

def loop2():
    for i in range(1,10):
        sleep(2)
        print('h',ctime())

def f_file(f_path):
    # if os.path.isabs(f_path):
    if os.path.exists(f_path) and not os.path.isfile(f_path + '/'+'test.txt'):
        os.mknod(f_path + '/'+'test1.txt', mode=777)
        print('abs_path')
    else:
        print('no_path')
    # os.mkdir(f_path)


def f_file_two(f_path):
    print(os.stat(path=f_path).st_atime)

def faith_time():

    """
    There is time of intruduce, 6 parts such as:
    1. The three format of time convert
    2. now time:
    3. time stamp:
    4. formating time:
    5. convert the origin time to time stamp:

    6.
    %y 两位数的年份表示（00-99）
    %Y 四位数的年份表示（000-9999）
    %m 月份（01-12）
    %d 月内中的一天（0-31）
    %H 24小时制小时数（0-23）
    %I 12小时制小时数（01-12）
    %M 分钟数（00=59）
    %S 秒（00-59）

    %a 本地简化星期名称
    %A 本地完整星期名称
    %b 本地简化的月份名称
    %B 本地完整的月份名称
    %c 本地相应的日期表示和时间表示
    %j 年内的一天（001-366）
    %p 本地A.M.或P.M.的等价符
    %U 一年中的星期数（00-53）星期天为星期的开始
    %w 星期（0-6），星期天为星期的开始
    %W 一年中的星期数（00-53）星期一为星期的开始
    %x 本地相应的日期表示
    %X 本地相应的时间表示
    %Z 当前时区的名称
    %% %号本身

    """
    print('time.ctime()', time.ctime(), '\n')
    print('time.gmtime()', time.gmtime(), '\n')


    # The three format of time convert
    tn1 = time.time()# float
    tn2 = time.localtime(tn1) # float --> tuple tuple
    tn3 = time.strftime('%Y-%m-%d %H:%M:%S', tn2) # tuple --> str
    tn4 = time.strptime(tn3, '%Y-%m-%d %H:%M:%S') # str --> tuple
    tn5 = time.mktime(tn4)# tuple --> float
    # tn6 = datetime(*tn4[0:6])
    print(
        'the type of tn1:', type(tn1), '\n',
        'the value of tn1:', tn1, '\n',

        'the type of tn2:', type(tn2), '\n',
        'the value of tn2:', tn2, '\n',

        'the type of tn3:', type(tn3), '\n',
        'the value of tn3:', tn3, '\n',

        'the type of tn4:', type(tn4), '\n',
        'the value of tn4:', tn4, '\n',

        'the type of tn5:', type(tn5), '\n',
        'the value of tn5:', tn5, '\n',
          )


    # now time
    t = time.time()
    print('All of origin time infomation:', '\n',
          'The t type is:', type(t), '\n',
          'The origin:', t, '\n',
          'Turn int is:', int(t), '\n',
          'Turn localtime is:', time.localtime(t), '\n',
          'Turn new type is:', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(t)), '\n',
          )

    # time stamp
    ts = 1234567890
    print('Turn is: ', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(ts)), '\n')

    # formating time
    print('The first type is:', time.strftime('%Y-%m-%d', time.localtime(t)), '\n',
          'The second type is:', time.strftime('%Y%m%d', time.localtime(t)), '\n',
          'The second type is:', time.strftime('%Y%m%d%H%M%S', time.localtime(t)), '\n',
          'The second type is:', time.strftime('%Y/%m/%d/%H/%M/%S', time.localtime(t)), '\n',
          )

    # convert the origin time to time stamp
    or_time = '2016-03-15 13:32:01'
    array_time = time.strptime(or_time, '%Y-%m-%d %H:%M:%S')
    print('The result is: ', time.mktime(array_time), '\n')

    """
    There is datetime of intruduce,
    
    """
    # now datetime
    dn = datetime.datetime.now()
    print('Origin datetime: ', dn, '\n',
          'strf is: ', dn.strftime('%Y-%m-%d %H:%M:%S %A'), '\n',
          'isoformat:', dn.isoformat(), '\n',
          'year:', dn.year, '\n',
          'hour:', dn.hour, '\n',
          'microsecond', dn.microsecond, '\n',
          'weekday (0-6)=(Mon-Sun): ', dn.weekday(), '\n',
          )

    # get time of 3 days ago:
    three_day_ago = (datetime.datetime.now() - datetime.timedelta(days=3))
    print('time is', three_day_ago.strftime('%Y-%m-%d %H:%M:%S'), '\n',)

    # 给定时间戳, 计算该时间的几天前时间
    time_stamp = 1234567890
    pt = time.localtime(time_stamp)
    pl = time.strftime('%Y-%m-%d %H:%M:%S', pt)
    dateArray = datetime.datetime.utcfromtimestamp(time_stamp)# turn datetime
    three_day = dateArray - datetime.timedelta(days=2)
    print('time_stamp is: ', pl, '\n',
          'three_day_ago is: ', three_day, '\n',
          'the type of time.location is:', type(pt), '\n',
          )

    # yesterday today  tomorrow
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)
    tomorrow = today + datetime.timedelta(days=1)
    print('today is:', today, '\n',
          'yesterday is: ', yesterday, '\n',
          'tomorrow is: ', tomorrow, '\n',
          )




if __name__ == "__main__":
    # timer = threading.Timer(0, hello, ["Hawk"])
    # timer.start()
    # loop1()
    # loop2()
    f_path = r'/opt/f_test/'
    # f_file(f_path)
    file_name = 'test1.txt'
    # f_file_two(f_path + file_name)
    # faith_time()
    # for i in range(1,10):
    #     print(chr(random.randint(97,122)))
