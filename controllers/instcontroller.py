from flask import request, Response
from json import dumps, loads
from root import application
from models.institutions import *
# from models.options import *
from decorators import *

@application.route("/api/v1/institutions/all", methods=["GET"])
def api_institutions_all():
    responseObject = {
        "status": "success",
        "message": "Retrieved all institutions successfully.",            
        "object": Institutions.get_all_institutions()
    }
    return Response(dumps(responseObject), 200, mimetype='application/json')

@application.route("/api/v1/institutions", methods=["GET"])
def api_institutions():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        responseObject = {
            "status": "failure",
            "message": "Failed to retrieve an Invalid Qualificaiton, no (id) field provided. please specify an (id)."
        }
        return Response(dumps(responseObject), 400, mimetype='application/json')

    institution = Institutions.get_institution_from_id(id)
    responseObject = {
        "status": "success",
        "message": "Institution retrieved successfully.",            
        "institution": institution.serialize()
    }
    return Response(dumps(responseObject), 200, mimetype='application/json')

@application.route("/api/v1/institution/<int:id>", methods=["GET"])
def api_institution_via_id(id):
    institution = Institutions.get_institution_from_id(id)
    if institution.id < 0:
        responseObject = {
            "status": "failure",
            "message": "Failed to retrieve an Invalid institution."                
        }
        return Response(dumps(responseObject), 400, mimetype='application/json')
    responseObject = {
        "status": "success",
        "message": "Institution retrieved successfully.",            
        "institution": institution.serialize()
    }
    return Response(dumps(responseObject), 200, mimetype='application/json')

@application.route("/api/v1/institutions", methods=["POST"])
#@token_required
def api_add_institution():
    request_data = request.get_json()
    if(Institutions.validate_institution(request_data)):
        institution = Institutions.submit_institution_from_json(request_data)
        if institution is None or institution.id < 0:
            responseObject = {
                "status": "failure",
                "message": "Failed to add an Invalid Institution."                
            }
            return Response(dumps(responseObject), 500, mimetype='application/json')
        responseObject = {
            "status": "success",
            "message": "Institution added successfully.",            
            "institution": institution.serialize()
        }
        return Response(dumps(responseObject), 201, mimetype='application/json')
    else:
        responseObject = {
            "status": "failure",
            "message": "Failed to add an Invalid Institution."                
        }
        return Response(dumps(responseObject), 400, mimetype='application/json')

# 
@application.route("/api/v1/institution/<int:id>", methods=["DELETE"])
@token_required
def api_delete_institution_via_id(id):
    subbject = Institutions.delete_question_from_id(id)
    if question is None or question.id < 0:
        responseObject = {
            "status": "failure",
            "message": "Failed to delete an Invalid Institution."                
        }
        return Response(dumps(responseObject), 404, mimetype='application/json')

    responseObject = {
        "status": "success",
        "message": "Institution deleted successfully.",            
        "institution": institution.serialize()
    }
    return Response(dumps(responseObject), 201, mimetype='application/json')