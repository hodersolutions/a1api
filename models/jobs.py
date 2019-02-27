#-------------------------------------------------------------------------------
# Name:     Users
# Purpose:
#
# Author:     Siva Samudrala
#
# Created:   13/02/2019
# Copyright:   (c) Hoder Solutions Pvt Ltd 2018
# Licence:   <your licence>
# Sample JSON:  {"username":"RF","email":"fedex@gmail.com","password":"fedex", "isrecruiter" : 1}
#-------------------------------------------------------------------------------
from root import application, db, bcrypt
from jwt import encode
from datetime import datetime, timedelta
from models import *
from json import dumps, loads

class Jobs(db.Model):
	__tablename__ =  "jobs"
	id = db.Column(db.Integer, primary_key=True)
	subject = db.Column(db.Integer, db.ForeignKey('subjects.id'))
	jobdetails = db.Column(db.String(2000), default="")
	minexperience = db.Column(db.Integer, default=0)
	maxexperience = db.Column(db.Integer, default=0)
	telephone = db.Column(db.Integer, default=0)
	institution = db.Column(db.String(80), default="")
	description = db.Column(db.String(80), default="")
	recruiter = db.Column(db.Integer, db.ForeignKey('users.id'))
	qualification = db.Column(db.Integer, db.ForeignKey('qualifications.id'))
	state = db.Column(db.Integer, db.ForeignKey('states.id'))
	district = db.Column(db.Integer, db.ForeignKey('districts.id'))
	registered_on = db.Column(db.DateTime, nullable=False, default=datetime.now())
	closed_on = db.Column(db.DateTime)
	isactive = db.Column(db.Boolean, nullable=False, default=True)

			
	@classmethod
	def add_job(classname, _user):
		pass

	@classmethod
	def submit_job_from_json(classname, json_job):
		job = classname()
		if not json_job.get("subject", None) is None:
			job.subject = json_job.get("subject", None)
		if not json_job.get("jobdetails", None) is None:
			job.jobdetails = json_job.get("jobdetails", None)
		if not json_job.get("minexperience", None) is None:
			job.minexperience = json_job.get("minexperience", None)
		if not json_job.get("maxexperience", None) is None:
			job.maxexperience = json_job.get("maxexperience", None)
		if not json_job.get("telephone", None) is None:
			job.telephone = json_job.get("telephone", None)
		if not json_job.get("institution", None) is None:
			job.institution = json_job.get("institution", None)
		if not json_job.get("submitter", None) is None:
			user = users.Users.get_user_by_username(json_job.get("submitter", None))
			if not user is None:
				print(user)
				job.recruiter = 1
		if not json_job.get("district", None) is None:
			job.district = json_job.get("district", None)
		if not json_job.get("state", None) is None:
			job.state = json_job.get("state", None)
		if not json_job.get("qualification", None) is None:
			job.qualification = json_job.get("qualification", None)
		if not json_job.get("description", None) is None:
			job.description = json_job.get("description", None)
		db.session.add(job)
		db.session.commit()
		return job

	@classmethod
	def get_jobs_by_filter(classname, filter):
		query = "select * from jobs where "
		for key, value in filter.items():
			query = "{} {} = {}".format(query, key, value)
		print(query)
		result = db.engine.execute(query)
		list_result =[]
		for job in result:
			job_object = dict(zip(result.keys(), job))
			list_result.append(Jobs.serialize_dict(job_object))

		return list_result

	def serialize(self):
		json_job = {
			"Id": self.id,
			"Title": self.description,
			#"Recruiter": users.Users.get_user_by(self.recruiter).email,
			"Minimum Qualification Needed": qualifications.Qualifications.get_qualification_from(self.qualification).qualification,
			"District": districts.Districts.get_district_from(self.district).district,
			"State": states.States.get_state_from(self.state).state,
			"School": self.institution,
			"Minimum years of Experience": self.minexperience,
			"Job Description": self.jobdetails,
			"Opened on":self.registered_on.strftime("%d-%B")
			}
		return json_job

	@classmethod
	def serialize_dict(classname, job_dict):
		json_job = {
			"Id": job_dict['id'],
			"Title": job_dict['description'],
			#"Recruiter": users.Users.get_user_by(self.recruiter).email,
			"Minimum Qualification Needed": qualifications.Qualifications.get_qualification_from(job_dict['qualification']).qualification,
			"District": districts.Districts.get_district_from(job_dict['district']).district,
			"State": states.States.get_state_from(job_dict['state']).state,
			"School": job_dict['institution'],
			"Minimum years of Experience": job_dict['minexperience'],
			"Job Description": job_dict['jobdetails'],
			"Opened on":job_dict['registered_on']
			}
		return json_job
