class User:
	id_ = ''
	name = ''
	def speak(self):
		print("id_: %s, name: %s"%(self.id_, self.name))
def tojson(obj):
	return {
	'id_': obj.id_,
	'name': obj.name
	}