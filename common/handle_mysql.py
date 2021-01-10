"""操作数据库的方法封装"""


import pymysql


class HandleDB:

    def __init__(self):
        # 连接数据库
        self.con = pymysql.connect(
                        host='api.lemonban.com',
                        user='future',
                        password='123456',
                        port=3306,
                        charset='utf8'
        )

    # 获取一条数据
    def find_one(self, sql):
        # 创建游标
        cur = self.con.cursor()
        # 执行sql
        cur.execute(sql)
        d = cur.fetchone()
        # 提交sql
        self.con.commit()
        # 关闭游标
        cur.close()
        return d

    # 获取所有数据
    def find_all(self, sql):
        # 创建游标
        cur = self.con.cursor()
        # 执行sql
        cur.execute(sql)
        d = cur.fetchall()
        # 提交sql
        self.con.commit()
        # 关闭游标
        cur.close()
        return d

    #  关闭连接的方法
    def __del__(self):
        # 关闭数据库连接
        self.con.close()

if __name__ == '__main__':
    con = HandleDB()
    sql = 'select leave_amount from futureloan.member where mobile_phone=17600000000;'
    d = con.find_one(sql)
    print(d)
