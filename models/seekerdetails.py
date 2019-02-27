#-------------------------------------------------------------------------------
# Name:        seekerdetails
# Purpose:     Model to map the seekers with their details 
#
# Author:      Siva Samudrala
#
# Created:     13/02/2019
# Copyright:   (c) Hoder Solutions Pvt Ltd 2019
# Licence:     <your licence>
# Sample JSON: {"user":123,"subject":1}
#-------------------------------------------------------------------------------
from root import application, db
from models import *

class Seekerdetails(db.Model):
    __tablename__ =  "seekerdetails"
    id = db.Column(db.Integer, primary_key=True)
    contactnumber = db.Column(db.Integer)
    experience = db.Column(db.Integer)
    currentpack = db.Column(db.Integer)
    expectedpack = db.Column(db.Integer)
    qualification = db.Column(db.Integer, db.ForeignKey('qualifications.id'))
    subject = db.Column(db.Integer, db.ForeignKey('subjects.id'))
    experiences = db.Column(db.String(2000))
    address = db.Column(db.String(2000))
    district = db.Column(db.Integer, db.ForeignKey('districts.id'))
    state = db.Column(db.Integer, db.ForeignKey('states.id'))
    medium = db.Column(db.Integer)
    user = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def serialize(self):
        json_user = {
            "id": self.id,
            "Contact Number": self.contactnumber,
            #"registered_on": str(self.registered_on),
            "Experience": self.experience,
            "Current Package": self.currentpack,
            "Qualification": self.qualification,
           # "Experience History": self.experiences,
            #"Address": self.address,
            "District": self.district,
            "State": self.state,
            "Medium": self.medium,
        }
        return json_user
