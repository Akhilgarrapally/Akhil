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

@app.route("/PHARMA_MEDICINE_STOCK",methods = ['GET','POST'])
def PHARMA_MEDICINE_STOCK():
     if request.method=='POST':
        d=request.json
        MEDICINE_ID = d['MEDICINE_ID']
        MEDICINE_NAME = d['MEDICINE_NAME']
        PHARMA_ID = d['PHARMA_ID']
        MEDICINE_STOCK_AVAILABILITY = d['MEDICINE_STOCK_AVAILABILITY']
        MEDICINE_MRP = d['MEDICINE_MRP']
        MEDICINE_DISCOUNT = d['MEDICINE_DISCOUNT']
        MEDICINE_FINAL_PRICE = d['MEDICINE_FINAL_PRICE']
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO PHARMA_MEDICINE_STOCK(MEDICINE_ID,MEDICINE_NAME ,PHARMA_ID,MEDICINE_STOCK_AVAILABILITY,MEDICINE_MRP,MEDICINE_DISCOUNT,MEDICINE_FINAL_PRICE) VALUES( %s,%s,%s,%s,%s,%s,%s)",(MEDICINE_ID,MEDICINE_NAME ,PHARMA_ID,MEDICINE_STOCK_AVAILABILITY,MEDICINE_MRP,MEDICINE_DISCOUNT,MEDICINE_FINAL_PRICE))
        mysql.connection.commit()
        cursor.close()
        return 'success'
     elif request.method == 'GET':
         d = request.json
         cur = mysql.connection.cursor()
         cur.execute("SELECT * FROM PHARMA_MEDICINE_STOCK")
         fetchdata = cur.fetchall()
         cur.close()
         return jsonify(fetchdata) 
     return 'unsuccess'
    
    
    
    
if __name__ == '__main__':
    app.run()