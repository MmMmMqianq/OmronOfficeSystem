import pymysql


conn = pymysql.connect(host="qianshaoqing.mysql.rds.aliyuncs.com", user="root", password="MQSq@19931219", database="test1")
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)  # 取出的没有行数据为字典形式{表头:value}

sql = "select * from t1 where username=%s and password = %s"  # 如果直接格式化字符串会出现漏洞，通过SQL注入即使用户名或者密码不对也能有返回值
															# 比如用户名输入asd' or 1=1 --
cursor.execute(sql, ("aaa", "pwd1"))

# cursor.scroll(2, mode="relative")  # 游标在当前位置向后偏移两个位置
# cursor.scroll(3, mode="absolute")  # 游标从头开始偏移3个位置

result = cursor.fetchone()  # 从所有匹配项中获取第一条数据，如过再执行一次就会取出第二条数据
result2 = cursor.fetchone()
result4 = cursor.fetchmany(2)  # 一次取多个
result3 = cursor.fetchall()  # 获取所有匹配的数据

print(result)
print(result2)
print(result3)

cursor.close()
conn.close()