from flask import request, Response
from json import dumps, loads
from root import application
from models.jobs import *
# from models.options import *
from decorators import *

@application.route("/api/v1/jobs/filter", methods=["GET"])
def api_jobs_all():
    filter_dict = request.args.to_dict()
    print(filter_dict)
    
    responseObject = {
        "status": "success",
        "message": "Retrieved all jobs successfully.",            
        "object": Jobs.get_jobs_by_filter(filter_dict)
    }
    return Response(dumps(responseObject), 200, mimetype='application/json')

@application.route("/api/v1/jobs", methods=["GET"])
def api_jobs():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        responseObject = {
            "status": "failure",
            "message": "Failed to retrieve an Invalid Qualificaiton, no (id) field provided. please specify an (id)."
        }
        return Response(dumps(responseObject), 400, mimetype='application/json')

    job = Jobs.get_job_from(id)
    responseObject = {
        "status": "success",
        "message": "Job retrieved successfully.",            
        "job": job.serialize()
    }
    return Response(dumps(responseObject), 200, mimetype='application/json')

@application.route("/api/v1/job/<int:id>", methods=["GET"])
def api_job_via(id):
    job = Jobs.query.get(id)
    if job.id < 0:
        responseObject = {
            "status": "failure",
            "message": "Failed to retrieve an Invalid job."                
        }
        return Response(dumps(responseObject), 400, mimetype='application/json')
    responseObject = {
        "status": "success",
        "message": "Job retrieved successfully.",            
        "job": job.serialize()
    }
    return Response(dumps(responseObject), 200, mimetype='application/json')

@application.route("/api/v1/jobs", methods=["POST"])
#@token_required
def api_add_job():
    request_data = request.form.to_dict()
    print(request_data["body"])
    #request_data = dict(request_data["body"])
    request_data = loads(request_data["body"])
    if(True):
        job = Jobs.submit_job_from_json(request_data)
        if job is None or job.id < 0:
            responseObject = {
                "status": "failure",
                "message": "Failed to add an Invalid Job."                
            }
            return Response(dumps(responseObject), 500, mimetype='application/json')
        responseObject = {
            "status": "success",
            "message": "Job added successfully.",            
            "job": job.serialize()
        }
        return Response(dumps(responseObject), 201, mimetype='application/json')
    else:
        responseObject = {
            "status": "failure",
            "message": "Failed to add an Invalid Job."                
        }
        return Response(dumps(responseObject), 400, mimetype='application/json')

# 
@application.route("/api/v1/job/<int:id>", methods=["DELETE"])
@token_required
def api_delete_job_via(id):
    subbject = Jobs.delete_question_from(id)
    if question is None or question.id < 0:
        responseObject = {
            "status": "failure",
            "message": "Failed to delete an Invalid Job."                
        }
        return Response(dumps(responseObject), 404, mimetype='application/json')

    responseObject = {
        "status": "success",
        "message": "Job deleted successfully.",            
        "job": job.serialize()
    }
    return Response(dumps(responseObject), 201, mimetype='application/json')