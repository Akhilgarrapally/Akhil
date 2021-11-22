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

@app.route("/DIAGNOSIS_SAMPLES",methods = ['GET','POST'])
def index():
     if request.method=='POST':
        d=request.json
        SAMPLE_TABLE_ID=d['SAMPLE_TABLE_ID']
        SAMPLE_ID=d['SAMPLE_ID']
        REQUEST_ID=d['REQUEST_ID']
        COLLECTED_DATETIME=d['COLLECTED_DATETIME']
        SAMPLE_COLLECTED_FROM=d['SAMPLE_COLLECTED_FROM']
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO DIAGNOSIS_SAMPLES(SAMPLE_TABLE_ID , SAMPLE_ID  , REQUEST_ID ,  COLLECTED_DATETIME , SAMPLE_COLLECTED_FROM) VALUES( %s,%s,%s,%s,%s)",
                       (SAMPLE_TABLE_ID , SAMPLE_ID ,  REQUEST_ID ,  COLLECTED_DATETIME , SAMPLE_COLLECTED_FROM))
        mysql.connection.commit()
        cursor.close()
        return 'success'
     else:
        return 'unsuccess'
        

   

if __name__ == '__main__':
    app.run()
