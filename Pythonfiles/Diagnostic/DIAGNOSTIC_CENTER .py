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

@app.route("/DIAGNOSTIC_CENTER",methods = ['GET','POST'])
def index():
     if request.method=='POST':
        d=request.json 
        DIAGNOSTIC_TABLE_ID = d['DIAGNOSTIC_TABLE_ID']
        DIAGNOSTIC_ID = d['DIAGNOSTIC_ID']
        DIAGNOSTIC_CENTER_NAME = d['DIAGNOSTIC_CENTER_NAME']
        FLAT_NO = d['FLAT_NO']
        STREET_NAME = d['STREET_NAME']
        CITY_NAME = d['CITY_NAME']
        STATE_NAME = d['STATE_NAME']
        COUNTRY_NAME = d['COUNTRY_NAME']
        ZIP_CODE = d['ZIP_CODE']
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO DIAGNOSTIC_CENTER(DIAGNOSTIC_TABLE_ID , DIAGNOSTIC_ID , DIAGNOSTIC_CENTER_NAME , FLAT_NO , STREET_NAME , CITY_NAME , STATE_NAME , COUNTRY_NAME , ZIP_CODE) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                       (DIAGNOSTIC_TABLE_ID , DIAGNOSTIC_ID ,  DIAGNOSTIC_CENTER_NAME , FLAT_NO , STREET_NAME , CITY_NAME , STATE_NAME , COUNTRY_NAME , ZIP_CODE))
        mysql.connection.commit()
        cursor.close()
        return 'success'
     else:
        return 'unsuccess'
        

   

if __name__ == '__main__':
    app.run()















