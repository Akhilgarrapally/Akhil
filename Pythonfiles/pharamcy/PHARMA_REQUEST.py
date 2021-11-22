from flask import Flask,request,jsonify
from flask_cors import CORS
from flask_mysqldb import MySQL
app = Flask("__name__")

app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']="Akhilyuvi143@"
app.config['MYSQL_DB']="clinicalfirst_pharmacy_dashboard"

mysql = MySQL(app)
CORS(app)

@app.route("/REQUESTS",methods = ['GET','POST'])
def REQUESTS():
     if request.method=='POST':
        d=request.json
        # REQUEST_ID = d['REQUEST_ID']
        PRESCRIPTION_ID = d['PRESCRIPTION_ID']
        REQUEST_STATUS = d['REQUEST_STATUS']
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO REQUESTS(PRESCRIPTION_ID , REQUEST_STATUS) VALUES( %s,%s)",(PRESCRIPTION_ID , REQUEST_STATUS))
        mysql.connection.commit()
        cursor.close()
        return 'success'
     elif request.method == 'GET':
         d = request.json
         cur = mysql.connection.cursor()
         cur.execute("SELECT * FROM REQUESTS")
         fetchdata = cur.fetchall()
         cur.close()
         return jsonify(fetchdata) 
     return 'unsuccess'
    
    
    
    
if __name__ == '__main__':
    app.run()