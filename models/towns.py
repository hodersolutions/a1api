#-------------------------------------------------------------------------------
# Name:        Towns
# Purpose:
#
# Author:      Siva Samudrala
#
# Created:     13/02/2019
# Copyright:   (c) Hoder Solutions Pvt Ltd 2019
# Licence:     <your licence>
# Sample JSON: {"town":"English", "id":1}
#-------------------------------------------------------------------------------
from root import db
# from models.options import Options

class Towns(db.Model):
    __tablename__ =  "towns"
    id = db.Column(db.Integer, primary_key=True)
    district = db.Column(db.Integer)
    town = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return '{"id":{0}, "town":{1}}'.format(self.id, self.town)

    @classmethod
    def get_all_towns(classname):
        towns = Towns.query.all()
        towns_json = [town.serialize() for town in towns]
        return towns_json

    @classmethod
    def get_town_from(classname, id):
        town = classname.query.get(id)
        return town

    @classmethod
    def delete_town_from(classname, id):
        town = classname.get_town_from(id)
        if town is None:
            return None
        db.session.delete(town)
        db.session.commit()
        return town

    @classmethod
    def submit_town_from_json(classname, json_town):
        town = classname(town=json_town['town'], district=json_town.get("district", 0))
        db.session.add(town)
        db.session.commit()
        return town

    #todo:json encoding needed
    def serialize(self):
        json_town = {
        'id' : self.id ,
        'town' : self.town,
        }
        return json_town

    @staticmethod
    def validate_town(town):
        if ('town' in town):
            return True
        else:
            return False