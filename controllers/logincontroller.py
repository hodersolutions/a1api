from root import application
from flask import request, Response
from json import dumps, loads
from models.users import *
from flask_cors import CORS, cross_origin

@application.route("/api/v1/auth/login", methods=["POST"])
def get_token():
	request_data = request.form.to_dict()
	try:
		print("Hello")
		request_data = loads(request_data["body"])
		email = request_data["email"]
		password = request_data["password"]
		print(request_data)
		user = Users.username_password_match(email, password)
		if user:
			auth_token = user.encode_auth_token()
			responseObject = {
				"status": "success",
				"message": "Login Success.",
				"auth_token": auth_token.decode(),
				"username": user.username,
				"id" : user.id,
				"recruiter" : user.isrecruiter
			}
			print(responseObject)
			return Response(dumps(responseObject), 201, mimetype="application/json")
		else:
			responseObject = {
				"status": "failure",
				"message": "Login failed. Please try again.",
			}
			print(responseObject)
			return Response(dumps(responseObject), 401, mimetype="application/json")
	except Exception as e:
		print("No")
		responseObject = {
			"status": "failure",
			"message": "Some error occured. Please try again."
		}
		return Response(dumps(responseObject), 401, mimetype="application/json")