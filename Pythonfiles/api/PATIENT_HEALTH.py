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

@app.route("/PATIENT_HEALTH",methods = ['GET','POST'])
def index():
     if request.method=='POST':
        d=request.json
        PATIENT_HEALTH_ID=d['PATIENT_HEALTH_ID']
        PATIENT_ID=d['PATIENT_ID']
        BLOOD_GROUP=d['BLOOD_GROUP']                
        PATIENT_AGE=d['PATIENT_AGE']
        PATIENT_WEIGHT=d['PATIENT_WEIGHT']
        PATIENT_HEIGHT=d['PATIENT_HEIGHT'] 
        PATIENT_SYSTOLIC_BP=d['PATIENT_SYSTOLIC_BP']
        PATIENT_DYASTOLIC_BP=d['PATIENT_DYASTOLIC_BP']
        PATIENT_TEMPARATURE=d['PATIENT_TEMPARATURE']
        CREATED_BY=d['CREATED_BY']
        IP_ADDRESS=d['IP_ADDRESS']
        CREATED_DATE=d['CREATED_DATE']
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO PATIENT_HEALTH(PATIENT_HEALTH_ID,PATIENT_ID,BLOOD_GROUP,PATIENT_AGE,PATIENT_WEIGHT,PATIENT_HEIGHT,PATIENT_SYSTOLIC_BP,PATIENT_DYASTOLIC_BP,PATIENT_TEMPARATURE,CREATED_BY,IP_ADDRESS,CREATED_DATE) VALUES( %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(PATIENT_HEALTH_ID,PATIENT_ID,BLOOD_GROUP,PATIENT_AGE,PATIENT_WEIGHT,PATIENT_HEIGHT,PATIENT_SYSTOLIC_BP,PATIENT_DYASTOLIC_BP,PATIENT_TEMPARATURE,CREATED_BY,IP_ADDRESS,CREATED_DATE))
        mysql.connection.commit()
        cursor.close()
        return 'success'
     else:
        return 'unsuccess'
        

   

if __name__ == '__main__':
    app.run()
