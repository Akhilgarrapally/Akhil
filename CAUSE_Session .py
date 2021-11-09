from flask import Flask,request,session,jsonify
from flask_cors import CORS
from flask_mysqldb import MySQL
from flask_session import Session

app = Flask("__name__")

app.config['SECRET_KEY'] ="mysecret"
app.config['SESSION_TYPE'] = "filesystem"
app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']="Akhilyuvi143@"
app.config['MYSQL_DB']="data"

mysql = MySQL(app)
CORS(app)
sess = Session()
sess.init_app(app)

@app.route("/CAUSE",methods = ['GET','POST'])
def index():
     if request.method=='POST':
        d=request.json
        SESSION_ID=d['SESSION_ID']
        CAUSE_ID=d['CAUSE_ID']
        CAUSE_NAME=d['CAUSE_NAME']
        INPUT=d['INPUT']
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO CAUSE(SESSION_ID , CAUSE_ID , CAUSE_NAME , INPUT) VALUES( %s,%s,%s,%s)",(SESSION_ID , CAUSE_ID , CAUSE_NAME , INPUT))
        mysql.connection.commit()
        cursor.close()
        return 'success'
     else:
        return 'unsuccess'
    
@app.route("/hh",methods = ['GET','POST'])       
def see():
    if request.method=='POST':
        d=request.json
        CAUSE_NAME=d['CAUSE_NAME']
        cursor = mysql.connection.cursor()
        cursor.execute('select * from CAUSE where CAUSE_NAME = %s ',(CAUSE_NAME,))
        fdata = cursor.fetchone()
        if fdata:
            session['CAUSE_NAME'] = fdata[2]  
            return session.get('CAUSE_NAME')
        return "not there in it"
        # return jsonify(fdata)
   

if __name__ == '__main__':
    app.run()

