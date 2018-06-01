from module.user import user
from flask import Response
from pac_class.user import User,tojson
import json
import pymysql

@user.route('/list', methods=['GET','POST'])
def list():
	db = pymysql.connect('localhost','root','root','db')
	cursor = db.cursor()
	sql = 'select * from user'
	list = []
	try:
		cursor.execute(sql)
		results = cursor.fetchall()
		for row in results:
			u = User()
			u.id_ = row[0]
			u.name = row[1]
			list.append(u)
	except:
		db.rollback()
	db.close()
	return Response(json.dumps(list, default=tojson), 'application/json')