from module.mall import mall
from module.mall.mall_ import Mall, tojson
from flask import Response, session, request
from pac_util.DBUtil import getConnection
import json

#商品列表
@mall.route('/list', methods=['GET','POST'])
def list():
	db = getConnection()
	cursor = db.cursor()
	sql = "select * from mall";
	list = []
	try:
		cursor.execute(sql)
		results = cursor.fetchall()
		print(results)
		for row in results:
			m = Mall()
			m.id_ = row[0]
			m.name = row[1]
			m.price = row[2]
			list.append(m)
		return Response(json.dumps(list, default=tojson, ensure_ascii=False), 'application/json')
	except:
		dict = {'error':'请求失败'}
		return Response(json.dumps(dict), 'application/json')
	db.close()	