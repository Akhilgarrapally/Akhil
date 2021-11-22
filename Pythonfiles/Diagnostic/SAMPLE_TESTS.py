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

@app.route("/SAMPLE_TESTS",methods = ['GET','POST'])
def index():
     if request.method=='POST':
        d=request.json
        SAMPLE_TESTS_TABLE_ID=d['SAMPLE_TESTS_TABLE_ID']
        SAMPLE_ID=d['SAMPLE_ID']
        TEST_ID=d['TEST_ID']
        TESTING_DATETIME=d['TESTING_DATETIME']
        TEST_DIAGNISED=d['TEST_DIAGNISED']
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO SAMPLE_TESTS(SAMPLE_TESTS_TABLE_ID , SAMPLE_ID  , TEST_ID ,  TESTING_DATETIME , TEST_DIAGNISED) VALUES( %s,%s,%s,%s,%s)",
                       (SAMPLE_TESTS_TABLE_ID , SAMPLE_ID ,  TEST_ID ,  TESTING_DATETIME , TEST_DIAGNISED))
        mysql.connection.commit()
        cursor.close()
        return 'success'
     else:
        return 'unsuccess'
        

   

if __name__ == '__main__':
    app.run()
