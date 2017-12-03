import pymysql as mdb
con = None
try:
    #连接mysql的方法：connect('ip','user','password','dbname')
    con = mdb.connect('10.129.7.200', 'user1',
        'Beaconuser1!', 'apibeacon');

    #所有的查询，都在连接con的一个模块cursor上面运行的
    cur = con.cursor()

    #执行一个查询
    cur.execute("SELECT VERSION()")

    #取得上个查询的结果，是单个结果
    data = cur.fetchone()
    print ("Database version : %s " % data)
finally:
    if con:
        #无论如何，连接记得关闭
        con.close()

with con:
    #获取连接的cursor，只有获取了cursor，我们才能进行各种操作
    cur = con.cursor()
#创建数据表writers(id, name)
    cur.execute("create table if not exists Writers(Id INT PRIMARY KEY AUTO_INCREMENT, Name VARCHAR (20))")
#插入数据
    cur.execute("INSERT INTO Writers(Name)VALUES ('Jack')")
    cur.execute("INSERT INTO Writers(Name)VALUES ('Merry')")
    cur.execute("INSERT INTO Writers(Name)VALUES ('Tanck')")