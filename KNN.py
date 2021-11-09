import pandas as pd
import numpy as np

from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors
from flask import Flask,render_template,request
from flask import jsonify
from flask_mysqldb import MySQL

app=Flask(__name__)




@app.route('/',methods=['GET','POST'])
def USER_SIGNUP():
     if request.method=="POST":
         
         DOCTORS_NAME = request.json['DOCTORS_NAME']
         
         data = pd.read_excel(r'C:\Users\indin\OneDrive\Desktop\data of diabiates.xlsx')
         formatted = data.pivot_table(columns='Symptoms',index='DOCTORS_NAME',values='Ratings_by_count')
         formatted.fillna(0, inplace=True)
         formatted_sparse = csr_matrix(formatted)
         
         model = NearestNeighbors(algorithm='brute',leaf_size=30,n_neighbors=5,n_jobs=1,metric_params=None,p=2,radius=1.0)
         model.fit(formatted_sparse)

         Symptoms =np.where(formatted.index==DOCTORS_NAME)[0][0]     
         distances,suggestions= model.kneighbors(formatted.iloc[Symptoms,:].values.reshape(1,-1),n_neighbors=4)

         for i in range(len(suggestions)):
             # print(formatted.index[suggestions[i]])
              list1 = formatted.index[suggestions[i]]
              #print(list1)
         
         return jsonify({'Recommended Doctors for the given doctor':list1[0],
                             'DOCtORNAME':list1[1],'DOCTORNAME':list1[2],'DOCNAME':list1[3]})
         
     else : return jsonify('akhil')
if "__name__" == '__main__':
    app.run()
