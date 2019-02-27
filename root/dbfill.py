import sqlalchemy as sa
import pandas as pd
con = sa.create_engine('sqlite:///questionbank.db')

#Fill the districts
def fillStates():
	chunks = pd.read_json('states.json')
	chunks.index = range(1,len(chunks)+1)
	chunks.index.rename("id", inplace=True)
	chunks.to_sql(name='states', if_exists='append', con=con)
fillStates()

#Fill the districts
def fillDistricts():
	chunks = pd.read_json('districts.json')
	chunks.to_sql(name='districts', if_exists='append', index=False, con=con)

fillDistricts()
#Fill the towns
def fillTowns():
	df = pd.read_json('towns.json')
	df.index = range(1,len(df)+1)
	df.index.rename("id", inplace=True)
	df.to_sql(name='towns', if_exists='append', con=con)
fillTowns()
#Fill the districts
def fillInstitutions():
	df = pd.read_json('institutions.json')
	df.index = range(1,len(df)+1)
	df.index.rename("id", inplace=True)
	df.to_sql(name='institutions', if_exists='append', con=con)
fillInstitutions()
#Fill the qualifications
def fillQualifications():
	df = pd.read_json('qualifications.json')
	df.index = range(1,len(df)+1)
	df.index.rename("id", inplace=True)
	df.to_sql(name='qualifications', if_exists='append', con=con)
fillQualifications()
	#Fill the districts
def fillSubjects():
	df = pd.read_json('subjects.json')
	df.index = range(1,len(df)+1)
	df.index.rename("id", inplace=True)
	df.to_sql(name='subjects', if_exists='append', con=con)
fillSubjects()