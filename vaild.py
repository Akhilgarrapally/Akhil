from flask import Flask,request
from flask_mysqldb import MySQL
from flask_jwt import jwt
import datetime
from functools import wraps
from flask_cors import CORS

app = Flask("__name__")

app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']="Akhilyuvi143@"
app.config['MYSQL_DB']="data"

mysql = MySQL(app)

@app.route("/",methods = ['GET','POST'])
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
        symbols = ['$', '@', '#', '%']
        if not USER_NAME:
            return 'user_name is missing'
        if not USER_MAIL_ID or '@' not in USER_MAIL_ID:
            return 'user_mail_id is missing'
        if not USER_PHONE_NUMBER :
            return 'user_phone_number is missing'
        if len(USER_PHONE_NUMBER) != 10:
            return "Enter Valid user_phone_number"
        if not USER_PASSWORD:
            return 'user_password is missing'
        if len(USER_PASSWORD) < 5:
            return 'user_password is should not be less than 6 characters'
        if len(USER_PASSWORD) > 20:
            return 'length should be not be greater than 10'
        if not any(char.isdigit() for char in USER_PASSWORD):
            return 'Password should have at least one numeral'
        if not any(char.isupper() for char in USER_PASSWORD):
            return 'Password should have at least one uppercase letter'
        if not any(char.islower() for char in USER_PASSWORD):
            return 'Password should have at least one lowercase letter'
        if not any(char in symbols for char in USER_PASSWORD):
            return 'Password should have at least one of the symbols '
        #if USER_PASSWORD != USER_CONFRIM_PASSWORD:
         #   return "user_confrim_password must be same as user_password"
        if not USER_IP:
            return 'user_ip is missing'
        if not USER_DATE_CREATED:
            return 'user_date_created is missing'
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO USER_SIGNUP(USER_SIGNUP_ID,USER_ID,USER_NAME,USER_MAIL_ID,USER_PHONE_NUMBER,USER_PASSWORD,USER_IP,USER_DATE_CREATED) VALUES( %s,%s,%s,%s,%s,%s,%s,%s)",(USER_SIGNUP_ID,USER_ID,USER_NAME,USER_MAIL_ID,USER_PHONE_NUMBER,USER_PASSWORD,USER_IP,USER_DATE_CREATED))
        mysql.connection.commit()
        cursor.close()
        return 'success'
     else:
        return 'unsuccess'
        

   

if __name__ == '__main__':
    app.run()
