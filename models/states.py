#-------------------------------------------------------------------------------
# Name:        States
# Purpose:
#
# Author:      Siva Samudrala
#
# Created:     13/02/2019
# Copyright:   (c) Hoder Solutions Pvt Ltd 2019
# Licence:     <your licence>
# Sample JSON: {"state":"English", "id":1}
#-------------------------------------------------------------------------------
from root import db
# from models.options import Options

class States(db.Model):
    __tablename__ =  "states"
    id = db.Column(db.Integer, primary_key=True)
    state = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return '{"id":{0}, "state":{1}}'.format(self.id, self.state)

    @classmethod
    def get_all_states(classname):
        states = States.query.all()
        states_json = [state.serialize() for state in states]
        return states_json

    @classmethod
    def get_state_from(classname, id):
        state = classname.query.get(id)
        return state

    @classmethod
    def delete_state_from(classname, id):
        state = classname.get_state_from(id)
        if state is None:
            return None
        db.session.delete(state)
        db.session.commit()
        return state

    @classmethod
    def submit_state_from_json(classname, json_state):
        state = classname(state=json_state['state'])
        db.session.add(state)
        db.session.commit()
        return state

    #todo:json encoding needed
    def serialize(self):
        json_state = {
        'id' : self.id ,
        'state' : self.state,
        }
        return json_state

    @staticmethod
    def validate_state(state):
        if ('state' in state):
            return True
        else:
            return False