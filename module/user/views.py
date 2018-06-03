from module.user import user
from flask import Response,session,request
from module.user.user_ import User,tojson
from util.DBUtil import getConnection
import json

#获得用户列表
@user.route('/list', methods=['GET','POST'])
def list():
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
	except:
		db.rollback()
	db.close()
	return Response(json.dumps(list, default=tojson), 'application/json')

#登录
@user.route('/login', methods=['GET','POST'])
def login():
	name = request.args.get('name')
	pwd = request.args.get('pwd')
	db = getConnection()
	cursor = db.cursor()
	sql = "select * from user where name = '%s' and pwd='%s'" % (name, pwd)
	print(sql)
	try:
		cursor.execute(sql)
		results = cursor.fetchone()
		if(results == None):
			dict = {'error':'用户名或密码不对'}
			return Response(json.dumps(error), 'application/json')
		user = User()
		user.id_ = results[0]
		user.name = results[1]
		user.pwd = results[2]
		session['id'] = user.id_
		session['name'] = user.name
		session['pwd'] = user.pwd
		return Response(json.dumps(user, default=tojson), 'application/json')
	except:
		dict = {'error':'请求失败'}
		return Response(json.dumps(dict), 'application/json')

#获得用户信息
@user.route('/getUser', methods=['GET','POST'])
def getUser():
	user = User()
	user.id_ = session.get('id')
	user.name = session.get('name')
	user.pwd = session.get('pwd')
	return Response(json.dumps(user, default=tojson), 'application/json')		