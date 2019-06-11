#-------------------------------------------------------------------------------
# Name:        __init__.py
# Purpose:
#
# Author:      kkrishnav
#
# Created:     15/10/2018
# Copyright:   (c) kkrishnav 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
import config

application = Flask(__name__)
application.config["SECRET_KEY"] = "hoderapi"
application.config['SQLALCHEMY_DATABASE_URI'] = config.CONNECTION_PARAMS
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
application.config['CORS_HEADERS'] = 'Content-Type'

CORS(application)
db = SQLAlchemy(application)
bcrypt = Bcrypt(application)

from controllers import *

print("Creating database and tables")
db.create_all()