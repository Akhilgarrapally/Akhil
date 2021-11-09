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

@app.route("/OUT_FOR_DELIVERY",methods = ['GET','POST'])
def OUT_FOR_DELIVERY():
     if request.method=='POST':
        d=request.json
        PATIENT_ID = d['PATIENT_ID']
        PAYMENT_ID = d['PAYMENT_ID']
        DELIVERY_PERSON_ID = d['DELIVERY_PERSON_ID']
        DELIVERY_TIME = d['DELIVERY_TIME']
        PATIENT_NAME = d['PATIENT_NAME']
        PATIENT_ADDRESS = d['PATIENT_ADDRESS']
        TYPE_DELIVERY = d['TYPE_DELIVERY']
        PICKUP_STATUS = d['PICKUP_STATUS']
        DELIVERY_STATUS = d['DELIVERY_STATUS']
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO OUT_FOR_DELIVERY(PATIENT_ID,PAYMENT_ID ,DELIVERY_PERSON_ID,DELIVERY_TIME,PATIENT_NAME,PATIENT_ADDRESS,TYPE_DELIVERY,PICKUP_STATUS,DELIVERY_STATUS) VALUES( %s,%s,%s,%s,%s,%s,%s,%s,%s)",(PATIENT_ID,PAYMENT_ID ,DELIVERY_PERSON_ID,DELIVERY_TIME,PATIENT_NAME,PATIENT_ADDRESS,TYPE_DELIVERY,PICKUP_STATUS,DELIVERY_STATUS))
        mysql.connection.commit()
        cursor.close()
        return 'success'
     elif request.method == 'GET':
         d = request.json
         cur = mysql.connection.cursor()
         cur.execute("SELECT * FROM OUT_FOR_DELIVERY")
         fetchdata = cur.fetchall()
         cur.close()
         return jsonify(fetchdata) 
     return 'unsuccess'
    
    
    
    
if __name__ == '__main__':
    app.run()