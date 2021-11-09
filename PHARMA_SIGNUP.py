from flask import Flask,request,jsonify
from flask_cors import CORS
from flask_mysqldb import MySQL
app = Flask("__name__")

app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']="Akhilyuvi143@"
app.config['MYSQL_DB']="clinicalfirst_pharmacy_dashboard"

mysql = MySQL(app)
CORS(app)

@app.route("/PHARMA_SIGNUP",methods = ['GET','POST'])
def PHARMA_SIGNUP():
     if request.method=='POST':
        d=request.json
        PHARMA_SIGNUP_ID = d['PHARMA_SIGNUP_ID']
        PHARMA_NAME = d['PHARMA_NAME']
        PHARMA_MAIL_ID = d['PHARMA_MAIL_ID']
        PHARMA_PHONE_NUMBER = d['PHARMA_PHONE_NUMBER']
        PHARMA_PASSWORD = d['PHARMA_PASSWORD']
        PHARMA_IP = d['PHARMA_IP']
        PHARMA_DATE_CREATED = d['PHARMA_DATE_CREATED']
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO PHARMA_SIGNUP(PHARMA_SIGNUP_ID,PHARMA_NAME ,PHARMA_MAIL_ID,PHARMA_PHONE_NUMBER,PHARMA_PASSWORD,PHARMA_IP,PHARMA_DATE_CREATED) VALUES( %s,%s,%s,%s,%s,%s,%s)",(PHARMA_SIGNUP_ID,PHARMA_NAME ,PHARMA_MAIL_ID,PHARMA_PHONE_NUMBER,PHARMA_PASSWORD,PHARMA_IP,PHARMA_DATE_CREATED))
        mysql.connection.commit()
        cursor.close()
        return 'success'
     elif request.method == 'GET':
         d = request.json
         cur = mysql.connection.cursor()
         cur.execute("SELECT * FROM PHARMA_SIGNUP")
         fetchdata = cur.fetchall()
         cur.close()
         return jsonify(fetchdata) 
     return 'unsuccess'
    
    
    
    
if __name__ == '__main__':
    app.run()