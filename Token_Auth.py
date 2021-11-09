from flask import Flask, render_template, request,redirect
from flask_mysqldb import MySQL
from flask import jsonify
import hashlib
import jwt
import datetime
import time
import socket   
from flask_cors import CORS


from functools import wraps

app = Flask(__name__)

app.config['SECRET_KEY'] = 'thisisthesecretkey'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Akhil'
app.config['MYSQL_DB'] = 'data'

mysql = MySQL(app)
CORS(app)

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        if not token:
            return jsonify({'message':'Token is missing!!!'})
        try:
            data = jwt.decode(token,app.config['SECRET_KEY'])
        except:
            return jsonify({'message':'Token is invalid'})
        return f(*args, **kwargs)
    return decorated

@app.route("/login", methods=['GET','POST'])
def login():
    if request.method == 'POST':
        
       USER_MAIL_ID = request.json['USER_MAIL_ID']
       USER_PASSWORD = request.json['USER_PASSWORD']
       j = hashlib.md5(USER_PASSWORD.encode())
       print(j.hexdigest())
       cur = mysql.connection.cursor()
       cur.execute('SELECT * FROM USER_SIGNUP1 WHERE USER_MAIL_ID = % s AND USER_PASSWORD = % s',
                       (USER_MAIL_ID, j.hexdigest()))
       account = cur.fetchone()
       if account:
            print(account)
           
            
            token = jwt.encode({'USER_MAIL_ID' : USER_MAIL_ID,'USER_PASSWORD': USER_PASSWORD, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])

            
            return jsonify({'token' : token.decode('UTF-8')})
            # return jsonify({'Login succesful and the token is': token})
       else:
            return jsonify('Unable to login')
    
    return jsonify('Unable to logi')
    
@app.route('/signup', methods=['POST'])
def USER_SIGNUP():
    if request.method == 'POST':
       try: 
         USER_SIGN_UP_ID = request.json['USER_SIGN_UP_ID']  
         
         USER_ID = request.json['USER_ID']
         USER_NAME = request.json['USER_NAME']
         USER_MAIL_ID = request.json['USER_MAIL_ID']
         USER_PHONE_NUMBER = request.json['USER_PHONE_NUMBER']
         USER_PASSWORD = request.json['USER_PASSWORD']
         #USER_IP = request.json['USER_IP']
         #USER_DATE_CREATED = request.json['USER_DATE_CREATED']
              
         h = hashlib.md5(USER_PASSWORD.encode())
         hostname = socket.gethostname()   
         IPAddr = socket.gethostbyname(hostname)   
         cur = mysql.connection.cursor()
         cur.execute('INSERT INTO USER_SIGNUP1(USER_SIGN_UP_ID,USER_ID,USER_NAME,USER_MAIL_ID,USER_PHONE_NUMBER,USER_PASSWORD,USER_IP,USER_HOSTNAME) VALUES (%s,%s,%s, %s, %s, %s, %s,%s)',(USER_SIGN_UP_ID,USER_ID,USER_NAME,USER_MAIL_ID,USER_PHONE_NUMBER,h.hexdigest(),IPAddr,hostname))
         mysql.connection.commit()
         cur.close()
         return jsonify('signup successful')
    
       except:
          return jsonify('user already exists try login or signup with different credentials')  
    
    
@app.route('/auth', methods=['GET', 'POST'])
@token_required
def user():
    if request.method == 'GET':
        details = request.json
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM user_signup1")
        fetchdata = cur.fetchall()
        cur.close()
        return jsonify(fetchdata)
    return 'Unsuccess'


if __name__ == '__main__':
    app.run()