import pymysql
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
import logging
import  logging.config


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
	a = cursor.execute(sql_select1)
	data = cursor.fetchall()
	if data != 0:
		max_id = data[0]["id"]
	else:
		max_id = 0
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


def insert_data(cursor: pymysql.cursors.DictCursor, conn: pymysql.connections.Connection, name, amount):
	sql_insert = "insert into random_amount(name, amount) values(%s, %s)"
	cursor.execute(sql_insert, (name, amount))
	conn.commit()


# def delete_data(cursor: pymysql.cursors.DictCursor, start_line, end_line):
# 	# sql_truncate = "delete from random_amount where id between %s and %s"
# 	sql_truncate = "truncate random_amount"
# 	cursor.execute(sql_truncate)
# 	# cursor.execute(sql_truncate, (start_line, end_line))


def close(conn: pymysql.connections.Connection, cursor: pymysql.cursors.DictCursor):
	# 关闭游标，关闭MySQL连接
	cursor.close()
	conn.close()


if __name__ == "__main__":
	logging.config.fileConfig("log/logging.conf")
	logger = logging.getLogger("applog")
	conn, cur = connect_db()

	print(get_contents_of_table(cur, 130, 260))
	insert_data(cur, conn, "aaa", "123")
	print(get_max_id(cur))

	close(conn, cur)
