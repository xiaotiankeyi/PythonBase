import pymysql

conn = pymysql.connect(host='192.168.117.9', port=3306, user='mysql', passwd='123', db='jforum')

handle = conn.cursor(cursor=pymysql.cursors.DictCursor)  # 生成对象

# sql = "create table s1(id tinyint, name varchar(10))"
# handle.execute(sql)

data = handle.execute("SELECT * from jforum_posts")
# print(data)

#获取下一行
print(handle.fetchone())

# print(handle.fetchall())

# handle.scroll(-1, mode="relative")  # 相对位置
# handle.scroll(2,mode="absolute")    #绝对位置

#显示十条数据
print(handle.fetchmany(10))

conn.commit()
# 关闭光标对象
handle.close()
# 关闭数据库连接
conn.close()
