from flask import Flask,request,jsonify
from flask_cors import CORS
from flask_mysqldb import MySQL
app = Flask("__name__")

app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']="Akhil"
app.config['MYSQL_DB']="data"

mysql = MySQL(app)
CORS(app)

@app.route("/USER_SIGNUP",methods = ['GET','POST'])
def user_signup():
     if request.method=='POST':
        d=request.json
        USER_SIGNUP_ID=d['USER_SIGNUP_ID']
        USER_ID = d['USER_ID']
        USER_NAME = d['USER_NAME']
        USER_MAIL_ID=d['USER_MAIL_ID']
        USER_PHONE_NUMBER=d['USER_PHONE_NUMBER']
        USER_PASSWORD=d['USER_PASSWORD']
        USER_IP=d['USER_IP']
        USER_DATE_CREATED=d['USER_DATE_CREATED']
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO USER_SIGNUP(USER_SIGNUP_ID,USER_ID,USER_NAME,USER_MAIL_ID,USER_PHONE_NUMBER,USER_PASSWORD,USER_IP,USER_DATE_CREATED) VALUES( %s,%s,%s,%s,%s,%s,%s,%s)",(USER_SIGNUP_ID,USER_ID,USER_NAME,USER_MAIL_ID,USER_PHONE_NUMBER,USER_PASSWORD,USER_IP,USER_DATE_CREATED))
        mysql.connection.commit()
        cursor.close()
        return 'success'
     elif request.method == 'GET':
         d = request.json
         cur = mysql.connection.cursor()
         cur.execute("SELECT * FROM USER_SIGNUP")
         fetchdata = cur.fetchall()
         cur.close()
         return jsonify(fetchdata) 
     return 'unsuccess'
        
@app.route("/USER_REGISTRATION",methods = ['GET','POST'])
def user_registration():
     if request.method=='POST':
        d=request.json
        USER_REG_ID=d['USER_REG_ID']
        USER_ID=d['USER_ID']
        USER_AGE=d['USER_AGE']
        USER_EXPERIANCE=d['USER_EXPERIANCE']
        USER_GENDER=d['USER_GENDER']
        USER_LICENSE_NUMBER=d['USER_LICENSE_NUMBER']
        FLAT_NO=d['FLAT_NO']
        STREET_NAME=d['STREET_NAME']
        CITY_NAME=d['CITY_NAME'] 
        STATE_NAME=d['STATE_NAME']
        COUNTRY_NAME=d['COUNTRY_NAME']
        ZIP_CODE=d['ZIP_CODE']
        USER_APPROVED=d['USER_APPROVED']
        USER_IP=d['USER_IP']
        USER_DATE_REGISTERED=d['USER_DATE_REGISTERED']
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO USER_REGISTRATION(USER_REG_ID,USER_ID,USER_AGE,USER_EXPERIANCE,USER_GENDER,USER_LICENSE_NUMBER,FLAT_NO,STREET_NAME,CITY_NAME,STATE_NAME,COUNTRY_NAME,ZIP_CODE,USER_APPROVED,USER_IP,USER_DATE_REGISTERED) VALUES( %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(USER_REG_ID,USER_ID,USER_AGE,USER_EXPERIANCE,USER_GENDER,USER_LICENSE_NUMBER,FLAT_NO,STREET_NAME,CITY_NAME,STATE_NAME,COUNTRY_NAME,ZIP_CODE,USER_APPROVED,USER_IP,USER_DATE_REGISTERED))
        mysql.connection.commit()
        cursor.close()
        return 'success'
     elif request.method == 'GET':
         d = request.json
         cur = mysql.connection.cursor()
         cur.execute("SELECT * FROM USER_REGISTRATION")
         fetchdata = cur.fetchall()
         cur.close()
         return jsonify(fetchdata) 
     return 'unsuccess'
 
@app.route("/USER_QUALIFIACTION",methods = ['GET','POST'])
def user_qualification():
     if request.method=='POST':
        d=request.json
        USER_QUAL_ID=d['USER_QUAL_ID']
        USER_ID=d['USER_ID']
        USER_QUALIFICATION_NAME=d['USER_QUALIFICATION_NAME']
        INSTITUTE_NAME=d['INSTITUTE_NAME']
        PROCUREMENT_YEAR=d['PROCUREMENT_YEAR']
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO USER_QUALIFIACTION(USER_ID,USER_QUALIFICATION_NAME,INSTITUTE_NAME,PROCUREMENT_YEAR) VALUES( %s,%s,%s,%s)",(USER_ID,USER_QUALIFICATION_NAME,INSTITUTE_NAME,PROCUREMENT_YEAR))
        mysql.connection.commit()
        cursor.close()
        return 'success'
     elif request.method == 'GET':
         d = request.json
         cur = mysql.connection.cursor()
         cur.execute("SELECT * FROM USER_QUALIFIACTION")
         fetchdata = cur.fetchall()
         cur.close()
         return jsonify(fetchdata) 
     return 'unsuccess'
@app.route("/USER_HOSPITAL",methods = ['GET','POST'])
def user_hospital():
     if request.method=='POST':
        d=request.json
        USER_HOSPITAL_ID=d['USER_HOSPITAL_ID']
        USER_ID=d['USER_ID']
        HOSPITAL_NAME = d['HOSPITAL_NAME']
        HOSPITAL_ADDRESS=d['HOSPITAL_ADDRESS']
        HOSPITAL_CITY = d['HOSPITAL_CITY']
        HOSPPITAL_STATE = d['HOSPPITAL_STATE']
        HOSPITAL_ZIP_CODE = d['HOSPITAL_ZIP_CODE']
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO USER_HOSPITAL(USER_HOSPITAL_ID,USER_ID,HOSPITAL_NAME,HOSPITAL_ADDRESS,HOSPITAL_CITY,HOSPPITAL_STATE,HOSPITAL_ZIP_CODE) VALUES( %s,%s,%s,%s,%s,%s,%s)",(USER_HOSPITAL_ID,USER_ID,HOSPITAL_NAME,HOSPITAL_ADDRESS,HOSPITAL_CITY,HOSPPITAL_STATE,HOSPITAL_ZIP_CODE))
        mysql.connection.commit()
        cursor.close()
        return 'success'
     elif request.method == 'GET':
         d = request.json
         cur = mysql.connection.cursor()
         cur.execute("SELECT * FROM USER_HOSPITAL")
         fetchdata = cur.fetchall()
         cur.close()
         return jsonify(fetchdata) 
     return 'unsuccess'
    
@app.route("/USER_SPECIALIZATION",methods = ['GET','POST'])
def user_specialzation():
     if request.method=='POST':
        d=request.json
        USER_SPECIALIZATION_ID=d['USER_SPECIALIZATION_ID']
        USER_ID=d['USER_ID']
        SPECIALIZATION_NAME=d['SPECIALIZATION_NAME']
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO USER_SPECIALIZATION(USER_SPECIALIZATION_ID,USER_ID,SPECIALIZATION_NAME) VALUES( %s,%s,%s)",(USER_SPECIALIZATION_ID,USER_ID,SPECIALIZATION_NAME))
        mysql.connection.commit()
        cursor.close()
        return 'success'
     elif request.method == 'GET':
         d = request.json
         cur = mysql.connection.cursor()
         cur.execute("SELECT * FROM USER_SPECIALIZATION")
         fetchdata = cur.fetchall()
         cur.close()
         return jsonify(fetchdata) 
     return 'unsuccess'
    
@app.route("/USER_DEPARTMENT",methods = ['GET','POST'])
def user_department():
     if request.method=='POST':
        d=request.json
        ID=d['ID']
        USER_ID=d['USER_ID']
        DEPT_ID=d['DEPT_ID']
        DEPT_NAME=d['DEPT_NAME']
        DEPT_HEAD=d['DEPT_HEAD']
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO USER_DEPARTMENT(ID,USER_ID,DEPT_ID,DEPT_NAME,DEPT_HEAD) VALUES( %s,%s,%s,%s,%s)",(ID,USER_ID,DEPT_ID,DEPT_NAME,DEPT_HEAD))
        mysql.connection.commit()
        cursor.close()
        return 'success'
     elif request.method == 'GET':
         d = request.json
         cur = mysql.connection.cursor()
         cur.execute("SELECT * FROM USER_DEPARTMENT")
         fetchdata = cur.fetchall()
         cur.close()
         return jsonify(fetchdata) 
     return 'unsuccess'
    
@app.route("/patient_personal",methods = ['GET','POST'])
def patient_personal():
     if request.method=='POST':
        d=request.json
        PATIENT_ID=d['PATIENT_ID']
        PATIENT_NAME = d['PATIENT_NAME']
        PHONE_NUMBER = d['PHONE_NUMBER']
        MAIL_ID = d['MAIL_ID']
        FLAT_NO = d['FLAT_NO']
        STREET_NAME = d['STREET_NAME']
        CITY_NAME = d['CITY_NAME']
        STATE_NAME = d['STATE_NAME']
        COUNTRY_NAME = d['COUNTRY_NAME']
        ZIP_CODE = d['ZIP_CODE']
        DATE_OF_BIRTH = d['DATE_OF_BIRTH']
        CREATED_BY = d['CREATED_BY']
        IP_ADDRESS=d['IP_ADDRESS']
        CREATED_DATE = d['CREATED_DATE']

        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO PATIENT_PERSONAL(PATIENT_ID,PATIENT_NAME,PHONE_NUMBER,MAIL_ID,FLAT_NO,STREET_NAME,CITY_NAME,STATE_NAME,COUNTRY_NAME,ZIP_CODE,DATE_OF_BIRTH,CREATED_BY,IP_ADDRESS,CREATED_DATE) VALUES( %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(PATIENT_ID,PATIENT_NAME,PHONE_NUMBER,MAIL_ID,FLAT_NO,STREET_NAME,CITY_NAME,STATE_NAME,COUNTRY_NAME,ZIP_CODE,DATE_OF_BIRTH,CREATED_BY,IP_ADDRESS,CREATED_DATE))
        mysql.connection.commit()
        cursor.close()
        return 'success'
     elif request.method == 'GET':
         d = request.json
         cur = mysql.connection.cursor()
         cur.execute("SELECT * FROM PATIENT_PERSONAL")
         fetchdata = cur.fetchall()
         cur.close()
         return jsonify(fetchdata) 
     return 'unsuccess'
   
@app.route("/PATIENT_HEALTH",methods = ['GET','POST'])
def patinet_health():
     if request.method=='POST':
        d=request.json
        PATIENT_HEALTH_ID=d['PATIENT_HEALTH_ID']
        PATIENT_ID=d['PATIENT_ID']
        BLOOD_GROUP=d['BLOOD_GROUP']                
        PATIENT_AGE=d['PATIENT_AGE']
        PATIENT_WEIGHT=d['PATIENT_WEIGHT']
        PATIENT_HEIGHT=d['PATIENT_HEIGHT'] 
        PATIENT_SYSTOLIC_BP=d['PATIENT_SYSTOLIC_BP']
        PATIENT_DYASTOLIC_BP=d['PATIENT_DYASTOLIC_BP']
        PATIENT_TEMPARATURE=d['PATIENT_TEMPARATURE']
        CREATED_BY=d['CREATED_BY']
        IP_ADDRESS=d['IP_ADDRESS']
        CREATED_DATE=d['CREATED_DATE']
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO PATIENT_HEALTH(PATIENT_HEALTH_ID,PATIENT_ID,BLOOD_GROUP,PATIENT_AGE,PATIENT_WEIGHT,PATIENT_HEIGHT,PATIENT_SYSTOLIC_BP,PATIENT_DYASTOLIC_BP,PATIENT_TEMPARATURE,CREATED_BY,IP_ADDRESS,CREATED_DATE) VALUES( %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(PATIENT_HEALTH_ID,PATIENT_ID,BLOOD_GROUP,PATIENT_AGE,PATIENT_WEIGHT,PATIENT_HEIGHT,PATIENT_SYSTOLIC_BP,PATIENT_DYASTOLIC_BP,PATIENT_TEMPARATURE,CREATED_BY,IP_ADDRESS,CREATED_DATE))
        mysql.connection.commit()
        cursor.close()
        return 'success'
     elif request.method == 'GET':
         d = request.json
         cur = mysql.connection.cursor()
         cur.execute("SELECT * FROM PATIENT_HEALTH")
         fetchdata = cur.fetchall()
         cur.close()
         return jsonify(fetchdata) 
     return 'unsuccess'


@app.route("/TESTS",methods = ['GET','POST'])
def tests():
     if request.method=='POST':
        d=request.json
        SESSION_ID=d['SESSION_ID']
        TEST_ID=d['TEST_ID']
        TEST_NAME=d['TEST_NAME']
        DISEASE_NAME=d['DISEASE_NAME']
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO TESTS(SESSION_ID , TEST_ID , TEST_NAME , DISEASE_NAME) VALUES( %s,%s,%s,%s)",(SESSION_ID , TEST_ID , TEST_NAME , DISEASE_NAME))
        mysql.connection.commit()
        cursor.close()
        return 'success'
     elif request.method == 'GET':
         d = request.json
         cur = mysql.connection.cursor()
         cur.execute("SELECT * FROM TESTS")
         fetchdata = cur.fetchall()
         cur.close()
         return jsonify(fetchdata) 
     return 'unsuccess'

@app.route("/TEST_RESULT",methods = ['GET','POST'])
def test_result():
     if request.method=='POST':
        d=request.json
        SESSION_ID=d['SESSION_ID']
        TEST_ID=d['TEST_ID']
        TEST_RESULT=d['TEST_RESULT']
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO TEST_RESULT(SESSION_ID , TEST_ID , TEST_RESULT ) VALUES( %s,%s,%s)",(SESSION_ID , TEST_ID , TEST_RESULT))
        mysql.connection.commit()
        cursor.close()
        return 'success'
     elif request.method == 'GET':
         d = request.json
         cur = mysql.connection.cursor()
         cur.execute("SELECT * FROM TEST_RESULT")
         fetchdata = cur.fetchall()
         cur.close()
         return jsonify(fetchdata) 
     return 'unsuccess'

@app.route("/SYMPTOM",methods = ['GET','POST'])
def symptom():
     if request.method=='POST':
        d=request.json
        SESSION_ID=d['SESSION_ID']
        SYMPTOM_ID=d['SYMPTOM_ID']
        SYMPTOM_NAME=d['SYMPTOM_NAME']
        INPUT=d['INPUT']
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO SYMPTOM(SESSION_ID , SYMPTOM_ID , SYMPTOM_NAME , INPUT) VALUES( %s,%s,%s,%s)",(SESSION_ID , SYMPTOM_ID , SYMPTOM_NAME , INPUT))
        mysql.connection.commit()
        cursor.close()
        return 'success'
     elif request.method == 'GET':
         d = request.json
         cur = mysql.connection.cursor()
         cur.execute("SELECT * FROM SYMPTOM")
         fetchdata = cur.fetchall()
         cur.close()
         return jsonify(fetchdata) 
     return 'unsuccess'

@app.route("/SESSION",methods = ['GET','POST'])
def session():
     if request.method=='POST':
        d=request.json
        ID=d['ID']
        SESSION_ID=d['SESSION_ID']
        USER_ID=d['USER_ID']
        PATIENT=d['PATIENT']
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO SESSION(ID ,SESSION_ID , USER_ID , PATIENT) VALUES( %s,%s,%s,%s)",(ID , SESSION_ID , USER_ID , PATIENT))
        mysql.connection.commit()
        cursor.close()
        return 'success'
     elif request.method == 'GET':
         d = request.json
         cur = mysql.connection.cursor()
         cur.execute("SELECT * FROM SESSION")
         fetchdata = cur.fetchall()
         cur.close()
         return jsonify(fetchdata) 
     return 'unsuccess'

@app.route("/CAUSE",methods = ['GET','POST'])
def cause():
     if request.method=='POST':
        d=request.json
        SESSION_ID=d['SESSION_ID']
        CAUSE_ID=d['CAUSE_ID']
        CAUSE_NAME=d['CAUSE_NAME']
        INPUT=d['INPUT']
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO CAUSE(SESSION_ID , CAUSE_ID , CAUSE_NAME , INPUT) VALUES( %s,%s,%s,%s)",(SESSION_ID , CAUSE_ID , CAUSE_NAME , INPUT))
        mysql.connection.commit()
        cursor.close()
        return 'success'
     elif request.method == 'GET':
         d = request.json
         cur = mysql.connection.cursor()
         cur.execute("SELECT * FROM CAUSE")
         fetchdata = cur.fetchall()
         cur.close()
         return jsonify(fetchdata) 
     return 'unsuccess'

@app.route("/LOGS",methods = ['GET','POST'])
def logs():
     if request.method=='POST':
        d=request.json
        LOG_ID=d['LOG_ID']
        LOGIN_EMAIL_ID=d['LOGIN_EMAIL_ID']
        LOGIN_TIME=d['LOGIN_TIME']
        LOGOUT_TIME=d['LOGOUT_TIME']
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO LOGS(LOG_ID,LOGIN_EMAIL_ID,LOGIN_TIME,LOGOUT_TIME) VALUES( %s,%s,%s,%s)",(LOG_ID,LOGIN_EMAIL_ID,LOGIN_TIME,LOGOUT_TIME))
        mysql.connection.commit()
        cursor.close()
        return 'success'
     elif request.method == 'GET':
         d = request.json
         cur = mysql.connection.cursor()
         cur.execute("SELECT * FROM LOGS")
         fetchdata = cur.fetchall()
         cur.close()
         return jsonify(fetchdata) 
     return 'unsuccess'
 
@app.route("/API_LOGS",methods = ['GET','POST'])
def api_log():
     if request.method=='POST':
        d=request.json
        API_ID=d['API_ID']
        API_NAME=d['API_NAME']
        ERROR_CODE=d['ERROR_CODE']
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO API_LOGS(API_ID,API_NAME,ERROR_CODE) VALUES( %s,%s,%s)",(API_ID,API_NAME,ERROR_CODE))
        mysql.connection.commit()
        cursor.close()
        return 'success'
     elif request.method == 'GET':
         d = request.json
         cur = mysql.connection.cursor()
         cur.execute("SELECT * FROM API_LOGS")
         fetchdata = cur.fetchall()
         cur.close()
         return jsonify(fetchdata) 
     return 'unsuccess'
     



   
if __name__ == '__main__':
    app.run()