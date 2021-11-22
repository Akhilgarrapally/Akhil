from flask import Flask,request,jsonify
from flask_cors import CORS
from flask_mysqldb import MySQL
app = Flask("__name__")

app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']="Akhilyuvi143@"
app.config['MYSQL_DB']="diagnostic_table"

mysql = MySQL(app)
CORS(app)
  
@app.route("/DIAGNOSIS_SAMPLES",methods = ['GET','POST'])
def DIAGNOSIS_SAMPLES():
     if request.method=='POST':
        d=request.json
        SAMPLE_TABLE_ID=d['SAMPLE_TABLE_ID']
        SAMPLE_ID=d['SAMPLE_ID']
        REQUEST_ID=d['REQUEST_ID']
        COLLECTED_DATETIME=d['COLLECTED_DATETIME']
        SAMPLE_COLLECTED_FROM=d['SAMPLE_COLLECTED_FROM']
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO DIAGNOSIS_SAMPLES(SAMPLE_TABLE_ID , SAMPLE_ID  , REQUEST_ID ,  COLLECTED_DATETIME , SAMPLE_COLLECTED_FROM) VALUES( %s,%s,%s,%s,%s)",
                       (SAMPLE_TABLE_ID , SAMPLE_ID ,  REQUEST_ID ,  COLLECTED_DATETIME , SAMPLE_COLLECTED_FROM))
        mysql.connection.commit()
        cursor.close()
        return 'success'
     elif request.method == 'GET':
         d = request.json
         cur = mysql.connection.cursor()
         cur.execute("SELECT * FROM DIAGNOSIS_SAMPLES")
         fetchdata = cur.fetchall()
         cur.close()
         return jsonify(fetchdata) 
     return 'unsuccess'    
    
@app.route("/DIAGNOSTIC_CENTER",methods = ['GET','POST'])
def DIAGNOSTIC_CENTER():
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
     elif request.method == 'GET':
         d = request.json
         cur = mysql.connection.cursor()
         cur.execute("SELECT * FROM DIAGNOSTIC_CENTER")
         fetchdata = cur.fetchall()
         cur.close()
         return jsonify(fetchdata) 
     return 'unsuccess'

@app.route("/DIAGNOSTIC_CENTER_SUB_ROLES",methods = ['GET','POST'])
def DIAGNOSTIC_CENTER_SUB_ROLES():
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
     elif request.method == 'GET':
         d = request.json
         cur = mysql.connection.cursor()
         cur.execute("SELECT * FROM DIAGNOSTIC_CENTER_SUB_ROLES")
         fetchdata = cur.fetchall()
         cur.close()
         return jsonify(fetchdata) 
     return 'unsuccess'
 
@app.route("/SAMPLE_ASSIGNMENT",methods = ['GET','POST'])
def SAMPLE_ASSIGNMENT():
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
     elif request.method == 'GET':
         d = request.json
         cur = mysql.connection.cursor()
         cur.execute("SELECT * FROM SAMPLE_ASSIGNMENT")
         fetchdata = cur.fetchall()
         cur.close()
         return jsonify(fetchdata) 
     return 'unsuccess'
   
@app.route("/SAMPLE_COLLECTION_LOCATIONS",methods = ['GET','POST'])
def SAMPLE_COLLECTION_LOCATIONS():
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
     elif request.method == 'GET':
         d = request.json
         cur = mysql.connection.cursor()
         cur.execute("SELECT * FROM SAMPLE_COLLECTION_LOCATIONS")
         fetchdata = cur.fetchall()
         cur.close()
         return jsonify(fetchdata) 
     return 'unsuccess'
 
@app.route("/SAMPLE_TESTS",methods = ['GET','POST'])
def SAMPLE_TESTS():
     if request.method=='POST':
        d=request.json
        SAMPLE_TESTS_TABLE_ID=d['SAMPLE_TESTS_TABLE_ID']
        SAMPLE_ID=d['SAMPLE_ID']
        TEST_ID=d['TEST_ID']
        TESTING_DATETIME=d['TESTING_DATETIME']
        TEST_DIAGNISED=d['TEST_DIAGNISED']
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO SAMPLE_TESTS(SAMPLE_TESTS_TABLE_ID , SAMPLE_ID  , TEST_ID ,  TESTING_DATETIME , TEST_DIAGNISED) VALUES( %s,%s,%s,%s,%s)",
                       (SAMPLE_TESTS_TABLE_ID , SAMPLE_ID ,  TEST_ID ,  TESTING_DATETIME , TEST_DIAGNISED))
        mysql.connection.commit()
        cursor.close()
        return 'success'
     elif request.method == 'GET':
         d = request.json
         cur = mysql.connection.cursor()
         cur.execute("SELECT * FROM SAMPLE_TESTS")
         fetchdata = cur.fetchall()
         cur.close()
         return jsonify(fetchdata) 
     return 'unsuccess'
 
@app.route("/TEST_PRICING",methods = ['GET','POST'])
def TEST_PRICING():
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
     elif request.method == 'GET':
         d = request.json
         cur = mysql.connection.cursor()
         cur.execute("SELECT * FROM TEST_PRICING")
         fetchdata = cur.fetchall()
         cur.close()
         return jsonify(fetchdata) 
     return 'unsuccess'
 
@app.route("/TEST_REQUESTS",methods = ['GET','POST'])
def TEST_REQUESTS():
     if request.method=='POST':
        d=request.json
        REQUEST_TABLE_ID=d['REQUEST_TABLE_ID']
        REQUEST_ID=d['REQUEST_ID']
        DOCTOR_NAME=d['DOCTOR_NAME']
        USER_ID=d['USER_ID']
        PATIENT_ID=d['PATIENT_ID']
        REQUEST_DATETIME=d['REQUEST_DATETIME']
        REQUEST_STATUS=d['REQUEST_STATUS']
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO TEST_REQUESTS(REQUEST_TABLE_ID , REQUEST_ID , DOCTOR_NAME , USER_ID , PATIENT_ID , REQUEST_DATETIME , REQUEST_STATUS) VALUES( %s,%s,%s,%s,%s,%s,%s)",
                       (REQUEST_TABLE_ID , REQUEST_ID , DOCTOR_NAME , USER_ID , PATIENT_ID , REQUEST_DATETIME , REQUEST_STATUS))
        mysql.connection.commit()
        cursor.close()
        return 'success'
     elif request.method == 'GET':
         d = request.json
         cur = mysql.connection.cursor()
         cur.execute("SELECT * FROM TEST_REQUESTS")
         fetchdata = cur.fetchall()
         cur.close()
         return jsonify(fetchdata) 
     return 'unsuccess'


if __name__ == '__main__':
    app.run()
