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

@app.route("/SAMPLE_COLLECTION_LOCATIONS",methods = ['GET','POST'])
def index():
     if request.method=='POST':
        d=request.json 
        SAMPLE_LOC_TABLE_ID=d['SAMPLE_LOC_TABLE_ID']
        LOC_ID=d['LOC_ID']
        LOC_NAME=d['LOC_NAME']
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO SAMPLE_COLLECTION_LOCATIONS(SAMPLE_LOC_TABLE_ID , LOC_ID , LOC_NAME) VALUES( %s,%s,%s)",
                       (SAMPLE_LOC_TABLE_ID , LOC_ID ,  LOC_NAME))
        mysql.connection.commit()
        cursor.close()
        return 'success'
     else:
        return 'unsuccess'
        

   

if __name__ == '__main__':
    app.run()















