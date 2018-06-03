import pymysql

def getConnection():
	return pymysql.connect(host='localhost',port=3306,user='root',passwd='root',db='db',charset='utf8')