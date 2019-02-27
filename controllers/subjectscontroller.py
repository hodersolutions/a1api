from flask import request, Response
from json import dumps, loads
from root import application
from models.subjects import *
# from models.options import *
from decorators import *

@application.route("/api/v1/subjects/all", methods=["GET"])
def api_subjects_all():
    responseObject = {
        "status": "success",
        "message": "Retrieved all subjects successfully.",            
        "object": Subjects.get_all_subjects()
    }
    return Response(dumps(responseObject), 200, mimetype='application/json')

@application.route("/api/v1/subjects", methods=["GET"])
def api_subjects():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        responseObject = {
            "status": "failure",
            "message": "Failed to retrieve an Invalid Question, no (id) field provided. please specify an (id)."
        }
        return Response(dumps(responseObject), 400, mimetype='application/json')

    subject = Subjects.get_subject_from_id(id)
    responseObject = {
        "status": "success",
        "message": "Subject retrieved successfully.",            
        "subject": subject.serialize()
    }
    return Response(dumps(responseObject), 200, mimetype='application/json')

@application.route("/api/v1/subject/<int:id>", methods=["GET"])
def api_subject_via_id(id):
    subject = Subjects.get_subject_from_id(id)
    if subject.id < 0:
        responseObject = {
            "status": "failure",
            "message": "Failed to retrieve an Invalid subject."                
        }
        return Response(dumps(responseObject), 400, mimetype='application/json')
    responseObject = {
        "status": "success",
        "message": "Subject retrieved successfully.",            
        "subject": subject.serialize()
    }
    return Response(dumps(responseObject), 200, mimetype='application/json')

@application.route("/api/v1/subjects", methods=["POST"])
#@token_required
def api_add_subject():
    request_data = request.get_json()
    if(Subjects.validate_subject(request_data)):
        subject = Subjects.submit_subject_from_json(request_data)
        if subject is None or subject.id < 0:
            responseObject = {
                "status": "failure",
                "message": "Failed to add an Invalid Subject."                
            }
            return Response(dumps(responseObject), 500, mimetype='application/json')
        responseObject = {
            "status": "success",
            "message": "Subject added successfully.",            
            "subject": subject.serialize()
        }
        return Response(dumps(responseObject), 201, mimetype='application/json')
    else:
        responseObject = {
            "status": "failure",
            "message": "Failed to add an Invalid Subject."                
        }
        return Response(dumps(responseObject), 400, mimetype='application/json')

# 
@application.route("/api/v1/subject/<int:id>", methods=["DELETE"])
@token_required
def api_delete_subject_via_id(id):
    subbject = Subjects.delete_question_from_id(id)
    if question is None or question.id < 0:
        responseObject = {
            "status": "failure",
            "message": "Failed to delete an Invalid Subject."                
        }
        return Response(dumps(responseObject), 404, mimetype='application/json')

    responseObject = {
        "status": "success",
        "message": "Subject deleted successfully.",            
        "subject": subject.serialize()
    }
    return Response(dumps(responseObject), 201, mimetype='application/json')