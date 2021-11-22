from flask import Flask,request
from flask_cors import CORS
from flask_mysqldb import MySQL
app = Flask("__name__")

app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']="Akhilyuvi143@"
app.config['MYSQL_DB']="data"

mysql = MySQL(app)
CORS(app)

@app.route("/USER_QUALIFIACTION",methods = ['GET','POST'])
def index():
     if request.method=='POST':
        d=request.json
        USER_QUAL_ID=d['USER_QUAL_ID']
        USER_ID=d['USER_ID']
        USER_QUALIFICATION_NAME=d['USER_QUALIFICATION_NAME']
        INSTITUTE_NAME=d['INSTITUTE_NAME']
        PROCUREMENT_YEAR=d['PROCUREMENT_YEAR']
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO USER_QUALIFIACTION(USER_ID,USER_QUALIFICATION_NAME,INSTITUTE_NAME,PROCUREMENT_YEAR) VALUES( %s,%s,%s,%s)",(USER_ID,USER_QUALIFICATION_NAME,INSTITUTE_NAME,PROCUREMENT_YEAR))
        mysql.connection.commit()
        cursor.close()
        return 'success'
     else:
        return 'unsuccess'
        

   

if __name__ == '__main__':
    app.run()
