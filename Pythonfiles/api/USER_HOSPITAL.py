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

@app.route("/USER_HOSPITAL",methods = ['GET','POST'])
def index():
     if request.method=='POST':
        d=request.json
        USER_HOSPITAL_ID=d['USER_HOSPITAL_ID']
        USER_ID=d['USER_ID']
        HOSPITAL_NAME = d['HOSPITAL_NAME']
        HOSPITAL_ADDRESS=d['HOSPITAL_ADDRESS']
        HOSPITAL_CITY = d['HOSPITAL_CITY']
        HOSPPITAL_STATE = d['HOSPPITAL_STATE']
        HOSPITAL_ZIP_CODE = d['HOSPITAL_ZIP_CODE']
        

        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO USER_HOSPITAL(USER_HOSPITAL_ID,USER_ID,HOSPITAL_NAME,HOSPITAL_ADDRESS,HOSPITAL_CITY,HOSPPITAL_STATE,HOSPITAL_ZIP_CODE) VALUES( %s,%s,%s,%s,%s,%s,%s)",(USER_HOSPITAL_ID,USER_ID,HOSPITAL_NAME,HOSPITAL_ADDRESS,HOSPITAL_CITY,HOSPPITAL_STATE,HOSPITAL_ZIP_CODE))
        mysql.connection.commit()
        cursor.close()
        return 'success'
     else:
        return 'unsuccess'
        

   

if __name__ == '__main__':
    app.run()
