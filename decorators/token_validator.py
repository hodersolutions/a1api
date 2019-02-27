from flask import request, Response
from json import dumps
from functools import wraps
from jwt import decode

def token_required(f):
	@wraps(f)
	def wrapper(*args, **kwargs):
		if "token" in request.headers and "username" in request.headers:
			token = request.headers['token']
			username = request.headers['username']
			try:
				decode(token, username)
				return f(*args, **kwargs)
			except:
				errorObj = {
					"status": "failure",
					"message": "Invalid access, please sign-in first to view this page."
				}
				return Response(dumps(errorObj), 401, mimetype="application/json")
		else:
			errorObj = {
				"status": "failure",
				"message": "Invalid access, please sign-in first to view this page."
			}
			return Response(dumps(errorObj), 401, mimetype="application/json")
	return wrapper