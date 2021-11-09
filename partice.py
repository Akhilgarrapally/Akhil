from flask import Flask,request
from flask_mysqldb import MySQL
import CORScanner
app = Flask("__name__")

app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']="Akhilyuvi143@"
app.config['MYSQL_DB']="clg"

mysql = MySQL(app)

@app.route("/",methods = ['GET','POST'])
def index():
     if request.method=='POST':
        d=request.json
        ID=d['ID']
        name=d['name']
        department=d['department']
        CGPA=d['CGPA']
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO college(ID,name,departAkhilyuvi143@ment,CGPA) VALUES( %s,%s,%s,%s)",(ID,name,department,CGPA))
        mysql.connection.commit()
        cursor.close()
        return 'sucess'
     else:
        return 'unsuccess'
        

   

if __name__ == '__main__':
    app.run()
