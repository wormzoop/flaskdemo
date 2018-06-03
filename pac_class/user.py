class User:
	id_ = ''
	name = ''
	pwd = ''
	def speak(self):
		print("id_: %s, name: %s, pwd: %s"%(self.id_, self.name, self.pwd))
def tojson(obj):
	return {
	'id_': obj.id_,
	'name': obj.name,
	'pwd': obj.pwd
	}