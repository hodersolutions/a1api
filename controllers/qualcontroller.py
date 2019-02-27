from flask import request, Response
from json import dumps, loads
from root import application
from models.qualifications import *
# from models.options import *
from decorators import *

@application.route("/api/v1/qualifications/all", methods=["GET"])
def api_qualifications_all():
    responseObject = {
        "status": "success",
        "message": "Retrieved all qualifications successfully.",            
        "object": Qualifications.get_all_qualifications()
    }
    return Response(dumps(responseObject), 200, mimetype='application/json')

@application.route("/api/v1/qualifications", methods=["GET"])
def api_qualifications():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        responseObject = {
            "status": "failure",
            "message": "Failed to retrieve an Invalid Qualificaiton, no (id) field provided. please specify an (id)."
        }
        return Response(dumps(responseObject), 400, mimetype='application/json')

    qualification = Qualifications.get_qualification_from_id(id)
    responseObject = {
        "status": "success",
        "message": "Qualification retrieved successfully.",            
        "qualification": qualification.serialize()
    }
    return Response(dumps(responseObject), 200, mimetype='application/json')

@application.route("/api/v1/qualification/<int:id>", methods=["GET"])
def api_qualification_via_id(id):
    qualification = Qualifications.get_qualification_from_id(id)
    if qualification.id < 0:
        responseObject = {
            "status": "failure",
            "message": "Failed to retrieve an Invalid qualification."                
        }
        return Response(dumps(responseObject), 400, mimetype='application/json')
    responseObject = {
        "status": "success",
        "message": "Qualification retrieved successfully.",            
        "qualification": qualification.serialize()
    }
    return Response(dumps(responseObject), 200, mimetype='application/json')

@application.route("/api/v1/qualifications", methods=["POST"])
#@token_required
def api_add_qualification():
    request_data = request.get_json()
    if(Qualifications.validate_qualification(request_data)):
        qualification = Qualifications.submit_qualification_from_json(request_data)
        if qualification is None or qualification.id < 0:
            responseObject = {
                "status": "failure",
                "message": "Failed to add an Invalid Qualification."                
            }
            return Response(dumps(responseObject), 500, mimetype='application/json')
        responseObject = {
            "status": "success",
            "message": "Qualification added successfully.",            
            "qualification": qualification.serialize()
        }
        return Response(dumps(responseObject), 201, mimetype='application/json')
    else:
        responseObject = {
            "status": "failure",
            "message": "Failed to add an Invalid Qualification."                
        }
        return Response(dumps(responseObject), 400, mimetype='application/json')

# 
@application.route("/api/v1/qualification/<int:id>", methods=["DELETE"])
@token_required
def api_delete_qualification_via_id(id):
    subbject = Qualifications.delete_question_from_id(id)
    if question is None or question.id < 0:
        responseObject = {
            "status": "failure",
            "message": "Failed to delete an Invalid Qualification."                
        }
        return Response(dumps(responseObject), 404, mimetype='application/json')

    responseObject = {
        "status": "success",
        "message": "Qualification deleted successfully.",            
        "qualification": qualification.serialize()
    }
    return Response(dumps(responseObject), 201, mimetype='application/json')