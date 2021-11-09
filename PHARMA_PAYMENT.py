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

@app.route("/PHARMA_PAYMENT",methods = ['GET','POST'])
def PHARMA_PAYMENT():
     if request.method=='POST':
        d=request.json
        PAYMENT_ID = d['PAYMENT_ID']
        REQUEST_ID = d['REQUEST_ID']
        TRANSACTION_ID = d['TRANSACTION_ID']
        PAYMENT_TYPE = d['PAYMENT_TYPE']
        PAYMENT_STATUS = d['PAYMENT_STATUS']
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO PHARMA_PAYMENT(PAYMENT_ID,REQUEST_ID ,TRANSACTION_ID,PAYMENT_TYPE,PAYMENT_STATUS) VALUES( %s,%s,%s,%s,%s)",(PAYMENT_ID,REQUEST_ID ,TRANSACTION_ID,PAYMENT_TYPE,PAYMENT_STATUS))
        mysql.connection.commit()
        cursor.close()
        return 'success'
     elif request.method == 'GET':
         d = request.json
         cur = mysql.connection.cursor()
         cur.execute("SELECT * FROM PHARMA_PAYMENT")
         fetchdata = cur.fetchall()
         cur.close()
         return jsonify(fetchdata) 
     return 'unsuccess'
    
    
    
    
if __name__ == '__main__':
    app.run()