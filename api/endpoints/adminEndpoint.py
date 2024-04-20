

from flask import Flask,request,jsonify,send_file
from flask_httpauth import HTTPBasicAuth
from flask_sqlalchemy import SQLAlchemy
#from response import testpay_response
from PIL import Image
import glob
from flask_cors import cross_origin
import hashlib, uuid
import os
from datetime import datetime
from models.adminModel import Admin
from api import app,db
from flask import make_response
from api import app,db,auth,authenticate


@app.route('/adminRegister' ,methods=['GET','POST'])
@cross_origin(origin='*')
def addAdmin():
    if request.method=='POST':

            data = request.get_json()

            nom=data['nom']
            prenom=data['prenom']
            username=data['username']
            password=data['password']
            hashed_password = hashlib.sha256((password).encode("ascii")).hexdigest()

            
            client=Admin(nom,prenom,username,hashed_password)
            db.session.add(client)
            db.session.commit()
            retour={"code":200,"title":"Ajout d'un admin","contenu":"Admin ajouté avec succes"}
            return make_response(jsonify(retour),200)

    else:
      retour={"code":403,"title":"Methode non authorisée","contenu":"Cet endpoint accepte que la methode post"}
      return make_response(jsonify(retour),403)



@app.route('/loginAdmin' ,methods=['GET','POST','OPTIONS'])
@auth.login_required
@cross_origin(origin='*')
def loginAdmin():
    if request.method=='POST':
            #print(request.get_json())
            data = request.get_json()

            username=data['username']
            password=data['password']
            hashed_password = hashlib.sha256((password).encode("ascii")).hexdigest()
            admin=db.session.query(Admin).filter(Admin.password==hashed_password).filter(Admin.username==username).first()
            if admin :
                retour={"code":200,"title":"Connexion","contenu":"Connexion reussie","nom":admin.nom,"prenom":admin.prenom,"id":admin.id}
                return make_response(jsonify(retour),200)
            else :
                retour={"code":401,"title":"Connexion","contenu":"Echec de connexion, identifiants incorrects"}
                return make_response(jsonify(retour),401)

    else:
      retour={"code":403,"title":"Methode non authorisée","contenu":"Cet endpoint accepte que la methode post"}
      return make_response(jsonify(retour),403)




@app.route('/admins' ,methods=['GET','POST'])
@auth.login_required
@cross_origin(origin='*')
def getAdmin():
    if request.method=='GET':
            clients=[]
            client = Admin.query.all()
            #user=db.session.query(User).all()

            for f in client:
                #print(u.nom)
                clients.append({"id":f.id,"nom":f.nom,"prenom":f.prenom,"username":f.username})


            retour={"code":200,"title":"Liste des admins","contenu":clients}
            #print(users[0])
            return make_response(jsonify(retour),200)

    else:
      retour={"code":403,"title":"Methode non authorisée","contenu":"Cet endpoint accepte que la methode GET"}
      return make_response(jsonify(retour),403)
