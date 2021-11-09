from flask import Flask, render_template, request,redirect
from flask_mysqldb import MySQL
from flask import jsonify
import socket   
app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Akhilyuvi143@'
app.config['MYSQL_DB'] = 'data'


    

mysql = MySQL(app)


@app.route("/data", methods=['GET','POST'])
def request_doct():
     if request.method == 'POST':
        # REQUEST_ID = request.json['REQUEST_ID']
         PATIENT_ID = request.json['PATIENT_ID']
         TIME_SLOTS = request.json['TIME_SLOTS']
         AVALIABLITY_STATUS = request.json['AVALIABLITY_STATUS']
         TRANSACTION_ID = request.json['TRANSACTION_ID']
         hostname = socket.gethostname()   
         IPAddr = socket.gethostbyname(hostname)   
         cur = mysql.connection.cursor()
         cur.execute('INSERT INTO request_doct( PATIENT_ID,TIME_SLOTS,AVALIABLITY_STATUS,TRANSACTION_ID, IP_ADDRESS) VALUES (%s, %s, %s, %s, %s)', 
                       ( PATIENT_ID, TIME_SLOTS,AVALIABLITY_STATUS,TRANSACTION_ID, IPAddr))
         mysql.connection.commit()
         cur.close()
         
         return jsonify('data enterd successfully')
     else : 
         return jsonify('data not enetered into database')    


@app.route("/availabilty", methods=['GET','POST'])
def doct_availabity():
    if request.method == 'GET':
        PATIENT_ID = request.json['PATIENT_ID']
        REQUEST_ID = request.json['REQUEST_ID']
        cur = mysql.connection.cursor()
        cur.execute('SELECT AVALIABLITY_STATUS FROM request_doct WHERE REQUEST_ID = % s AND PATIENT_ID = % s',
                       (REQUEST_ID, PATIENT_ID))
        
        account = cur.fetchone()
       
        print(account)
        print(type(account))
        akhil =account[0]
        if akhil==0:
           hi = doc_list()
           print(hi)

           return jsonify('sorry doctor is unavailable',hi)
        else:
           hi= payment_gateway()
           return jsonify('doctor is available',hi)
    else:
        return jsonify('unsuccess')  




def doc_list():
    return 'list of doctors'

def payment_gateway():
    
    return "integrate payment gateway"
if __name__ == '__main__':
    app.run()