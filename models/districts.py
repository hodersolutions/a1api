#-------------------------------------------------------------------------------
# Name:        Districts
# Purpose:
#
# Author:      Siva Samudrala
#
# Created:     13/02/2019
# Copyright:   (c) Hoder Solutions Pvt Ltd 2019
# Licence:     <your licence>
# Sample JSON: {"district":"English", "id":1}
#-------------------------------------------------------------------------------
from root import db
# from models.options import Options

class Districts(db.Model):
    __tablename__ =  "districts"
    id = db.Column(db.Integer, primary_key=True)
    district = db.Column(db.String(200), nullable=False)
    state = db.Column(db.Integer)

    def __repr__(self):
        return '{"id":{0}, "district":{1}}'.format(self.id, self.district)

    @classmethod
    def get_all_districts(classname):
        districts = Districts.query.all()
        districts_json = [district.serialize() for district in districts]
        return districts_json

    @classmethod
    def get_district_from(classname, id):
        district = classname.query.get(id)
        return district

    @classmethod
    def delete_district_from(classname, id):
        district = classname.get_district_from(id)
        if district is None:
            return None
        db.session.delete(district)
        db.session.commit()
        return district

    @classmethod
    def submit_district_from_json(classname, json_district):
        district = classname(district=json_district['district'], state=json_district.get("state", 0))
        db.session.add(district)
        db.session.commit()
        return district

    #todo:json encoding needed
    def serialize(self):
        json_district = {
        'id' : self.id ,
        'name' : self.district,
        }
        return json_district

    @staticmethod
    def validate_district(district):
        if ('district' in district):
            return True
        else:
            return False