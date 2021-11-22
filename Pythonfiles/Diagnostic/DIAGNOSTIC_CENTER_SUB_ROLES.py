from flask import Flask,request
from flask_cors import CORS
from flask_mysqldb import MySQL
app = Flask("__name__")

app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']="Akhilyuvi143@"
app.config['MYSQL_DB']="diagnostic_table"

mysql = MySQL(app)
CORS(app)

@app.route("/DIAGNOSTIC_CENTER_SUB_ROLES",methods = ['GET','POST'])
def index():
     if request.method=='POST':
        d=request.json 
        SUB_ROLES_TABLE_ID=d['SUB_ROLES_TABLE_ID']
        USER_ID=d['USER_ID']
        SUB_ROLE_ID=d['SUB_ROLE_ID']
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO DIAGNOSTIC_CENTER_SUB_ROLES(SUB_ROLES_TABLE_ID , USER_ID , SUB_ROLE_ID) VALUES( %s,%s,%s)",
                       (SUB_ROLES_TABLE_ID , USER_ID ,  SUB_ROLE_ID))
        mysql.connection.commit()
        cursor.close()
        return 'success'
     else:
        return 'unsuccess'
        

   

if __name__ == '__main__':
    app.run()















