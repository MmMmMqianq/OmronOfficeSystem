import pymysql

user1 = "user1"
password1 = "pwd1"

user2 = "user2"
password2 = "pwd2"

conn = pymysql.connect(host="qianshaoqing.mysql.rds.aliyuncs.com", user="omron", password="omron@2021", database="officesystem")
cursor = conn.cursor()
i = 0
while i < 100:
	sql_insert = "insert into random_amount(name, amount) values(%s, %s)"
	ret1 = cursor.execute(sql_insert, (user1, str(i)))  # 插入一条数据, ret返回值表示受影响的行数
	i += 1
# sql = "truncate table random_amount "
# cursor.execute(sql)
	conn.commit()  # 提交

cursor.close()
conn.close()