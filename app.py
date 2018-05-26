from flask import Flask, Response
from flask import request
from pac_class.user import User,tojson
import pymysql
import json

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def home():
    return '<html><title>首页</title><body><p>welcome首页</p></body></html>'

@app.route('/user/list', methods=['GET'])
def userlist():
	db = pymysql.connect("rm-2zey1rij96gh594txto.mysql.rds.aliyuncs.com","root","123QWE!@#","heisa")
	cursor = db.cursor()
	sql = 'select * from test'
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
