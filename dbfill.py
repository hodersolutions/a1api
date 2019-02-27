import sqlalchemy as sa
import pandas as pd
con = sa.create_engine('sqlite:///questionbank.db')

#Fill the districts
def fillDistricts:
	chunks = pd.read_csv('districts.csv', chunksize=100000)
	for chunk in chunks:
		chunk.to_sql(name='districts', if_exist='append', con=con)

#Fill the towns
def fillTowns:
	chunks = pd.read_csv('towns.csv', chunksize=100000)
	for chunk in chunks:
		chunk.to_sql(name='towns', if_exist='append', con=con)

#Fill the districts
def fillInstitutions:
	chunks = pd.read_csv('institutions.csv', chunksize=100000)
	for chunk in chunks:
		chunk.to_sql(name='institutions', if_exist='append', con=con)
