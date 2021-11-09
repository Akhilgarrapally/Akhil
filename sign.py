# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 09:51:27 2021

@author: indin
"""

from flask import Flask,request
from flask_mysqldb import MySQL
app = Flask("__name__")

app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']="Akhilyuvi143@"
app.config['MYSQL_DB']="flask_signup"

mysql = MySQL(app)

@app.route("/",methods = ['GET','POST'])
def index():
     if request.method=='POST':
        d=request.json
        name=d['name']
        email = d['email']
        password=d['password']
        rpw= d['rpw']
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO sign(name,email,password,rpw) VALUES( %s,%s,%s,%s)",(name,email,password,rpw))
        mysql.connection.commit()
        cursor.close()
        return 'sucess'
     else:
        return 'unsuccess'
        

   

if __name__ == '__main__':
    app.run()
