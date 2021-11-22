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

@app.route("/TEST_RESULT",methods = ['GET','POST'])
def index():
     if request.method=='POST':
        d=request.json
        SESSION_ID=d['SESSION_ID']
        TEST_ID=d['TEST_ID']
        TEST_RESULT=d['TEST_RESULT']
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO TEST_RESULT(SESSION_ID , TEST_ID , TEST_RESULT ) VALUES( %s,%s,%s)",(SESSION_ID , TEST_ID , TEST_RESULT))
        mysql.connection.commit()
        cursor.close()
        return 'success'
     else:
        return 'unsuccess'
        

   

if __name__ == '__main__':
    app.run()
