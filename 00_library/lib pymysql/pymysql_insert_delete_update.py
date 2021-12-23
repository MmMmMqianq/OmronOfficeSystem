"""
	1. 连接数据库
	2. 创建游标
	3. 增删改需要commit(),查不需要
	4. 关闭游标
	5. 关闭连接
"""
import pymysql

user1 = "user1"
password1 = "pwd1"

user2 = "user2"
password2 = "pwd2"

conn = pymysql.connect(host="qianshaoqing.mysql.rds.aliyuncs.com", user="root", password="MQSq@19931219", database="test1")
cursor = conn.cursor()

sql_insert = "insert into t1(username, password) values(%s, %s)"
ret1 = cursor.execute(sql_insert, (user1, password1))  # 插入一条数据, ret返回值表示受影响的行数
ret2 = cursor.executemany(sql_insert, [(user1, password1), (user2, password2)])  # 插入多条数据
print(cursor.lastrowid)  # 返回新插入数据的自增ID

sql_delete = "delete from t1 where id<6"
ret3 = cursor.execute(sql_delete)

sql_update = "update t1 set username=%s where username=%s"
ret4 = cursor.execute(sql_update, ("aaa", "user1"))

conn.commit()  # 提交

cursor.close()
conn.close()