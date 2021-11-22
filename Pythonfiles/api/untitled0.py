from flask import Flask, render_template, request,redirect
from flask_mysqldb import MySQL
from flask_cors import CORS
from flask import jsonify
import hashlib
import jwt
import datetime
import time
import socket   


from functools import wraps

app = Flask(__name__)

app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']="Akhilyuvi143@"
app.config['MYSQL_DB']="clinicalfirst_pharmacy_dashboard"

mysql = MySQL(app)
CORS(app)


@app.route("/login", methods=['GET','POST'])
def login():
    if request.method == 'POST':
        
       PHARMA_MAIL_ID = request.json['PHARMA_MAIL_ID']
       PHARMA_PASSWORD = request.json['PHARMA_PASSWORD']
       j = hashlib.md5(PHARMA_PASSWORD.encode())
       print(j.hexdigest())
       cur = mysql.connection.cursor()
       cur.execute('SELECT * FROM PHARMA_SIGNUP WHERE PHARMA_MAIL_ID = % s AND PHARMA_PASSWORD = % s',
                       (PHARMA_MAIL_ID, j.hexdigest()))
       account = cur.fetchone()
       if account:
            print(account)
           
            
            token = jwt.encode({'PHARMA_MAIL_ID' : PHARMA_MAIL_ID,'PHARMA_PASSWORD': PHARMA_PASSWORD, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])

            
            #return jsonify({'token' : token.decode('UTF-8')})
            return jsonify({'Login succesful and the token is': token})
       else:
            return jsonify('Unable to login')
    
    return jsonify('Unable to logi')
    
@app.route('/signup', methods=['POST'])
def PHARMA_SIGNUP():
    if request.method == 'POST':
       try: 
         PHARMA_SIGNUP_ID = request.json['PHARMA_SIGN_UP_ID']  
         
         PHARMA_ID = request.json['PHARMA_ID']
         PHARMA_NAME = request.json['PHARMA_NAME']
         PHARMA_MAIL_ID = request.json['PHARMA_MAIL_ID']
         PHARMA_PHONE_NUMBER = request.json['PHARMA_PHONE_NUMBER']
         PHARMA_PASSWORD = request.json['PHARMA_PASSWORD']
         #PHARMA_IP = request.json['PHARMA_IP']
         #PHARMA_DATE_CREATED = request.json['PHARMA_DATE_CREATED']
              
         h = hashlib.md5(PHARMA_PASSWORD.encode())
         hostname = socket.gethostname()   
         IPAddr = socket.gethostbyname(hostname)   
         cur = mysql.connection.cursor()
         cur.execute('INSERT INTO PHARMA_SIGNUP(PHARMA_SIGNUP_ID,PHARMA_ID,PHARMA_NAME,PHARMA_MAIL_ID,PHARMA_PHONE_NUMBER,PHARMA_PASSWORD,PHARMA_IP,PHARMA_HOSTNAME) VALUES (%s,%s,%s, %s, %s, %s, %s,%s)',(PHARMA_SIGNUP_ID,PHARMA_ID,PHARMA_NAME,PHARMA_MAIL_ID,PHARMA_PHONE_NUMBER,h.hexdigest(),IPAddr,hostname))
         mysql.connection.commit()
         cur.close()
         return jsonify('signup successful')
    
       except:
          return jsonify('PHARMA already exists try login or signup with different credentials')  
    

if __name__ == '__main__':
    app.run()