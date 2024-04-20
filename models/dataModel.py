

from flask_sqlalchemy import SQLAlchemy
from flask import Flask,request,jsonify,send_file

from api import db
#db=SQLAlchemy()


class Datas(db.Model):
    __tablename__='datas'

    id=db.Column(db.Integer,primary_key=True)
    age =db.Column(db.Integer)
    gender =db.Column(db.Integer)
    height=db.Column(db.Integer)
    weight =db.Column(db.Float)
    ap_hi =db.Column(db.Integer)
    ap_lo =db.Column(db.Integer)
    cholesterol =db.Column(db.Integer)
    gluc =db.Column(db.Integer)
    smoke =db.Column(db.Integer)
    alco =db.Column(db.Integer)
    active =db.Column(db.Integer)
    cardio=db.Column(db.Integer)
    proba=db.Column(db.Float)



    def __init__(self,age,gender,height,weight,ap_hi,ap_lo,cholesterol,gluc,smoke,alco,active,cardio,proba):
        self.age=age
        self.gender=gender
        self.height=height
        self.weight=weight
        self.ap_hi=ap_hi
        self.ap_lo=ap_lo
        self.cholesterol=cholesterol
        self.gluc=gluc
        self.smoke=smoke
        self.alco=alco
        self.active=active
        self.cardio=cardio
        self.proba=proba
        
