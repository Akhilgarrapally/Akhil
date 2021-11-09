from flask import Flask,render_template,request
from flask import jsonify
from flask_mysqldb import MySQL

app=Flask(__name__)


import pandas as pd
import numpy as np

import pickle
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score
df = pd.read_excel(r'C:\Users\indin\OneDrive\Desktop\data of diabiates.xlsx')
df
replace_zero = ['Glucose', 'BloodPressure', 'SkinThickness', 'BMI', 'Insulin']
for column in replace_zero:
 df[column] = df[column].replace(0, np.NaN) 
 mean = int(df[column].mean(skipna=True)) 
 df[column] = df[column].replace(np.NaN, mean) 


@app.route('/',methods=['GET','POST'])
def index():
     if request.method=="POST":
         Pregnancies = request.json['Pregnancies']
         Glucose = request.json['Glucose']
         BloodPressure = request.json['BloodPressure']
         SkinThickness = request.json['SkinThickness']
         Insulin = request.json['Insulin']
         BMI = request.json['BMI']
         DiabetesPedigreeFunction = request.json['DiabetesPedigreeFunction']
         Age = request.json['Age']
         d=[[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]]
        
         a = df.iloc[:, 0:8]
         b = df.iloc[:, 8]
       
        
         a_train, a_test, b_train, b_test = train_test_split(a, b, random_state=0,test_size=0.2)
         model=LogisticRegression(solver='lbfgs')
         model.fit(a_train,b_train)
         b_pred=model.predict(d)
         pickle.dump(model,open('model.pkl','wb'))
         list1 = b_pred.tolist()
         
     
         return jsonify({'predicted_output': list1})
     if __name__=='__main__':
      app.run()
