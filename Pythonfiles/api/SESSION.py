from flask import Flask,request,session,jsonify
from flask_cors import CORS
from flask_mysqldb import MySQL
from flask_session import Session

app = Flask("__name__")

app.config['SESSION_TYPE'] = "filesystem"
app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']="Akhilyuvi143@"
app.config['MYSQL_DB']="data"

mysql = MySQL(app)
CORS(app)
sess = Session()
sess.init_app(app)

@app.route("/SESSION",methods = ['GET','POST'])
def index():
     if request.method=='POST':
        d=request.json
        ID=d['ID']
        SESSION_ID=d['SESSION_ID']
        USER_ID=d['USER_ID']
        PATIENT=d['PATIENT']
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO SESSION(ID ,SESSION_ID , USER_ID , PATIENT) VALUES( %s,%s,%s,%s)",(ID , SESSION_ID , USER_ID , PATIENT))
        mysql.connection.commit()
        cursor.close()
        return 'success'
     else:
        return 'unsuccess'
 

     
       
   

if __name__ == '__main__':
    app.run()
