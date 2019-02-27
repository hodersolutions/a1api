#-------------------------------------------------------------------------------
# Name:     Users
# Purpose:
#
# Author:     Siva Samudrala
#
# Created:   13/02/2019
# Copyright:   (c) Hoder Solutions Pvt Ltd 2018
# Licence:   <your licence>
# Sample JSON:  {"username":"RF","email":"fedex@gmail.com","password":"fedex", "isrecruiter" : 1}
#-------------------------------------------------------------------------------
from root import application, db, bcrypt
#from jwt import encode
from datetime import datetime, timedelta
from models.seekerdetails import Seekerdetails

class Users(db.Model):
	__tablename__ =  "users"
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), nullable=False)
	firstname = db.Column(db.String(80), nullable=True)
	lastname = db.Column(db.String(80), nullable=True)
	email = db.Column(db.String(80), nullable=False)
	password = db.Column(db.String(80), nullable=False)
	registered_on = db.Column(db.DateTime, nullable=False, default=datetime.now())
	isrecruiter = db.Column(db.Boolean, nullable=False, default=False)
	isactive = db.Column(db.Boolean, nullable=False, default=False)
	details = db.relationship('Seekerdetails', backref='enquiry', lazy=True)

	def __repr__(self):
		return '{"username": {0}, "email": {1}, "recruiter": {2} }'.format(self.username, self.email, self.isrecruiter)


	def fullname(self):
		return "{} {}".format(self.firstname, self.lastname)

	@classmethod
	def username_password_match(classname, _email, _password):
		print(_email, _password)
		user = classname.query.filter_by(email=_email).first()
		if user and bcrypt.check_password_hash(user.password, _password):
			print("exists")
			return user
		else:
			print("absent")
			return None

	@classmethod
	def add_user(classname, _user):
		try:
			pw_hash = bcrypt.generate_password_hash(_user.password)
			_user.password = pw_hash
			db.session.add(_user)
			db.session.commit()
		except Exception as e:
			return e

		return classname.get_user_by_username(_user.username)

	@classmethod
	def get_all_users(classname):
		return [user.serialize() for user in classname.query.all()]

	@classmethod
	def get_user_by_username(classname, _username):
		try:
			user_object = classname.query.filter_by(username=_username).first()
			if(user_object == None):
				return user_object
			else:
				return user_object.serialize()
		except:
			return False
	@classmethod
	def get_users_from_text(classname, text):
		query = """select id, Users.firstname, Users.lastname from Users where Users.firstname like "%{}%"
		 or Users.lastname like "%{}%" or Users.username like "%{}%" """.format(text, text, text)
		result = db.engine.execute(query)
		list_result =[]
		for user in result:
			user_dict = {}
			user_dict['id'] = user[0]
			user_dict['label'] = "{} {}".format(user[1], user[2])
			list_result.append(user_dict)
		return list_result


	@classmethod
	def get_user_by_email(classname, _email):
		try:
			user_object = classname.query.filter_by(email=_email).first()
			if(user_object == None):
				return user_object
			else:
				return user_object.serialize()
		except:
			return False

	@classmethod
	def get_user_by(classname, id):
		user_object = classname.query.get(id)
		if(user_object == None):
			return None
		else:
			return user_object

	@classmethod
	def delete_user_by_username(classname, _username):
		try:
			classname.query.filter_by(username=_username).delete()
			db.session.commit()
		except:
			return False

		return True


	@classmethod
	def update_user_by_username(classname, _username, _user):
		try:
			user_to_update = classname.query.filter_by(username=_username).first()
			user_to_update.email = _user.email
			user_to_update.password = _user.password
			db.session.commit()
		except:
			return False

		return classname.get_user_by_username(_user.username)

	@staticmethod
	def validate_user(user):
		if ("username" in user and "email" in user and "password" in user):
			return True
		else:
			return False

	def encode_auth_token(self):
		"""
		Generates the Auth Token
		:return: string
		"""
		try:
			header = {
				"alg": "HS256",
				"typ": "JWT"
			}
			# Max value = timedelta(days=999999999, hours=23, minutes=59, seconds=59, microseconds=999999)
			payload = {
				"exp": datetime.utcnow() + timedelta(days=2, hours=0, minutes=0, seconds=0, microseconds=0),
				"iat": datetime.utcnow(),
				"sub": self.id,
				"name": self.username
			}
			#return encode(payload, self.username, headers=header)
			return "hshhdhdsjlhlfdjh"
		except Exception as e:
			return e

	@classmethod
	def get_users_by_filter(classname, filter):
		query = "select * from Users inner join seekerdetails on Users.id = Seekerdetails.user where "
		for key, value in filter.items():
			query = "{} Seekerdetails.{} = {}".format(query, key, value)
		print(query)
		result = db.engine.execute(query)
		list_result =[]
		for job in result:
			job_object = dict(zip(result.keys(), job))
			list_result.append(User.serialize_dict(job_object))

		return list_result

	def serialize(self):
		json_user = {
			"id": self.id,
			"Username": self.username,
			"Email": self.email,
			#"registered_on": str(self.registered_on),
			"Recruiter": self.isrecruiter,
			"Fullname": self.fullname(),
			"details" : [detail.serialize() for detail in self.details]

		}
		return json_user

############################################################################################
#All the functions to retrieve seeker details and update them
############################################################################################
	def update_user(self, details):
		db.session.add(self)
		db.session.add(details)
		db.session.commit()
