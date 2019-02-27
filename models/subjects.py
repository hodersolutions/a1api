#-------------------------------------------------------------------------------
# Name:        Subjects
# Purpose:
#
# Author:      Siva Samudrala
#
# Created:     13/02/2019
# Copyright:   (c) Hoder Solutions Pvt Ltd 2019
# Licence:     <your licence>
# Sample JSON: {"subject":"English", "id":1}
#-------------------------------------------------------------------------------
from root import db

class Subjects(db.Model):
    __tablename__ =  "subjects"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    subject = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return '{"id":{0}, "subject":{1}}'.format(self.id, self.subject)

    @classmethod
    def get_all_subjects(classname):
        subjects = Subjects.query.all()
        subjects_json = [subject.serialize() for subject in subjects]
        return subjects_json

    @classmethod
    def get_subject_from(classname, id):
        subject = classname.query.get(id)
        return subject

    @classmethod
    def delete_subject_from(classname, id):
        subject = classname.get_subject_from(id)
        if subject is None:
            return None
        db.session.delete(subject)
        db.session.commit()
        return subject

    @classmethod
    def submit_subject_from_json(classname, json_subject):
        subject = classname(subject=json_subject['subject'])
        db.session.add(subject)
        db.session.commit()
        return subject

    #todo:json encoding needed
    def serialize(self):
        json_subject = {
        'id' : self.id ,
        'name' : self.subject,
        }
        return json_subject

    @staticmethod
    def validate_subject(subject):
        if ('subject' in subject):
            return True
        else:
            return False