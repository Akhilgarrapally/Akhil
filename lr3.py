from flask import Flask,request
from flask import jsonify
from flask_mysqldb import MySQL

app=Flask(__name__)

app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']="Akhilyuvi143@"
app.config['MYSQL_DB']="flask"

import pandas as p
import numpy as n
from json import JSONEncoder
import json


import pickle
import matplotlib.pyplot as pl
import seaborn as s
s.set()
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.metrics import accuracy_score
import sklearn.metrics as sm

d = p.read_excel(r'C:\Users\indin\OneDrive\Desktop\data of diabiates.xlsx')
replace_zero = ['Glucose', 'BloodPressure', 'SkinThickness', 'BMI', 'Insulin']
for column in replace_zero:
    d[column] = d[column].replace(0, n.NaN) 
    mean = int(d[column].mean(skipna=True)) 
    d[column] = d[column].replace(n.NaN, mean) 
   

mysql = MySQL(app)

@app.route('/',methods=['GET','POST'])
def index():
     if request.method=="POST":
         d = p.read_excel(r'C:\Users\indin\OneDrive\Desktop\data of diabiates.xlsx')
         X = d.iloc[:, 0:8] 
         y = d.iloc[:, 1]
         X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0,test_size=0.3)
         d = d.to_dict()
         d = json.dumps(d)
         #d = d.to_json()
         d = request.get_json()
         sc_X = StandardScaler()
         X_train = sc_X.fit_transform(X_train)
         X_test = sc_X.transform(X_test)
         model=LinearRegression() 
         model.fit(X_train,y_train)
         y_pred=model.predict(X_test)
         pickle.dump(model,open('model.pkl','wb'))
         print(r2_score(y_test, y_pred))
         print(y_pred)
         print(y_test)                  
         print("Mean absolute error =", (sm.mean_absolute_error(y_test, y_pred))) 
         print("Mean squared error =", (sm.mean_squared_error(y_test, y_pred))) 
         print("Explain variance score =", (sm.explained_variance_score(y_test, y_pred))) 
         print("R2 score =", (sm.r2_score(y_test, y_pred))) 
         #return 'success'
         return jsonify(y_test,y_pred,r2_score(y_test,y_pred),sm.mean_absolute_error(y_test,y_pred), sm.mean_squared_error(y_test, y_pred), sm.explained_variance_score(y_test, y_pred))
        
     else:
          d = p.read_excel(r'C:\Users\indin\OneDrive\Desktop\data of diabiates.xlsx')
          X = d.iloc[:, 0:8]
          y = d.iloc[:, 1]
          d = request.json()
          Pregnancies = d['Pregnancies']
          #Glucose = d['Glucose']
          BloodPressure = d['BloodPressure']
          SkinThickness = d['SkinThickness']
          Insulin = d['Insulin']
          BMI = d['BMI']
          DiabetesPedigreeFunction = d['DiabetesPedigreeFunction']
          Age = d['Age']
          #Outcome = d['Outcome']
          d= p.DataFrame([Pregnancies,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
          print(d) 
          cur = mysql.connection.cursor()
          cur.execute("INSERT INTO dia(Pregnancies,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age) VALUES (%s,%s,%s,%s,%s,%s,%s)", (Pregnancies,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age))
          mysql.connection.commit()
          cur.close()
         
          X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0,test_size=0.3)
          
          model=LinearRegression()
          model.fit(X_train,y_train)
          c=model.predict(d)
          pickle.dump(model,open('model.pkl','wb'))
          print(c)
          print(model.predict(d))
          #import requests
          #print(json())
          #return 'success'
          return jsonify((r2_score(y_test, y_pred),y_pred,sm.mean_absolute_error(y_test,y_pred),sm.mean_squared_error(y_test,y_pred),sm.explained_variance_score(y_test,y_pred)))  
 
          
if __name__=='__main__':
   app.run()