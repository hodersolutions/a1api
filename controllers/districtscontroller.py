from flask import request, Response
from json import dumps, loads
from root import application
from models.districts import *
# from models.options import *
from decorators import *

@application.route("/api/v1/districts/all", methods=["GET"])
def api_districts_all():
    responseObject = {
        "status": "success",
        "message": "Retrieved all districts successfully.",            
        "object": Districts.get_all_districts()
    }
    return Response(dumps(responseObject), 200, mimetype='application/json')

@application.route("/api/v1/districts", methods=["GET"])
def api_districts():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        responseObject = {
            "status": "failure",
            "message": "Failed to retrieve an Invalid District, no (id) field provided. please specify an (id)."
        }
        return Response(dumps(responseObject), 400, mimetype='application/json')

    district = Districts.get_district_from_id(id)
    responseObject = {
        "status": "success",
        "message": "District retrieved successfully.",            
        "district": district.serialize()
    }
    return Response(dumps(responseObject), 200, mimetype='application/json')

@application.route("/api/v1/district/<int:id>", methods=["GET"])
def api_district_via_id(id):
    district = Districts.get_district_from_id(id)
    if district.id < 0:
        responseObject = {
            "status": "failure",
            "message": "Failed to retrieve an Invalid district."                
        }
        return Response(dumps(responseObject), 400, mimetype='application/json')
    responseObject = {
        "status": "success",
        "message": "District retrieved successfully.",            
        "district": district.serialize()
    }
    return Response(dumps(responseObject), 200, mimetype='application/json')

@application.route("/api/v1/districts", methods=["POST"])
#@token_required
def api_add_district():
    request_data = request.get_json()
    if(Districts.validate_district(request_data)):
        district = Districts.submit_district_from_json(request_data)
        if district is None or district.id < 0:
            responseObject = {
                "status": "failure",
                "message": "Failed to add an Invalid District."                
            }
            return Response(dumps(responseObject), 500, mimetype='application/json')
        responseObject = {
            "status": "success",
            "message": "District added successfully.",            
            "district": district.serialize()
        }
        return Response(dumps(responseObject), 201, mimetype='application/json')
    else:
        responseObject = {
            "status": "failure",
            "message": "Failed to add an Invalid District."                
        }
        return Response(dumps(responseObject), 400, mimetype='application/json')

# 
@application.route("/api/v1/district/<int:id>", methods=["DELETE"])
@token_required
def api_delete_district_via_id(id):
    subbject = Districts.delete_question_from_id(id)
    if question is None or question.id < 0:
        responseObject = {
            "status": "failure",
            "message": "Failed to delete an Invalid District."                
        }
        return Response(dumps(responseObject), 404, mimetype='application/json')

    responseObject = {
        "status": "success",
        "message": "District deleted successfully.",            
        "district": district.serialize()
    }
    return Response(dumps(responseObject), 201, mimetype='application/json')