from flask import Flask,request,session,jsonify
from flask_cors import CORS
from flask_mysqldb import MySQL
from flask_caching import Cache


 
app = Flask("__name__")
cache = Cache()


app.config['CACHE_TYPE'] = 'simple'
app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']="Akhilyuvi143@"
app.config['MYSQL_DB']="data"

mysql = MySQL(app)
CORS(app)
cache.init_app(app)
# @cache.cached(timeout=2)
# def hello_world():
#     randomnum =  randint(1,10)
#     return f'<h1> THE NUMBER IS :{randomnum}</h1>'

@app.route("/USER_SIGNUP",methods = ['GET','POST'])
def index():
     if request.method=='POST':
        d=request.json
        USER_SIGNUP_ID=d['USER_SIGNUP_ID']
        USER_ID = d['USER_ID']
        USER_NAME = d['USER_NAME']
        USER_MAIL_ID=d['USER_MAIL_ID']
        USER_PHONE_NUMBER=d['USER_PHONE_NUMBER']
        USER_PASSWORD=d['USER_PASSWORD']
        USER_IP=d['USER_IP']
        USER_DATE_CREATED=d['USER_DATE_CREATED']
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO USER_SIGNUP(USER_SIGNUP_ID,USER_ID,USER_NAME,USER_MAIL_ID,USER_PHONE_NUMBER,USER_PASSWORD,USER_IP,USER_DATE_CREATED) VALUES( %s,%s,%s,%s,%s,%s,%s,%s)",(USER_SIGNUP_ID,USER_ID,USER_NAME,USER_MAIL_ID,USER_PHONE_NUMBER,USER_PASSWORD,USER_IP,USER_DATE_CREATED))
        mysql.connection.commit()
        cursor.close()
        return 'success'
     else:
        return 'unsuccess'
@app.route('/cache', methods=['POST','GET'] )
@cache.cached(timeout=10)
def hello():
    cur = mysql.connection.cursor()
    cur.execute('select USER_NAME from USER_SIGNUP order by rand() limit 1')
    fdata = cur.fetchall()
    return jsonify(fdata)
    
     

   

if __name__ == '__main__':
    app.run()
