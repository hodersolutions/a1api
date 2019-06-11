import urllib
import sys
import platform;

CONNECTION_PARAMS = (
    "DRIVER={SQL Server Native Client 11.0};"
    "SERVER=(local)\\SQLEXPRESS;"
    "DATABASE=schoolbank;"
    "UID=kkrishnav;"
    "PWD='2018@Factset';"
    "Trusted_Connection=yes;"
)

if str(sys.argv[1]) == 'home':
    CONNECTION_PARAMS = (
        "DRIVER={SQL Server Native Client 11.0};"
        "SERVER=varanasikalyan;"
        "DATABASE=schoolbank;"
        "UID=varanasikalyan\\Kalyan;"
        "Trusted_Connection=yes;"
    )

CONNECTION_STRING = ''

if platform.sys.version_info.major < 3:
    CONNECTION_STRING = 'mssql+pyodbc:///?odbc_connect={0}'.format(urllib.quote_plus(CONNECTION_PARAMS))
else:
    if str(sys.argv[2]) == 'postgresql':
        CONNECTION_STRING = 'postgresql+psycopg2://postgres:qwerty@localhost/schoolbank'
    elif str(sys.argv[2]) == 'sqllite':
        CONNECTION_STRING = 'sqlite:///..//root//schoolbank.db'
    else:
        CONNECTION_STRING = 'mssql+pyodbc:///?odbc_connect={0}'.format(urllib.parse.quote_plus(CONNECTION_PARAMS))

CHUNK_SIZE = 10000