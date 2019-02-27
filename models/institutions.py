#-------------------------------------------------------------------------------
# Name:        Institutions
# Purpose:
#
# Author:      Siva Samudrala
#
# Created:     13/02/2019
# Copyright:   (c) Hoder Solutions Pvt Ltd 2019
# Licence:     <your licence>
# Sample JSON: {"institution":"English", "id":1}
#-------------------------------------------------------------------------------
from root import db
# from models.options import Options

class Institutions(db.Model):
    __tablename__ =  "institutions"
    id = db.Column(db.Integer, primary_key=True)
    district = db.Column(db.Integer)
    institution = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return '{"id":{0}, "institution":{1}}'.format(self.id, self.institution)

    @classmethod
    def get_all_institutions(classname):
        institutions = Institutions.query.all()
        institutions_json = [institution.serialize() for institution in institutions]
        return institutions_json

    @classmethod
    def get_institution_from(classname, id):
        institution = classname.query.get(id)
        return institution

    @classmethod
    def delete_institution_from(classname, id):
        institution = classname.get_institution_from(id)
        if institution is None:
            return None
        db.session.delete(institution)
        db.session.commit()
        return institution

    @classmethod
    def submit_institution_from_json(classname, json_institution):
        institution = classname(institution=json_institution['institution'], district=json_institution["district"])
        db.session.add(institution)
        db.session.commit()
        return institution

    #todo:json encoding needed
    def serialize(self):
        json_institution = {
        'id' : self.id ,
        'institution' : self.institution,
        }
        return json_institution

    @staticmethod
    def validate_institution(institution):
        if ('institution' in institution):
            return True
        else:
            return False