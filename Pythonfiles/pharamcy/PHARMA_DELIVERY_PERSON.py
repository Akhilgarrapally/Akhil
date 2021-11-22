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

@app.route("/PHARMA_DELIVERY_PERSON",methods = ['GET','POST'])
def PHARMA_DELIVERY_PERSON():
     if request.method=='POST':
        d=request.json
        DELIVERY_PERSON_ID = d['DELIVERY_PERSON_ID']
        DELIVERY_NAME = d['DELIVERY_NAME']
        DELIVERY_PHONE_NUMBER = d['DELIVERY_PHONE_NUMBER']
        DELIVERY_DRIVING_LICENCE_NUMBER = d['DELIVERY_DRIVING_LICENCE_NUMBER']
        DELIVERY_PRESENT_LOCATION = d['DELIVERY_PRESENT_LOCATION']
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO PHARMA_DELIVERY_PERSON(DELIVERY_PERSON_ID,DELIVERY_NAME ,DELIVERY_PHONE_NUMBER,DELIVERY_DRIVING_LICENCE_NUMBER,DELIVERY_PRESENT_LOCATION) VALUES( %s,%s,%s,%s,%s)",(DELIVERY_PERSON_ID,DELIVERY_NAME ,DELIVERY_PHONE_NUMBER,DELIVERY_DRIVING_LICENCE_NUMBER,DELIVERY_PRESENT_LOCATION))
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
    
    
    
    
if __name__ == '__main__':
    app.run()