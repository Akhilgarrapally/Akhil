from flask import Flask,request,jsonify
import pymysql

app = Flask(__name__)


@app.route('/create', methods=['POST','GET'])
def create():
    if request.method == 'GET':
        connection = pymysql.connect(host='sql6.freesqldatabase.com',
                                     user='sql6422581',
                                     password='LjPhFzdixN',
                                     database='sql6422581',
                                     cursorclass=pymysql.cursors.DictCursor)
        with connection:
            with connection.cursor() as cursor:
                # Create a new record
                sql = "CREATE TABLE employees (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, lastname VARCHAR(20), firstname VARCHAR(20))"
                cursor.execute(sql)
                connection.commit()
                return "Success"
@app.route('/insert', methods=['POST','GET'])
def insert():
    if request.method == 'POST':
        details = request.json
        lastname = details['lastname']
        firstname = details['firstname']
        connection = pymysql.connect(host='sql6.freesqldatabase.com',
                                     user='sql6422581',
                                     password='LjPhFzdixN',
                                     database='sql6422581',
                                     cursorclass=pymysql.cursors.DictCursor)
        with connection:
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO employees (lastname, firstname) VALUES (%s, %s)", (lastname, firstname))
                connection.commit()
                return "Success"
@app.route('/fetch', methods=['POST','GET'])
def fetch():
    if request.method == 'GET':
        connection = pymysql.connect(host='sql6.freesqldatabase.com',
                                     user='sql6422581',
                                     password='LjPhFzdixN',
                                     database='sql6422581',
                                     cursorclass=pymysql.cursors.DictCursor)
        with connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM employees")
                fetchdata = cursor.fetchall()
                connection.commit()
                return jsonify(fetchdata)




if __name__ == '__main__':
    app.run()
