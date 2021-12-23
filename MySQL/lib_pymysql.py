"""
模拟登录验证用户名和密码
"""

import pymysql


user = input("请输入用户名：")
password = input("请输入密码：")

conn = pymysql.connect(host="qianshaoqing.mysql.rds.aliyuncs.com", user="root", password="MQSq@19931219", database="test1")
cursor = conn.cursor()

sql = "select * from t1 where username=%s and password = %s"  # 如果直接格式化字符串会出现漏洞，通过SQL注入即使用户名或者密码不对也能有返回值
															# 比如用户名输入asd' or 1=1 --
cursor.execute(sql, (user, password))
# result2 = cursor.fetchall()  # 获取所有匹配的数据
result = cursor.fetchone()  # 获取第一个匹配项

cursor.close()
conn.close()

if result is None:
	print("用户名或密码错误！")
else:
	print("登录成功！")