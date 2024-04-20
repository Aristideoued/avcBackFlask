
import flask as fk
from flask import Flask
from flask_httpauth import HTTPBasicAuth
from werkzeug.http import parse_authorization_header
import json

import hashlib
from flask_sqlalchemy import SQLAlchemy
from functools import update_wrapper
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:2885351@localhost/avcdata'

db=SQLAlchemy(app)

from models.adminModel import Admin


auth = HTTPBasicAuth()
#db=SQLAlchemy()



@auth.verify_password
def authenticate(username, password):
    hashed_password = hashlib.sha256((password).encode("ascii")).hexdigest()
    admin=db.session.query(Admin).filter(Admin.password==hashed_password).filter(Admin.username==username).first()
    if admin:
      return True
    else:
      return False
    return False
#def testFunction():
    #return "test ok"
