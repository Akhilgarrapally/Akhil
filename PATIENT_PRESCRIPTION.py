from flask import Flask,request,jsonify
from flask_cors import CORS
from flask_mysqldb import MySQL
app = Flask("__name__")

app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']="Akhilyuvi143@"
app.config['MYSQL_DB']="clinicalfirst_pharmacy_dashboard"

mysql = MySQL(app)
CORS(app)

@app.route("/PATIENT_PRESCRIPTION",methods = ['GET','POST'])
def PATIENT_PRESCRIPTION():
     if request.method=='POST':
        d=request.json
        PRESCRIPTION_ID = d['PRESCRIPTION_ID']
        PATIENT_ID = d['PATIENT_ID']
        PATIENT_NAME = d['PATIENT_NAME']
        DOCTOR_ID = d['DOCTOR_ID']
        DOCTOR_NAME = d['DOCTOR_NAME']
        DOCTOR_LICENCE = d['DOCTOR_LICENCE']
        MEDICINE_NAME = d['MEDICINE_NAME']
        MEDICINE_QUANTITY = d['MEDICINE_QUANTITY']
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO PATIENT_PRESCRIPTION(PRESCRIPTION_ID,PATIENT_ID ,PATIENT_NAME,DOCTOR_ID,DOCTOR_NAME,DOCTOR_LICENCE,MEDICINE_NAME,MEDICINE_QUANTITY) VALUES( %s,%s,%s,%s,%s,%s,%s,%s)",(PRESCRIPTION_ID,PATIENT_ID ,PATIENT_NAME,DOCTOR_ID,DOCTOR_NAME,DOCTOR_LICENCE,MEDICINE_NAME,MEDICINE_QUANTITY))
        mysql.connection.commit()
        cursor.close()
        return 'success'
     elif request.method == 'GET':
         d = request.json
         cur = mysql.connection.cursor()
         cur.execute("SELECT * FROM PATIENT_PRESCRIPTION")
         fetchdata = cur.fetchall()
         cur.close()
         return jsonify(fetchdata) 
     return 'unsuccess'
    
    
    
    
if __name__ == '__main__':
    app.run()
