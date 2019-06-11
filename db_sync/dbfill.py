import sqlalchemy as sa
import pandas as pd
import config
import gc
con = sa.create_engine(config.CONNECTION_STRING)

#Fill the States
def fillStates():
	states_df = pd.read_json('json//states.json')
	states_df.index = range(1, len(states_df) + 1)
	states_df.index.rename("id", inplace=True)
	states_df.to_sql(name='states',
					if_exists='append',
					con=con,
					dtype={'id': sa.types.BIGINT(), 
                        	'state': sa.types.NVARCHAR(length=30)})
	del states_df
	gc.collect()
fillStates()

#Fill the Districts
def fillDistricts():
	districts_df = pd.read_json('json//districts.json')
	districts_df.to_sql(name='districts',
						if_exists='append',
						index=False,
						con=con,
						dtype={'id': sa.types.BIGINT(),
								'district': sa.types.NVARCHAR(length=30),
								'state_id': sa.types.BIGINT()})
	del districts_df
	gc.collect()
fillDistricts()

#Fill the Towns
def fillTowns():
	towns_df = pd.read_json('json//towns.json')
	towns_df.index = range(1, len(towns_df) + 1)
	towns_df.index.rename("id", inplace=True)	
	towns_df.to_sql(name='towns',
					if_exists='append',
					con=con,
					dtype={'id': sa.types.BIGINT(),
							'town': sa.types.NVARCHAR(length=30),
							'district_id': sa.types.BIGINT()})
	del towns_df
	gc.collect()
fillTowns()

#Fill the Institutions
def fillInstitutions():
	institutions_df = pd.read_json('json//institutions.json')
	institutions_df.index = range(1, len(institutions_df) + 1)
	institutions_df.index.rename("id", inplace=True)	
	institutions_df.to_sql(name='institutions',
							if_exists='append',
							con=con,
							dtype={'id': sa.types.BIGINT(),
									'institution': sa.types.NVARCHAR(length=150),
									'district_id': sa.types.BIGINT()})
	del institutions_df
	gc.collect()
fillInstitutions()

#Fill the Qualifications
def fillQualifications():
	qualifications_df = pd.read_json('json//qualifications.json')
	qualifications_df.index = range(1, len(qualifications_df) + 1)
	qualifications_df.index.rename("id", inplace=True)
	qualifications_df.to_sql(name='qualifications',
							if_exists='append',
							con=con,
							dtype={'id': sa.types.BIGINT(),
									'qualification': sa.types.NVARCHAR(length=20)})
	del qualifications_df
	gc.collect()
fillQualifications()

#Fill the Subjects
def fillSubjects():
	subjects_df = pd.read_json('json//subjects.json')
	subjects_df.index = range(1, len(subjects_df) + 1)
	subjects_df.index.rename("id", inplace=True)
	subjects_df.to_sql(name='subjects',
						if_exists='append',
						con=con,
						dtype={'id': sa.types.BIGINT(),
								'subject': sa.types.NVARCHAR(length=20)})
	del subjects_df
	gc.collect()
fillSubjects()