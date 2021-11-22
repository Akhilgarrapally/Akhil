from flask import Flask,request,jsonify
from flask_cors import CORS
from flask_mysqldb import MySQL
app = Flask("__name__")

app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']="Akhil"
app.config['MYSQL_DB']="clinicalfirst_pharmacy_dashboard"

mysql = MySQL(app)
CORS(app)

@app.route("/PHARMA_SIGNUP",methods = ['GET','POST'])
def PHARMA_SIGNUP():
     if request.method=='POST':
        d=request.json
        # PHARMA_SIGNUP_ID = d['PHARMA_SIGNUP_ID']
        PHARMA_NAME = d['PHARMA_NAME']
        PHARMA_MAIL_ID = d['PHARMA_MAIL_ID']
        PHARMA_PHONE_NUMBER = d['PHARMA_PHONE_NUMBER']
        PHARMA_PASSWORD = d['PHARMA_PASSWORD']
        PHARMA_IP = d['PHARMA_IP']
        PHARMA_DATE_CREATED = d['PHARMA_DATE_CREATED']
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO PHARMA_SIGNUP(PHARMA_NAME ,PHARMA_MAIL_ID,PHARMA_PHONE_NUMBER,PHARMA_PASSWORD,PHARMA_IP,PHARMA_DATE_CREATED) VALUES( %s,%s,%s,%s,%s,%s)",(PHARMA_NAME ,PHARMA_MAIL_ID,PHARMA_PHONE_NUMBER,PHARMA_PASSWORD,PHARMA_IP,PHARMA_DATE_CREATED))
        mysql.connection.commit()
        cursor.close()
        return 'success'
     elif request.method == 'GET':
         d = request.json
         cur = mysql.connection.cursor()
         cur.execute("SELECT * FROM PHARMA_SIGNUP")
         fetchdata = cur.fetchall()
         cur.close()
         return jsonify(fetchdata) 
     return 'unsuccess'

@app.route("/PHARMA_REGISTRATION",methods = ['GET','POST'])
def PHARMA_REGISTRATION():
     if request.method=='POST':
        d=request.json
        # PHARMA_REG_ID=d['PHARMA_REG_ID']
        PHARMA_ID=d['PHARMA_ID']
        PHARMA_RATING=d['PHARMA_RATING']
        PHARMA_LICENSE_NUMBER=d['PHARMA_LICENSE_NUMBER']
        FLAT_NO=d['FLAT_NO']
        STREET_NAME=d['STREET_NAME']
        CITY_NAME=d['CITY_NAME'] 
        STATE_NAME=d['STATE_NAME']
        COUNTRY_NAME=d['COUNTRY_NAME']
        ZIP_CODE=d['ZIP_CODE']
        PHARMA_APPROVED=d['PHARMA_APPROVED']
        PHARMA_IP=d['PHARMA_IP']
        PHARMA_DATE_REGISTERED=d['PHARMA_DATE_REGISTERED']
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO PHARMA_REGISTRATION(PHARMA_ID,PHARMA_RATING,PHARMA_LICENSE_NUMBER,FLAT_NO,STREET_NAME,CITY_NAME,STATE_NAME,COUNTRY_NAME,ZIP_CODE,PHARMA_APPROVED,PHARMA_IP,PHARMA_DATE_REGISTERED) VALUES( %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(PHARMA_ID,PHARMA_RATING,PHARMA_LICENSE_NUMBER,FLAT_NO,STREET_NAME,CITY_NAME,STATE_NAME,COUNTRY_NAME,ZIP_CODE,PHARMA_APPROVED,PHARMA_IP,PHARMA_DATE_REGISTERED))
        mysql.connection.commit()
        cursor.close()
        return 'success'
     elif request.method == 'GET':
         d = request.json
         cur = mysql.connection.cursor()
         cur.execute("SELECT * FROM PHARMA_REGISTRATION")
         fetchdata = cur.fetchall()
         cur.close()
         return jsonify(fetchdata) 
     return 'unsuccess'

@app.route("/PATIENT_PRESCRIPTION",methods = ['GET','POST'])
def PATIENT_PRESCRIPTION():
     if request.method=='POST':
        d=request.json
        # PRESCRIPTION_ID = d['PRESCRIPTION_ID']
        PATIENT_ID = d['PATIENT_ID']
        PATIENT_NAME = d['PATIENT_NAME']
        DOCTOR_ID = d['DOCTOR_ID']
        DOCTOR_NAME = d['DOCTOR_NAME']
        DOCTOR_LICENCE = d['DOCTOR_LICENCE']
        MEDICINE_NAME = d['MEDICINE_NAME']
        MEDICINE_QUANTITY = d['MEDICINE_QUANTITY']
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO PATIENT_PRESCRIPTION(PATIENT_ID ,PATIENT_NAME,DOCTOR_ID,DOCTOR_NAME,DOCTOR_LICENCE,MEDICINE_NAME,MEDICINE_QUANTITY) VALUES(%s,%s,%s,%s,%s,%s,%s)",(PATIENT_ID ,PATIENT_NAME,DOCTOR_ID,DOCTOR_NAME,DOCTOR_LICENCE,MEDICINE_NAME,MEDICINE_QUANTITY))
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

@app.route("/PHARMA_MEDICINE_STOCK",methods = ['GET','POST'])
def PHARMA_MEDICINE_STOCK():
     if request.method=='POST':
        d=request.json
        # MEDICINE_ID = d['MEDICINE_ID']
        MEDICINE_NAME = d['MEDICINE_NAME']
        PHARMA_ID = d['PHARMA_ID']
        MEDICINE_STOCK_AVAILABILITY = d['MEDICINE_STOCK_AVAILABILITY']
        MEDICINE_MRP = d['MEDICINE_MRP']
        MEDICINE_DISCOUNT = d['MEDICINE_DISCOUNT']
        MEDICINE_FINAL_PRICE = d['MEDICINE_FINAL_PRICE']
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO PHARMA_MEDICINE_STOCK(MEDICINE_NAME ,PHARMA_ID,MEDICINE_STOCK_AVAILABILITY,MEDICINE_MRP,MEDICINE_DISCOUNT,MEDICINE_FINAL_PRICE) VALUES( %s,%s,%s,%s,%s,%s)",(MEDICINE_NAME ,PHARMA_ID,MEDICINE_STOCK_AVAILABILITY,MEDICINE_MRP,MEDICINE_DISCOUNT,MEDICINE_FINAL_PRICE))
        mysql.connection.commit()
        cursor.close()
        return 'success'
     elif request.method == 'GET':
         d = request.json
         cur = mysql.connection.cursor()
         cur.execute("SELECT * FROM PHARMA_MEDICINE_STOCK")
         fetchdata = cur.fetchall()
         cur.close()
         return jsonify(fetchdata) 
     return 'unsuccess'    

@app.route("/PHARMA_REQUESTS",methods = ['GET','POST'])
def PHARMA_REQUESTS():
     if request.method=='POST':
        d=request.json
        # REQUEST_ID = d['REQUEST_ID']
        PRESCRIPTION_ID = d['PRESCRIPTION_ID']
        REQUEST_STATUS = d['REQUEST_STATUS']
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO PHARMA_REQUESTS(PRESCRIPTION_ID , REQUEST_STATUS) VALUES( %s,%s)",(PRESCRIPTION_ID , REQUEST_STATUS))
        mysql.connection.commit()
        cursor.close()
        return 'success'
     elif request.method == 'GET':
         d = request.json
         cur = mysql.connection.cursor()
         cur.execute("SELECT * FROM PHARMA_REQUESTS")
         fetchdata = cur.fetchall()
         cur.close()
         return jsonify(fetchdata) 
     return 'unsuccess'

@app.route("/PHARMA_PAYMENT",methods = ['GET','POST'])
def PHARMA_PAYMENT():
     if request.method=='POST':
        d=request.json
        # PAYMENT_ID = d['PAYMENT_ID']
        REQUEST_ID = d['REQUEST_ID']
        TRANSACTION_ID = d['TRANSACTION_ID']
        PAYMENT_TYPE = d['PAYMENT_TYPE']
        PAYMENT_STATUS = d['PAYMENT_STATUS']
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO PHARMA_PAYMENT(REQUEST_ID ,TRANSACTION_ID,PAYMENT_TYPE,PAYMENT_STATUS) VALUES(%s,%s,%s,%s)",(REQUEST_ID ,TRANSACTION_ID,PAYMENT_TYPE,PAYMENT_STATUS))
        mysql.connection.commit()
        cursor.close()
        return 'success'
     elif request.method == 'GET':
         d = request.json
         cur = mysql.connection.cursor()
         cur.execute("SELECT * FROM PHARMA_PAYMENT")
         fetchdata = cur.fetchall()
         cur.close()
         return jsonify(fetchdata) 
     return 'unsuccess'

@app.route("/PHARMA_DELIVERY_PERSON",methods = ['GET','POST'])
def PHARMA_DELIVERY_PERSON():
     if request.method=='POST':
        d=request.json
        # DELIVERY_PERSON_ID = d['DELIVERY_PERSON_ID']
        DELIVERY_NAME = d['DELIVERY_NAME']
        DELIVERY_PHONE_NUMBER = d['DELIVERY_PHONE_NUMBER']
        DELIVERY_DRIVING_LICENCE_NUMBER = d['DELIVERY_DRIVING_LICENCE_NUMBER']
        DELIVERY_PRESENT_LOCATION = d['DELIVERY_PRESENT_LOCATION']
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO PHARMA_DELIVERY_PERSON(DELIVERY_NAME ,DELIVERY_PHONE_NUMBER,DELIVERY_DRIVING_LICENCE_NUMBER,DELIVERY_PRESENT_LOCATION) VALUES( %s,%s,%s,%s)",(DELIVERY_NAME ,DELIVERY_PHONE_NUMBER,DELIVERY_DRIVING_LICENCE_NUMBER,DELIVERY_PRESENT_LOCATION))
        mysql.connection.commit()
        cursor.close()
        return 'success'
     elif request.method == 'GET':
         d = request.json
         cur = mysql.connection.cursor()
         cur.execute("SELECT * FROM PHARMA_DELIVERY_PERSON")
         fetchdata = cur.fetchall()
         cur.close()
         return jsonify(fetchdata) 
     return 'unsuccess'
 
@app.route("/PHARMA_OUT_FOR_DELIVERY",methods = ['GET','POST'])
def PHARMA_OUT_FOR_DELIVERY():
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
        cursor.execute("INSERT INTO PHARMA_OUT_FOR_DELIVERY(PATIENT_ID,PAYMENT_ID ,DELIVERY_PERSON_ID,DELIVERY_TIME,PATIENT_NAME,PATIENT_ADDRESS,TYPE_DELIVERY,PICKUP_STATUS,DELIVERY_STATUS) VALUES( %s,%s,%s,%s,%s,%s,%s,%s,%s)",(PATIENT_ID,PAYMENT_ID ,DELIVERY_PERSON_ID,DELIVERY_TIME,PATIENT_NAME,PATIENT_ADDRESS,TYPE_DELIVERY,PICKUP_STATUS,DELIVERY_STATUS))
        mysql.connection.commit()
        cursor.close()
        return 'success'
     elif request.method == 'GET':
         d = request.json
         cur = mysql.connection.cursor()
         cur.execute("SELECT * FROM PHARMA_OUT_FOR_DELIVERY")
         fetchdata = cur.fetchall()
         cur.close()
         return jsonify(fetchdata) 
     return 'unsuccess'
           
    
    
if __name__ == '__main__':
    app.run()