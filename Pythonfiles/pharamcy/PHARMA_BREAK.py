from flask import Flask,request,jsonify
from flask_cors import CORS
from flask_mysqldb import MySQL
app = Flask("__name__")

app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']="Akhil"
app.config['MYSQL_DB']="pharma"

mysql = MySQL(app)
CORS(app)

@app.route("/LUNCH_BREAK",methods = ['GET','POST'])
def LUNCH_BREAK():
     if request.method=='POST':
        d=request.json
        Everyday = d['Everyday']
        monday = d['monday']
        tuesday = d['tuesday']
        wednsday = d['wednsday']
        thursday = d['thursday']
        friday = d['friday']
        
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO LUNCH_BREAK(Everyday,monday ,tuesday,wednsday,thursday,friday) VALUES( %s,%s,%s,%s,%s,%s)",(Everyday,monday ,tuesday,wednsday,thursday,friday))
        mysql.connection.commit()
        cursor.close()
        return 'success'
     elif request.method == 'GET':
         d = request.json
         cur = mysql.connection.cursor()
         cur.execute("SELECT * FROM LUNCH_BREAK")
         fetchdata = cur.fetchall()
         cur.close()
         return jsonify(fetchdata) 
     return 'unsuccess'
    
    
    
    
if __name__ == '__main__':
    app.run()