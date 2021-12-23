import pymysql


def connect_db(h="qianshaoqing.mysql.rds.aliyuncs.com", u="omron", pwd="omron@2021", db="officesystem"):
	"""
	建立数据库的连接
	:param h: 主机地址
	:param u: 用户名
	:param pwd: 密码
	:param db: 数据库名
	:return: conn, cursor
	"""
	conn = pymysql.connect(host=h, user=u, password=pwd, database=db)
	cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
	return conn, cursor


def get_max_id(cursor: pymysql.cursors.DictCursor):
	"""
	获取表中的总行数
	:param cursor: 游标
	:return: 返回总行数
	"""
	sql_select1 = "select id from random_amount order by id desc limit 1"
	cursor.execute(sql_select1)
	max_id = cursor.fetchall()[0]["id"]
	return max_id


def get_contents_of_table(cursor: pymysql.cursors.DictCursor, starting_line=1, ending_line=22):
	"""
	获取数据库表中指定行的数据行用于显示到table widget
	:param cursor: 游标
	:param starting_line: 起始行号
	:param ending_line: 结束行号
	:return: data，返回字典列表
	"""
	sql_select2 = "select * from random_amount where id between %s and %s"
	cursor.execute(sql_select2, (str(starting_line), str(ending_line)))

	data = cursor.fetchall()
	return data


def close(conn: pymysql.connections.Connection, cursor: pymysql.cursors.DictCursor):
	# 关闭游标，关闭MySQL连接
	cursor.close()
	conn.close()


if __name__ == "__main__":
	conn, cursor = connect_db()
	get_max_id(cursor)
	get_contents_of_table(cursor, 1, 26)
	close(conn, cursor)
