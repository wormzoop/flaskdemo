from flask import Flask, Response
from flask import request
from pac_class.user import User,tojson
from pac_util.DBUtil import getConnection
import pymysql
import json

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def home():
    return '<html><title>首页</title><body><p>welcome首页</p></body></html>'

@app.route('/user/list', methods=['GET'])
def userlist():
	db = getConnection()
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
			print(list)
	except:
		db.rollback()
	db.close()
	return Response(json.dumps(list, default=tojson), 'application/json')

if __name__ == '__main__':
    app.run()
