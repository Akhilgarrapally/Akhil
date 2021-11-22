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

@app.route("/USER_SPECIALIZATION",methods = ['GET','POST'])
def index():
     if request.method=='POST':
        d=request.json
        USER_SPECIALIZATION_ID=d['USER_SPECIALIZATION_ID']
        USER_ID=d['USER_ID']
        SPECIALIZATION_NAME=d['SPECIALIZATION_NAME']
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO USER_SPECIALIZATION(USER_SPECIALIZATION_ID,USER_ID,SPECIALIZATION_NAME) VALUES( %s,%s,%s)",(USER_SPECIALIZATION_ID,USER_ID,SPECIALIZATION_NAME))
        mysql.connection.commit()
        cursor.close()
        return 'success'
     else:
        return 'unsuccess'
        

   

if __name__ == '__main__':
    app.run()