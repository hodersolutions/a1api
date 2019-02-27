from root import application, db

class dbModlelPlus(db.Model):
	def filter_by(**kwargs):
		arg_list = []
		for key, value in kwargs.items():
			if type(value) == '__list__':
				query = "{}.in({})".format(key, value)
				arg_list.append(query)
			else:
				query = "{}={}".format(key, value)
				arg_list.append(query)

		return db.Model.filter_by(*arg_list)