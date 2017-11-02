import pymysql
"""
连接数据库
"""
#简单粗暴法连接
# sql = """select * from tb_org;"""
# db = pymysql.Connect(host='10.132.37.126', port=3306, user='root', password='root', db='blog', charset='utf8')
# cursor = db.cursor()#创建游标
# print(cursor)
# c = cursor.execute(sql)#执行语句
# print(c)
# date = cursor.fetchone()#返回结果
# print(date)#输出结果
# cursor.close()#关闭游标
# db.close()#关闭连接

class Connect_mysql(object):
    def __init__(self, host, port, user, password, db, charset):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db = db
        self.charset = charset
        self.conn = None
        self.cur = None

    def get_connect(self):
        """
        得到连接
        :return:
        """
        try:
            conn = pymysql.Connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                db=self.db,
                charset=self.charset,

            )
            return conn
        except Exception as e:
            print("connect error: ", e)

    def get_cur(self):
        """
        获取游标
        :return:
        """
        try:
            self.conn = self.get_connect()
            self.cur = self.conn.cursor()
        except Exception as e:
            print("cursor error: ", e)

    def close(self):
        """
        关闭游标和连接
        :return:
        """
        self.cur.close()
        self.conn.close()

    def query(self, sql):
        """
        执行sql语句
        :return:
        """
        try:
            self.cur.execute(sql)
            sql_date = self.cur.fetchall()
            return sql_date
        except Exception as e:
            print("query error: ", e)

if __name__ == "__main__":
    host = '10.132.37.126'
    port = 3306
    user = 'root'
    password = 'root'
    db = 'blog'
    charset = 'utf8'
    sql = 'select * from tb_org;'

    r = Connect_mysql(host, port, user, password, db, charset)
    r.get_cur()
    d = r.query(sql)
    print(d)