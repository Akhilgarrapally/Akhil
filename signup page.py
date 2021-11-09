from flask import Flask,request,render_template,request
from flask_mysqldb import MySQL
app = Flask(__name__)


app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']="Akhilyuvi143@"
app.config['MYSQL_DB']="flask_signup"

mysql = MySQL(app)

@app.route("/",methods = ['GET','POST'])
def index():
    if request.method=='POST':
        d=request.json
        name=d['name']
        emailid = d['emailid']
        password=d['password']
        reenterpassword = d['reenterpassword']
        cursor = mysql.Connection.cursor()
        cursor.execute("INSERT INTO signup(name,emailid,password,reenterpassword) VALUES( %s,%s,%s,%s)",(name,emailid,password,reenterpassword))
        mysql.Connection.commit()
        cursor.close()
        return 'success'
    else:
        return 'unsuccess'

   

if __name__ == '__main__':
    app.run()
    
    
    
    
    
    
    