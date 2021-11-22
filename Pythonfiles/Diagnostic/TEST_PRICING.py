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

@app.route("/TEST_PRICING",methods = ['GET','POST'])
def index():
     if request.method=='POST':
        d=request.json
        TEST_PRICING_TABLE_ID=d['TEST_PRICING_TABLE_ID']
        TEST_ID=d['TEST_ID']
        TEST_PRICE=d['TEST_PRICE']
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO TEST_PRICING(TEST_PRICING_TABLE_ID, TEST_ID, TEST_PRICE) VALUES( %s,%s,%s)",
                       (TEST_PRICING_TABLE_ID, TEST_ID, TEST_PRICE))
        mysql.connection.commit()
        cursor.close()
        return 'success'
     else:
        return 'unsuccess'
        

   

if __name__ == '__main__':
    app.run()
