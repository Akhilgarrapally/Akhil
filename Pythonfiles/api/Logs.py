from flask import Flask,request,session,jsonify
from flask_cors import CORS
from flask_mysqldb import MySQL
from flask_session import Session
app = Flask("__name__")

app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']="Akhilyuvi143@"
app.config['MYSQL_DB']="data"

mysql = MySQL(app)
CORS(app)


@app.route("/LOGS",methods = ['GET','POST'])
def index():
     if request.method=='POST':
        d=request.json
        LOG_ID=d['LOG_ID']
        LOGIN_EMAIL_ID=d['LOGIN_EMAIL_ID']
        LOGIN_TIME=d['LOGIN_TIME']
        LOGOUT_TIME=d['LOGOUT_TIME']
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO LOGS(LOG_ID,LOGIN_EMAIL_ID,LOGIN_TIME,LOGOUT_TIME) VALUES( %s,%s,%s,%s)",(LOG_ID,LOGIN_EMAIL_ID,LOGIN_TIME,LOGOUT_TIME))
        mysql.connection.commit()
        cursor.close()
        return 'success'
     else:
        return 'unsuccess'
        
# @app.route('/h', methods=['POST','GET'])
# def get():
#     if request.method == "POST":
#         d = request.json
#         LOGIN_EMAIL_ID = d['LOGIN_EMAIL_ID']
#         cur = mysql.connection.cursor()
#         cur.execute('SELECT * FROM logs WHERE LOGIN_EMAIL_ID = % s ',(LOGIN_EMAIL_ID,))
#         fdata = cur.fetchone()
#         if fdata:
#             session['LOGIN_EMAIL_ID'] = fdata['LOGIN_EMAIL_ID']
#             return session.get('LOGIN_EMAIL_ID')
#         return "Not Present in This LOGS"
   

if __name__ == '__main__':
    app.run()
