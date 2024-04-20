

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
from models.dataModel import Datas
from models.adminModel import Admin
from api import app,db
from flask import make_response
from api import app,db,auth,authenticate
import pandas as pd
from joblib import dump, load


@app.route('/model' ,methods=['GET','POST'])
@auth.login_required
@cross_origin(origin='*')
def testModel():
    if request.method=='POST':

            data = request.get_json()
            age =int(data['age'])
            gender =int(data['gender'])
            height =int(data['height'])
            weight =float(data['weight'])
            ap_hi =int(data['ap_hi'])
            ap_lo =int(data['ap_lo'])
            cholesterol =int(data['cholesterol'])
            gluc =int(data['gluc'])
            smoke =int(data['smoke'])
            alco =int(data['alco'])
            active =int(data['active'])
            #cardio =int(data['cardio'])
            #proba =float(data['proba'])
            

           
            #data=Datas(age,gender,height,weight,ap_hi,ap_lo,cholesterol,gluc,smoke,alco,active,cardio,proba)
            #db.session.add(data)
            #db.session.commit()
            test={
            
            "gender":gender,
            "height":height,
            "weight":weight,
            "ap_hi":ap_hi,
            "ap_lo":ap_lo,
            "cholesterol":cholesterol,
            "gluc":gluc,
            "smoke":smoke,
            "alco":alco,
            "active":active,
            "ageEnAnnee":age
           
            }
            X_test = pd.DataFrame(test, index=[0])
            loaded_model = load('/home/rsu/Bureau/Projets/GestionClientFlask/api/endpoints/random_forest_avc_model.joblib')
            y_pred=loaded_model.predict(X_test)
            probabilities = loaded_model.predict_proba(X_test)
            probabilities_class_1=None

            if(int(y_pred[0]==1)):               
                probabilities_class_1 = probabilities[:, 1]

            else:
                probabilities_class_1 = probabilities[:, 0]





            retour={"code":200,"title":"Prediction du model","prediction":int(y_pred[0]),"probabilite":probabilities_class_1[0]}
            return make_response(jsonify(retour),200)

    else:
      retour={"code":403,"title":"Methode non authorisée","contenu":"Cet endpoint accepte que la methode post"}
      return make_response(jsonify(retour),403)



