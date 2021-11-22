from flask import Flask,request
from flask_cors import CORS
from flask_mysqldb import MySQL
app = Flask("__name__")

app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']="Akhilyuvi143@"
app.config['MYSQL_DB']="diagnostic_table"

mysql = MySQL(app)
CORS(app)

@app.route("/TEST_REQUESTS",methods = ['GET','POST'])
def index():
     if request.method=='POST':
        d=request.json
        REQUEST_TABLE_ID=d['REQUEST_TABLE_ID']
        REQUEST_ID=d['REQUEST_ID']
        DOCTOR_NAME=d['DOCTOR_NAME']
        USER_ID=d['USER_ID']
        PATIENT_ID=d['PATIENT_ID']
        REQUEST_DATETIME=d['REQUEST_DATETIME']
        REQUEST_STATUS=d['REQUEST_STATUS']
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO TEST_REQUESTS(REQUEST_TABLE_ID , REQUEST_ID , DOCTOR_NAME , USER_ID , PATIENT_ID , REQUEST_DATETIME , REQUEST_STATUS) VALUES( %s,%s,%s,%s,%s,%s,%s)",
                       (REQUEST_TABLE_ID , REQUEST_ID , DOCTOR_NAME , USER_ID , PATIENT_ID , REQUEST_DATETIME , REQUEST_STATUS))
        mysql.connection.commit()
        cursor.close()
        return 'success'
     else:
        return 'unsuccess'
        

   

if __name__ == '__main__':
    app.run()
