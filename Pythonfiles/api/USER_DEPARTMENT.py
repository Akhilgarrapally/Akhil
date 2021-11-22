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

@app.route("/USER_DEPARTMENT",methods = ['GET','POST'])
def index():
     if request.method=='POST':
        d=request.json
        ID=d['ID']
        USER_ID=d['USER_ID']
        DEPT_ID=d['DEPT_ID']
        DEPT_NAME=d['DEPT_NAME']
        DEPT_HEAD=d['DEPT_HEAD']
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO USER_DEPARTMENT(ID,USER_ID,DEPT_ID,DEPT_NAME,DEPT_HEAD) VALUES( %s,%s,%s,%s,%s)",(ID,USER_ID,DEPT_ID,DEPT_NAME,DEPT_HEAD))
        mysql.connection.commit()
        cursor.close()
        return 'success'
     else:
        return 'unsuccess'
        

   

if __name__ == '__main__':
    app.run()
