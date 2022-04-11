
import pymysql

class DBUitl(object):
    def __init__(self):
        """初始化"""
        try:
            self.connection = pymysql.connect(
                host='192.168.0.121',
                user='mysql',
                port=3306,
                passwd='123456',
                db='test',
                charset='utf8'
            )
            # cursor = pymysql.cursors.DictCursor设置数据返回结果类型为字典
            self.conn=self.connection.cursor(cursor=pymysql.cursors.DictCursor)
        except Exception as e:
            print(e)

    def close(self):
        """关闭连接"""
        if self.conn:
            self.conn.close()

        if self.connection:
            self.connection.close()

    def DQL(self, sql, *args):
        """从数据库中得一个或多个表查询数据"""
        try:
            self.conn.execute(sql, args)
            # 返回结果集
            return self.conn.fetchall()
            # return self.conn.fetchone()
            # return self.conn.fetchmany(size=0)
        except Exception as e:
            print(e)
        finally:
            self.close()

    def DML(self, sql, *args):
        """修改数据库中的数据,包括插入(INSERT)、更新(UPDATE)和删除(DELETE)"""
        try:
            count = self.conn.execute(sql, args)
            self.connection.commit()
            return count
        except Exception as e:
            if self.connection:
                self.connection.rollback()
            print(e)
        finally:
            self.close()

    def DDL(self, sql, *args):
        """用于创建、修改、和删除数据库内的数据结构"""
        pass

if __name__ == "__main__":
    dbutil = DBUitl()
    # sql = "insert into student (id, name, age) values(%s, %s, %s)"
    # count = dbutil.DML(sql, 24, 'tom', 33)
    # print(count)

    sql = "select id, name, age from student where age>%s"
    data = dbutil.DQL(sql, 25)
    print(data)