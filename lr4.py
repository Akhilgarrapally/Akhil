from flask import Flask,request,json,jsonify
from flask_mysqldb import MySQL
import pandas as p
import numpy as n
import pickle
import matplotlib.pyplot as pl
import seaborn as s
s.set()
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import sklearn.metrics as sm

app = Flask(__name__)
app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']="Akhilyuvi143@"
app.config['MYSQL_DB']="flask"


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
          Pregnancies = d['Pregnancies']
          #Glucose = d['Glucose']
          BloodPressure = d['BloodPressure']
          SkinThickness = d['SkinThickness']
          Insulin = d['Insulin']
          BMI = d['BMI']
          DiabetesPedigreeFunction = d['DiabetesPedigreeFunction']
          Age = d['Age']
          #Outcome = d['Outcome']
          a = [[Pregnancies,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]]
         
          X = d.iloc[:, 0:8]
          y = d.iloc[:, 1]
         
          X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0,test_size=0.3)
          model=LinearRegression()
          model.fit(X_train,y_train)
          nsamples, nx, ny = X_train.shape
          X_train = X_train.reshape((nsamples,nx*ny))
          y_pred = model.predict(a)
          pickle.dump(model,open('model.pkl','wb'))
          list0=y_pred.tolist()
          print(y_pred)
          return jsonify({'predicted_ouput': list0})
     
         
if __name__ == '__main__':
    app.run()