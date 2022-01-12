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
	# sql_select1 = "select id from random_amount order by id desc limit 1"
	sql_select1 = "SELECT count(*) from random_amount;"
	max_id = cursor.execute(sql_select1)
	data = cursor.fetchall()
	if data != 0:
		max_id = data[0]["count(*)"]
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
	# sql_select2 = "select * from random_amount where id between %s and %s"
	sql_select2 = "select * from random_amount limit %s, %s"
	cursor.execute(sql_select2, (starting_line, ending_line))
	data = cursor.fetchall()
	return data


def insert_data(cursor: pymysql.cursors.DictCursor, conn: pymysql.connections.Connection, name, amount):
	sql_insert = "insert into random_amount(name, amount) values(%s, %s)"
	cursor.execute(sql_insert, (name, amount))
	conn.commit()


def delete_data(cursor: pymysql.cursors.DictCursor, conn: pymysql.connections.Connection, id_list):
	sql_delete = "delete from random_amount where id = %s"
	cursor.executemany(sql_delete, id_list)
	conn.commit()


def update_data(cursor: pymysql.cursors.DictCursor, conn: pymysql.connections.Connection, id_amount: list):
	"""
	更新amount列的数据
	:param cursor:
	:param conn:
	:param id_amount: 列表，该列表必须由(amount, id)元祖构成
	:return:
	"""
	sql_update = "update random_amount set amount = %s where id = %s"
	cursor.executemany(sql_update, id_amount)
	conn.commit()


def get_id(cursor: pymysql.cursors.DictCursor):
	sql_select = "select id from random_amount"
	cursor.execute(sql_select)
	id_list = cursor.fetchall()
	return id_list


def close(conn: pymysql.connections.Connection, cursor: pymysql.cursors.DictCursor):
	# 关闭游标，关闭MySQL连接
	cursor.close()
	conn.close()


if __name__ == "__main__":
	logging.config.fileConfig("log/logging.conf")
	logger = logging.getLogger("applog")
	conn, cur = connect_db()
	update_data(cur, conn, [(20, 1), (21, 4), (22, 5), (23, 6), (24, 7)])

	close(conn, cur)
