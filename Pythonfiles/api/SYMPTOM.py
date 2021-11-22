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

@app.route("/SYMPTOM",methods = ['GET','POST'])
def index():
     if request.method=='POST':
        d=request.json
        SESSION_ID=d['SESSION_ID']
        SYMPTOM_ID=d['SYMPTOM_ID']
        SYMPTOM_NAME=d['SYMPTOM_NAME']
        INPUT=d['INPUT']
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO SYMPTOM(SESSION_ID , SYMPTOM_ID , SYMPTOM_NAME , INPUT) VALUES( %s,%s,%s,%s)",(SESSION_ID , SYMPTOM_ID , SYMPTOM_NAME , INPUT))
        mysql.connection.commit()
        cursor.close()
        return 'success'
     else:
        return 'unsuccess'
        

   

if __name__ == '__main__':
    app.run()

