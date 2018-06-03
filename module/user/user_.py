class User:
	id_ = ''
	name = ''
	def toString(self):
		print("id_: %s, name: %s"%(self.id_, self.name))

def tojson(obj):
	return {
	'id': obj.id_,
	'name': obj.name
	}