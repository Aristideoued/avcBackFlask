

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
from models.clientModel import Client
from models.adminModel import Admin
from api import app,db
from flask import make_response
from api import app,db,auth,authenticate


@app.route('/userRegister' ,methods=['GET','POST'])
@auth.login_required
@cross_origin(origin='*')
def addClient():
    if request.method=='POST':

            data = request.get_json()

            nom=data['nom']
            prenom=data['prenom']
            email=data['email']
            password=data['password']
            hashed_password = hashlib.sha256((password).encode("ascii")).hexdigest()

            
            client=Client(nom,prenom,email,hashed_password)
            db.session.add(client)
            db.session.commit()
            retour={"code":200,"title":"Ajout d'un utilisateur","contenu":"Utilisateur ajouté avec succes"}
            return make_response(jsonify(retour),200)

    else:
      retour={"code":403,"title":"Methode non authorisée","contenu":"Cet endpoint accepte que la methode post"}
      return make_response(jsonify(retour),403)



@app.route('/loginUser' ,methods=['GET','POST','OPTIONS'])
@auth.login_required
@cross_origin(origin='*')
def loginUser():
    if request.method=='POST':
            #print(request.get_json())
            data = request.get_json()

            email=data['email']
            password=data['password']
            hashed_password = hashlib.sha256((password).encode("ascii")).hexdigest()
            admin=db.session.query(Client).filter(Client.password==hashed_password).filter(Client.email==email).first()
            if admin :
                retour={"code":200,"title":"Connexion","contenu":"Connexion reussie","nom":admin.nom,"prenom":admin.prenom,"id":admin.id}
                return make_response(jsonify(retour),200)
            else :
                retour={"code":401,"title":"Connexion","contenu":"Echec de connexion, identifiants incorrects"}
                return make_response(jsonify(retour),401)

    else:
      retour={"code":403,"title":"Methode non authorisée","contenu":"Cet endpoint accepte que la methode post"}
      return make_response(jsonify(retour),403)



@app.route('/userById' ,methods=['GET','POST'])
@auth.login_required
@cross_origin(origin='*')
def getClientById():
    if request.method=='POST':
            clients=[]
            data = request.get_json()

            id=int(data['id'])

            client=db.session.query(Client).filter(Client.id==id)

            for f in client:
                #print(u.nom)
                clients.append({"id":f.id,"nom":f.nom,"prenom":f.prenom,"contact":f.contact,"email":f.email})


            retour={"code":200,"title":"Client "+str(id),"contenu":clients}
            #print(users[0])
            return make_response(jsonify(retour),200)

    else:
      retour={"code":403,"title":"Methode non authorisée","contenu":"Cet endpoint accepte que la methode POST"}
      return make_response(jsonify(retour),403)



@app.route('/users' ,methods=['GET','POST'])
@auth.login_required
@cross_origin(origin='*')
def getClient():
    if request.method=='GET':
            clients=[]
            client = Client.query.all()
            #user=db.session.query(User).all()

            for f in client:
                #print(u.nom)
                clients.append({"id":f.id,"nom":f.nom,"prenom":f.prenom,"contact":f.contact,"email":f.email})


            retour={"code":200,"title":"Liste des clients","contenu":clients}
            #print(users[0])
            return make_response(jsonify(retour),200)

    else:
      retour={"code":403,"title":"Methode non authorisée","contenu":"Cet endpoint accepte que la methode GET"}
      return make_response(jsonify(retour),403)


@app.route('/delete/user' ,methods=['GET','POST'])
@auth.login_required
@cross_origin(origin='*')
def delete_user():
    if request.method=='POST':
            test=False
            data = request.get_json()

            id=int(data['id'])

            user1=db.session.query(Client).filter(Client.id==id).first()
            if user1:
                Client.query.filter_by(id=id).delete()
                db.session.commit()

                retour={"code":200,"title":"Suppression de compte client","contenu":"Compte supprimé avec succès"}
                return make_response(jsonify(retour),200)
            else :

                retour={"code":401,"title":"Echec de suppression","contenu":"Compte non trouvé"}
                return make_response(jsonify(retour),401)




    else:
      retour={"code":403,"title":"Methode non authorisée","contenu":"Cet endpoint accepte que la methode post"}
      return make_response(jsonify(retour),403)



@app.route('/update/user' ,methods=['GET','POST'])
@auth.login_required
@cross_origin(origin='*')
def update_user():
    if request.method=='POST':
            test=False
            data = request.get_json()

            id=int(data['id'])
            nom=data['nom']
            prenom=data['prenom']
            email=data['email']
            contact=data['contact']



            user1=db.session.query(Client).filter(Client.id==id).first()
            if user1:
                user1.nom=nom
                user1.prenom=prenom
                user1.email=email
                user1.contact=contact
                db.session.add(user1)
                db.session.commit()

                retour={"code":200,"title":"Modification de compte","contenu":"Compte modifié avec succès"}
                return make_response(jsonify(retour),200)
            else :

                retour={"code":401,"title":"Echec de modification","contenu":"Compte non trouvé"}
                return make_response(jsonify(retour),401)




    else:
      retour={"code":403,"title":"Methode non authorisée","contenu":"Cet endpoint accepte que la methode post"}
      return make_response(jsonify(retour),403)

