

from flask_sqlalchemy import SQLAlchemy
from flask import Flask,request,jsonify,send_file

from api import db
#db=SQLAlchemy()


class Client(db.Model):
    __tablename__='clients'
    id=db.Column(db.Integer,primary_key=True)
    nom=db.Column(db.String(60))
    prenom=db.Column(db.String(60))
    email=db.Column(db.String(255))
    password=db.Column(db.String(255))
    



    def __init__(self,nom,prenom,email,password):
        self.nom=nom
        self.prenom=prenom
        self.email=email
        self.password=password
        
