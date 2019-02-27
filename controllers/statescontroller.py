from flask import request, Response
from json import dumps, loads
from root import application
from models.states import *
# from models.options import *
from decorators import *

@application.route("/api/v1/states/all", methods=["GET"])
def api_states_all():
    responseObject = {
        "status": "success",
        "message": "Retrieved all states successfully.",            
        "object": States.get_all_states()
    }
    return Response(dumps(responseObject), 200, mimetype='application/json')

@application.route("/api/v1/states", methods=["GET"])
def api_states():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        responseObject = {
            "status": "failure",
            "message": "Failed to retrieve an Invalid State, no (id) field provided. please specify an (id)."
        }
        return Response(dumps(responseObject), 400, mimetype='application/json')

    state = States.get_state_from_id(id)
    responseObject = {
        "status": "success",
        "message": "State retrieved successfully.",            
        "state": state.serialize()
    }
    return Response(dumps(responseObject), 200, mimetype='application/json')

@application.route("/api/v1/state/<int:id>", methods=["GET"])
def api_state_via_id(id):
    state = States.get_state_from_id(id)
    if state.id < 0:
        responseObject = {
            "status": "failure",
            "message": "Failed to retrieve an Invalid state."                
        }
        return Response(dumps(responseObject), 400, mimetype='application/json')
    responseObject = {
        "status": "success",
        "message": "State retrieved successfully.",            
        "state": state.serialize()
    }
    return Response(dumps(responseObject), 200, mimetype='application/json')

@application.route("/api/v1/states", methods=["POST"])
#@token_required
def api_add_state():
    request_data = request.get_json()
    if(States.validate_state(request_data)):
        state = States.submit_state_from_json(request_data)
        if state is None or state.id < 0:
            responseObject = {
                "status": "failure",
                "message": "Failed to add an Invalid State."                
            }
            return Response(dumps(responseObject), 500, mimetype='application/json')
        responseObject = {
            "status": "success",
            "message": "State added successfully.",            
            "state": state.serialize()
        }
        return Response(dumps(responseObject), 201, mimetype='application/json')
    else:
        responseObject = {
            "status": "failure",
            "message": "Failed to add an Invalid State."                
        }
        return Response(dumps(responseObject), 400, mimetype='application/json')

# 
@application.route("/api/v1/state/<int:id>", methods=["DELETE"])
@token_required
def api_delete_state_via_id(id):
    subbject = States.delete_question_from_id(id)
    if question is None or question.id < 0:
        responseObject = {
            "status": "failure",
            "message": "Failed to delete an Invalid State."                
        }
        return Response(dumps(responseObject), 404, mimetype='application/json')

    responseObject = {
        "status": "success",
        "message": "State deleted successfully.",            
        "state": state.serialize()
    }
    return Response(dumps(responseObject), 201, mimetype='application/json')