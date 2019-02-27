#-------------------------------------------------------------------------------
# Name:        Qualifications
# Purpose:
#
# Author:      Siva Samudrala
#
# Created:     13/02/2019
# Copyright:   (c) Hoder Solutions Pvt Ltd 2019
# Licence:     <your licence>
# Sample JSON: {"qualification":"English", "id":1}
#-------------------------------------------------------------------------------
from root import db
# from models.options import Options

class Qualifications(db.Model):
    __tablename__ =  "qualifications"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    qualification = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return '{"id":{0}, "qualification":{1}}'.format(self.id, self.qualification)

    @classmethod
    def get_all_qualifications(classname):
        qualifications = Qualifications.query.all()
        qualifications_json = [qualification.serialize() for qualification in qualifications]
        return qualifications_json

    @classmethod
    def get_qualification_from(classname, id):
        qualification = classname.query.get(id)
        return qualification

    @classmethod
    def delete_qualification_from(classname, id):
        qualification = classname.get_qualification_from(id)
        if qualification is None:
            return None
        db.session.delete(qualification)
        db.session.commit()
        return qualification

    @classmethod
    def submit_qualification_from_json(classname, json_qualification):
        qualification = classname(qualification=json_qualification['qualification'])
        db.session.add(qualification)
        db.session.commit()
        return qualification

    #todo:json encoding needed
    def serialize(self):
        json_qualification = {
        'id' : self.id ,
        'name' : self.qualification,
        }
        return json_qualification

    @staticmethod
    def validate_qualification(qualification):
        if ('qualification' in qualification):
            return True
        else:
            return False