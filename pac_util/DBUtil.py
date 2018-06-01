import pymysql

def getConnection():
	return pymysql.connect('localhost','root','root','db')