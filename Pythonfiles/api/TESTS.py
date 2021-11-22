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

@app.route("/TESTS",methods = ['GET','POST'])
def index():
     if request.method=='POST':
        d=request.json
        SESSION_ID=d['SESSION_ID']
        TEST_ID=d['TEST_ID']
        TEST_NAME=d['TEST_NAME']
        DISEASE_NAME=d['DISEASE_NAME']
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO TESTS(SESSION_ID , TEST_ID , TEST_NAME , DISEASE_NAME) VALUES( %s,%s,%s,%s)",(SESSION_ID , TEST_ID , TEST_NAME , DISEASE_NAME))
        mysql.connection.commit()
        cursor.close()
        return 'success'
     else:
        return 'unsuccess'
        

   

if __name__ == '__main__':
    app.run()
