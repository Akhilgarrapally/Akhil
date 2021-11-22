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

@app.route("/SAMPLE_ASSIGNMENT",methods = ['GET','POST'])
def index():
     if request.method=='POST':
        d=request.json 
        SAMPLE_ASSIGN_TABLE_ID=d['SAMPLE_ASSIGN_TABLE_ID']
        SAMPLE_ID=d['SAMPLE_ID']
        SAMPLE_ASSIGNEE=d['SAMPLE_ASSIGNEE']
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO SAMPLE_ASSIGNMENT(SAMPLE_ASSIGN_TABLE_ID , SAMPLE_ID , SAMPLE_ASSIGNEE) VALUES( %s,%s,%s)",
                       (SAMPLE_ASSIGN_TABLE_ID , SAMPLE_ID ,  SAMPLE_ASSIGNEE))
        mysql.connection.commit()
        cursor.close()
        return 'success'
     else:
        return 'unsuccess'
        

   

if __name__ == '__main__':
    app.run()















