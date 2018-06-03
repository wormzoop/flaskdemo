class Mall:
	id_ = ''
	name = ''
	price = 0
	def toString(self):
		print("id: %s, name: %s, price: %d"%(self.id_, self.name, self.price))

def tojson(obj):
	return {
	'id': obj.id_,
	'name': obj.name,
	'price': obj.price
	}		