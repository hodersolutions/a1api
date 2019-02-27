from flask import request, Response
from json import dumps, loads
from root import application
from models.towns import *
# from models.options import *
from decorators import *

@application.route("/api/v1/towns/all", methods=["GET"])
def api_towns_all():
    responseObject = {
        "status": "success",
        "message": "Retrieved all towns successfully.",            
        "question": Towns.get_all_towns()
    }
    return Response(dumps(responseObject), 200, mimetype='application/json')

@application.route("/api/v1/towns", methods=["GET"])
def api_towns():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        responseObject = {
            "status": "failure",
            "message": "Failed to retrieve an Invalid Town, no (id) field provided. please specify an (id)."
        }
        return Response(dumps(responseObject), 400, mimetype='application/json')

    town = Towns.get_town_from_id(id)
    responseObject = {
        "status": "success",
        "message": "Town retrieved successfully.",            
        "town": town.serialize()
    }
    return Response(dumps(responseObject), 200, mimetype='application/json')

@application.route("/api/v1/town/<int:id>", methods=["GET"])
def api_town_via_id(id):
    town = Towns.get_town_from_id(id)
    if town.id < 0:
        responseObject = {
            "status": "failure",
            "message": "Failed to retrieve an Invalid town."                
        }
        return Response(dumps(responseObject), 400, mimetype='application/json')
    responseObject = {
        "status": "success",
        "message": "Town retrieved successfully.",            
        "town": town.serialize()
    }
    return Response(dumps(responseObject), 200, mimetype='application/json')

@application.route("/api/v1/towns", methods=["POST"])
#@token_required
def api_add_town():
    request_data = request.get_json()
    if(Towns.validate_town(request_data)):
        town = Towns.submit_town_from_json(request_data)
        if town is None or town.id < 0:
            responseObject = {
                "status": "failure",
                "message": "Failed to add an Invalid Town."                
            }
            return Response(dumps(responseObject), 500, mimetype='application/json')
        responseObject = {
            "status": "success",
            "message": "Town added successfully.",            
            "town": town.serialize()
        }
        return Response(dumps(responseObject), 201, mimetype='application/json')
    else:
        responseObject = {
            "status": "failure",
            "message": "Failed to add an Invalid Town."                
        }
        return Response(dumps(responseObject), 400, mimetype='application/json')

# 
@application.route("/api/v1/town/<int:id>", methods=["DELETE"])
@token_required
def api_delete_town_via_id(id):
    subbject = Towns.delete_question_from_id(id)
    if question is None or question.id < 0:
        responseObject = {
            "status": "failure",
            "message": "Failed to delete an Invalid Town."                
        }
        return Response(dumps(responseObject), 404, mimetype='application/json')

    responseObject = {
        "status": "success",
        "message": "Town deleted successfully.",            
        "town": town.serialize()
    }
    return Response(dumps(responseObject), 201, mimetype='application/json')