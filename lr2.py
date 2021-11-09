from flask import Flask,request
from flask import jsonify

import pickle
import pandas as p
import numpy as n
import json

app = Flask("__name__")

@app.route("/",methods=['GET','POST'])
def predict():
    model = pickle.load(open('model.pkl','rb'))
    d = request.get_json(force=True)
    prediction = model.predict([[n.array(d['exp'])]])
    output = prediction[0]
    return jsonify(output)     
           
       
if __name__ == '__main__':
    app.run()


