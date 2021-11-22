from flask import Flask,request,jsonify
from flask_cors import CORS
from flask_mysqldb import MySQL
app = Flask("__name__")

app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']="Akhil"
app.config['MYSQL_DB']="pharma"

mysql = MySQL(app)
CORS(app)

@app.route("/PATIENT_NAME",methods = ['GET','POST'])
def PATIENT_NAME():
    if request.method=='GET':
        d = request.json
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM PATIENT_PERSONAL")
        fetchdata = cur.fetchall()
        cur.close()
        return jsonify(fetchdata) 
    return 'unsuccess'

@app.route("/working_days",methods = ['GET','POST'])
def working_days():
    if request.method == 'GET':
        d = request.json
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM working_days")
        fetchdata = cur.fetchall()
        cur.close()
        # return jsonify(fetchdata) 
        return 'success'
    elif request.method == 'GET':
         d = request.json
         cur = mysql.connection.cursor()
         cur.execute("SELECT * FROM working_days")
         fetchdata = cur.fetchall()
         cur.close()
         return jsonify(fetchdata) 
     
   

@app.route("/SCHEDULE",methods = ['GET','POST'])
def SCHEDULE():
     if request.method=='POST':
        d=request.json
        Everyday = d['Everyday']
        monday = d['monday']
        tuesday = d['tuesday']
        wednsday = d['wednsday']
        thursday = d['thursday']
        friday = d['friday']
        
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO SCHEDULE(Everyday,monday ,tuesday,wednsday,thursday,friday) VALUES( %s,%s,%s,%s,%s,%s)",(Everyday,monday ,tuesday,wednsday,thursday,friday))
        mysql.connection.commit()
        cursor.close()
        return 'success'
     elif request.method == 'GET':
         d = request.json
         cur = mysql.connection.cursor()
         cur.execute("SELECT * FROM SCHEDULE")
         fetchdata = cur.fetchall()
         cur.close()
         return jsonify(fetchdata) 
     return 'unsuccess'
    
    
    
    
if __name__ == '__main__':
    app.run()