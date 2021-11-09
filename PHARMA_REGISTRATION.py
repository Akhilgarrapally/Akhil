from flask import Flask,request,jsonify
from flask_cors import CORS
from flask_mysqldb import MySQL
app = Flask("__name__")

app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_PHARMA']="root"
app.config['MYSQL_PASSWORD']="Akhilyuvi143@"
app.config['MYSQL_DB']="clinicalfirst_pharmacy_dashboard"

mysql = MySQL(app)
CORS(app)

@app.route("/PHARMA_REGISTRATION",methods = ['GET','POST'])
def PHARMA_REGISTRATION():
     if request.method=='POST':
        d=request.json
        PHARMA_REG_ID=d['PHARMA_REG_ID']
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
        cursor.execute("INSERT INTO PHARMA_REGISTRATION(PHARMA_REG_ID,PHARMA_ID,PHARMA_RATING,PHARMA_LICENSE_NUMBER,FLAT_NO,STREET_NAME,CITY_NAME,STATE_NAME,COUNTRY_NAME,ZIP_CODE,PHARMA_APPROVED,PHARMA_IP,PHARMA_DATE_REGISTERED) VALUES( %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(PHARMA_REG_ID,PHARMA_ID,PHARMA_RATING,PHARMA_LICENSE_NUMBER,FLAT_NO,STREET_NAME,CITY_NAME,STATE_NAME,COUNTRY_NAME,ZIP_CODE,PHARMA_APPROVED,PHARMA_IP,PHARMA_DATE_REGISTERED))
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


if __name__ == '__main__':
    app.run()