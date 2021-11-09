from flask import Flask,request
from flask import jsonify
import pandas as p
import numpy as n
import matplotlib.pyplot as pl
"%matplotlib inline"
import seaborn as s
import warnings
warnings.filterwarnings("ignore")
import plotly as P
from statsmodels.stats.outliers_influence import variance_inflation_factor
app = Flask("__name__")

@app.route("/",methods = ['GET','POST'])
def index():
     if request.method=='POST':
      d = p.read_excel(r'C:\Users\indin\OneDrive\Desktop\data of diabiates.xlsx')
      X = n.array(d)
      vif = p.DataFrame()
      vif=[variance_inflation_factor(X,i) for i in range(X.shape[1])]
      print(vif)
      X = p.DataFrame(X)
      X=d.iloc[:,:8]
      y=d.iloc[:,1]
      print(X.head())
      print(y)
      from sklearn.model_selection import train_test_split
      X_train,X_test,y_train,y_test = train_test_split(X,y, test_size = 0.3,random_state=15)
      from sklearn import linear_model
      reg = linear_model.LinearRegression()
      reg.fit(X_train,y_train)
      print('coefficients: ',reg.coef_)
      print('intercept: ',reg.intercept_)
      y_pred= reg.predict(X_test)
      y_pred
      from sklearn.metrics import r2_score
      #from sklearn.metrics import accuracy_score
      print(r2_score(y_test,y_pred))
      import sklearn.metrics as sm
      print("Mean absolute error =", round(sm.mean_absolute_error(y_test, y_pred))) 
      print("Mean squared error =", round(sm.mean_squared_error(y_test, y_pred))) 
      print("Explain variance score =", round(sm.explained_variance_score(y_test, y_pred))) 
      print("R2 score =", round(sm.r2_score(y_test, y_pred))) 
         #return 'scuccess'
      
      y_pred = reg.predict(X_train)
      y_pred
      print(r2_score(y_train,y_pred))
      return jsonify(r2_score(y_test, y_pred),y_pred,y_test,sm.mean_absolute_error(y_test, y_pred),sm.mean_squared_error(y_test, y_pred),sm.explained_variance_score(y_test, y_pred))
     else:
         return y_pred
    
 
if __name__ == '__main__':
    app.run()

