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

@app.route("/USER_REGISTRATION",methods = ['GET','POST'])
def index():
     if request.method=='POST':
        d=request.json
        USER_REG_ID=d['USER_REG_ID']
        USER_ID=d['USER_ID']
        USER_AGE=d['USER_AGE']
        USER_EXPERIANCE=d['USER_EXPERIANCE']
        USER_GENDER=d['USER_GENDER']
        USER_LICENSE_NUMBER=d['USER_LICENSE_NUMBER']
        FLAT_NO=d['FLAT_NO']
        STREET_NAME=d['STREET_NAME']
        CITY_NAME=d['CITY_NAME'] 
        STATE_NAME=d['STATE_NAME']
        COUNTRY_NAME=d['COUNTRY_NAME']
        ZIP_CODE=d['ZIP_CODE']
        USER_APPROVED=d['USER_APPROVED']
        USER_IP=d['USER_IP']
        USER_DATE_REGISTERED=d['USER_DATE_REGISTERED']
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO USER_REGISTRATION(USER_REG_ID,USER_ID,USER_AGE,USER_EXPERIANCE,USER_GENDER,USER_LICENSE_NUMBER,FLAT_NO,STREET_NAME,CITY_NAME,STATE_NAME,COUNTRY_NAME,ZIP_CODE,USER_APPROVED,USER_IP,USER_DATE_REGISTERED) VALUES( %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(USER_REG_ID,USER_ID,USER_AGE,USER_EXPERIANCE,USER_GENDER,USER_LICENSE_NUMBER,FLAT_NO,STREET_NAME,CITY_NAME,STATE_NAME,COUNTRY_NAME,ZIP_CODE,USER_APPROVED,USER_IP,USER_DATE_REGISTERED))
        mysql.connection.commit()
        cursor.close()
        return 'success'
     else:
        return 'unsuccess'
        

   

if __name__ == '__main__':
    app.run()
