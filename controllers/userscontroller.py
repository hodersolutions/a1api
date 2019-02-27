from flask import request, Response
from json import dumps, loads
from root import application
from models.users import *
from models.seekerdetails import *
#from decorators import *
from flask_cors import CORS, cross_origin
#---------------------------------------Valiate Token----------------------------------------------#

@application.route("/api/v1/token/validate", methods=["GET"])
#@token_required
def api_token_validate():
    responseObject = {
        "status": "success",
        "message": "Token Valid.",
        "token": True
    }
    return Response(dumps(responseObject), 200, mimetype='application/json')

#---------------------------------------GET all users----------------------------------------------#

@application.route("/api/v1/users/all", methods=["GET"])
#@token_required
def api_users_all():
    responseObject = {
        "status": "success",
        "message": "Users found.",
        "user": Users.get_all_users()
    }
    return Response(dumps(responseObject), 200, mimetype='application/json')

@application.route("/api/v1/users/filter", methods=["GET"])
def api_users_filter():
    filter_dict = request.args.to_dict()
    print(filter_dict)
    
    responseObject = {
        "status": "success",
        "message": "Retrieved all profiles successfully.",            
        "object": Users.get_users_by_filter(filter_dict)
    }
    return Response(dumps(responseObject), 200, mimetype='application/json')
#---------------------------GET user by username from query string---------------------------------#

@application.route("/api/v1/users/username", methods=["GET"])
#@token_required
def api_user_by_username():
    if 'username' in request.args:
        username = request.args['username']
    else:
        responseObject = {
            "status": "failure",
            "message": "Error: No username field provided. Please specify an username."
        }
        response = Response(dumps(responseObject), 400, mimetype='application/json')

    user = Users.get_user_by_username(username)
    if user == None:
        responseObject = {
            "status": "failure",
            "message": "User not found.",
            "user": user
        }
    else:
        responseObject = {
            "status": "success",
            "message": "User found.",
            "user": user
        }
    return Response(dumps(responseObject), 200, mimetype='application/json')

@application.route("/api/v1/user/<int:id>", methods=["GET"])
#@token_required
def api_user_by_id(id):
    user = Users.query.get(id)
    details =  user.details
    if user == None:
        responseObject = {
            "status": "failure",
            "message": "User not found.",
            "user": user
        }
    else:
        responseObject = {
            "status": "success",
            "message": "User found.",
            "user": user.serialize()
        }
    return Response(dumps(responseObject), 200, mimetype='application/json')

@application.route("/api/v1/users/search/<string:text>", methods=["GET"])
#@token_required
def api_users_by_text(text):
    result = Users.get_users_from_text(text)
    if result == None:
        responseObject = {
            "status": "failure",
            "message": "User not found.",
            "user": user
        }
    else:
        responseObject = {
            "status": "success",
            "message": "User found.",
            "options": result
        }
    return Response(dumps(responseObject), 200, mimetype='application/json')

#---------------------------GET user by username from query string---------------------------------#

@application.route("/api/v1/users/username/exist", methods=["GET"])
def api_user_by_username_exist():
    if 'username' in request.args:
        username = request.args['username']
    else:
        responseObject = {
            "status": "no",
            "message": "Error: No username field provided. Please specify an username."
        }
        response = Response(dumps(responseObject), 400, mimetype='application/json')

    user = Users.get_user_by_username(username)
    if user == None:
        responseObject = {
            "status": "no",
            "message": "User not found."
        }
    else:
        responseObject = {
            "status": "yes",
            "message": "User found."
        }
    return Response(dumps(responseObject), 200, mimetype='application/json')

#-----------------------------GET user by email from query string----------------------------------#

@application.route("/api/v1/users/email", methods=["GET"])
#@token_required
def api_user_by_email():
    if 'email' in request.args:
        email = request.args['email']
    else:
        responseObject = {
            "status": "failure",
            "message": "Error: No email field provided. Please specify an email."
        }
        response = Response(dumps(responseObject), 400, mimetype='application/json')
    
    user = Users.get_user_by_email(email)
    if user == None:
        responseObject = {
            "status": "failure",
            "message": "User not found.",
            "user": user
        }
    else:
        responseObject = {
            "status": "success",
            "message": "User found.",
            "user": user
        }
    return Response(dumps(responseObject), 200, mimetype='application/json')

#-----------------------------GET user by email from query string----------------------------------#

@application.route("/api/v1/users/email/exist", methods=["GET"])
def api_user_by_email_exist():
    if 'email' in request.args:
        email = request.args['email']
    else:
        responseObject = {
            "status": "no",
            "message": "Error: No email field provided. Please specify an email."
        }
        response = Response(dumps(responseObject), 400, mimetype='application/json')
    
    user = Users.get_user_by_email(email)
    if user == None:
        responseObject = {
            "status": "no",
            "message": "User not found."
        }
    else:
        responseObject = {
            "status": "yes",
            "message": "User found."
        }
    return Response(dumps(responseObject), 200, mimetype='application/json')

#---------------------------GET user by username from url extension--------------------------------#

@application.route("/api/v1/users/<string:username>", methods=["GET"])
def api_user_via_username(username):
    responseObject = {
        'status': 'success',
        'message': 'Successfully registered.',
        'user': Users.get_user_by_username(username)
    }
    return Response(dumps(responseObject), 200, mimetype='application/json')

#------------------------------------------POST user-----------------------------------------------#

@application.route("/api/v1/users", methods=["POST"])
#@cross_origin(origin='localhost', headers=['Content- Type','Authorization'])
def api_add_user():
    request_data = request.form.to_dict()
    print(request.form)
    print(request_data["body"])
    #request_data = dict(request_data["body"])
    request_data = loads(request_data["body"])
    print(type(request_data))
    if(Users.validate_user(request_data)):
        new_user = Users()
        new_user.username = request_data["username"]
        new_user.password = request_data["password"]
        new_user.email = request_data["email"]
        new_user.isrecruiter = request_data["recruiter"]
        #To Do: add admin from client
        responseObject = {
            'status': 'success',
            'message': 'Successfully registered.',
            'user': Users.add_user(new_user)
        }
        print(responseObject)
        response = Response(dumps(responseObject), 201, mimetype='application/json')
        return response
    else:
        responseObject = {
            'status': 'fail',
            'message': 'Failed to registered the user.',
            'user': None
        }
        response = Response(dumps(responseObject), 400, mimetype='application/json')
        return response

#-----------------------------------------DELETE user----------------------------------------------#
@application.route("/api/v1/users/<string:username>/details", methods=["POST"])
#@cross_origin(origin='localhost', headers=['Content- Type','Authorization'])
def api_add_userdetails(username):
    user_dict = Users.get_user_by_username(username)
    user = None
    if user_dict is None:
        responseObject = {
            'status': 'fail',
            'message': 'User Not Found. Failed to Update the user.',
            'user': None
        }
        response = Response(dumps(responseObject), 400, mimetype='application/json')
        return response

    user = Users.query.get(user_dict['id'])
    seekerdetailslist = user.details
    seekerdetails = None
    if len(seekerdetailslist)==0:
        seekerdetails = Seekerdetails()
    else:
        seekerdetails = seekerdetailslist[0]
    request_data = request.form.to_dict()
    request_data = dict(loads(request_data["body"]))
    if(request_data is not None):
        firstname = request_data.get("firstname", None)
        if firstname is not None:
            user.firstname = firstname
        lastname = request_data.get("lastname", None)
        if lastname is not None:
            user.lastname = lastname
        contactemail = request_data.get("contactemail", None)
        if contactemail is not None:
            user.email = contactemail
        phoneno = request_data.get("phoneno", None)
        if phoneno is not None:
            seekerdetails.contactnumber = phoneno
        address = request_data.get("address", None)
        if address is not None:
            seekerdetails.address = dumps(address)
        qualification = request_data.get("qualification", None)
        if qualification is not None:
            seekerdetails.qualification = qualification
        subject = request_data.get("subject", None)
        if subject is not None: 
            seekerdetails.subject = subject
        district = request_data.get("district", None)
        if district is not None:
            seekerdetails.district = district
        state = request_data.get("state", None)
        if state is not None:
            seekerdetails.state = state
        medium = request_data.get("medium", None)
        if medium is not None:
            seekerdetails.medium = medium
        experience = request_data.get("experience", None)
        if experience is not None:
            seekerdetails.experience = experience
        experiences = request_data.get("experiences", None)
        if experiences is not None:
            seekerdetails.experiences = dumps(experiences)
        currentpack = request_data.get("currentpack", None)
        if currentpack is not None:
            seekerdetails.currentpack = currentpack
        expectedpack = request_data.get("expectedpack", None)
        if expectedpack is not None:
            seekerdetails.expectedpack = expectedpack
        seekerdetails.user = user.id
        responseObject = {
            'status': 'success',
            'message': 'Successfully updated user details.',
            'user': user.update_user(seekerdetails)
        }
        print(responseObject)
        response = Response(dumps(responseObject), 201, mimetype='application/json')
        return response
    else:
        responseObject = {
            'status': 'fail',
            'message': 'Failed to registered the user.',
            'user': None
        }
        response = Response(dumps(responseObject), 400, mimetype='application/json')
        return response
#-----------------------------------------DELETE user----------------------------------------------#

@application.route("/api/v1/users/<string:username>", methods=["DELETE"])
def api_delete_user_via_username(username):
    responseObject = {
        'status': 'success',
        'message': 'Successfully deleted user.',
        'user': Users.delete_user_by_username(username)
    }
    response = Response(dumps(responseObject), 201, mimetype='application/json')
    return response

#--------------------------------------------------------------------------------------------------#