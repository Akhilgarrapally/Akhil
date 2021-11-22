from flask import Flask,request
from flask_cors import CORS
from flask_mysqldb import MySQL
app = Flask("__name__")

app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']="Akhilyuvi143@"
app.config['MYSQL_DB']="data"

mysql = MySQL(app)
CORS(app)

@app.route("/patient_personal",methods = ['GET','POST'])
def index():
     if request.method=='POST':
        d=request.json
        PATIENT_ID=d['PATIENT_ID']
        PATIENT_NAME = d['PATIENT_NAME']
        PHONE_NUMBER = d['PHONE_NUMBER']
        MAIL_ID = d['MAIL_ID']
        FLAT_NO = d['FLAT_NO']
        STREET_NAME = d['STREET_NAME']
        CITY_NAME = d['CITY_NAME']
        STATE_NAME = d['STATE_NAME']
        COUNTRY_NAME = d['COUNTRY_NAME']
        ZIP_CODE = d['ZIP_CODE']
        DATE_OF_BIRTH = d['DATE_OF_BIRTH']
        CREATED_BY = d['CREATED_BY']
        IP_ADDRESS=d['IP_ADDRESS']
        CREATED_DATE = d['CREATED_DATE']

        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO PATIENT_PERSONAL(PATIENT_ID,PATIENT_NAME,PHONE_NUMBER,MAIL_ID,FLAT_NO,STREET_NAME,CITY_NAME,STATE_NAME,COUNTRY_NAME,ZIP_CODE,DATE_OF_BIRTH,CREATED_BY,IP_ADDRESS,CREATED_DATE) VALUES( %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(PATIENT_ID,PATIENT_NAME,PHONE_NUMBER,MAIL_ID,FLAT_NO,STREET_NAME,CITY_NAME,STATE_NAME,COUNTRY_NAME,ZIP_CODE,DATE_OF_BIRTH,CREATED_BY,IP_ADDRESS,CREATED_DATE))
        mysql.connection.commit()
        cursor.close()
        return 'success'
     else:
        return 'unsuccess'
        

   

if __name__ == '__main__':
    app.run()
