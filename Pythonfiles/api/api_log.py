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

@app.route("/API_LOGS",methods = ['GET','POST'])
def index():
     if request.method=='POST':
        d=request.json
        API_ID=d['API_ID']
        API_NAME=d['API_NAME']
        ERROR_CODE=d['ERROR_CODE']
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO API_LOGS(API_ID,API_NAME,ERROR_CODE) VALUES( %s,%s,%s)",(API_ID,API_NAME,ERROR_CODE))
        mysql.connection.commit()
        cursor.close()
        return 'success'
     else:
        return 'unsuccess'
        

   

if __name__ == '__main__':
    app.run()
