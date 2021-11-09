import mysql.connector as a
db = a.connect(host="localhost",user="root",password="Akhilyuvi143@",database="flask_signup")
print(db)
cursor = db.cursor()
cursor.execute("SHOW DATABASES")
databases = cursor.fetchall()
print(databases)
for database in databases:
    print(database)

cursor.execute("SHOW TABLES")
tables= cursor.fetchall()
for table in tables:
    print(table)

cursor.execute("DESC login")
print(cursor.fetchall())

query = "INSERT INTO login (name,email)VALUES(%s,%s)"
values = ("Akhil","Akhil@gmail.com")
          
cursor.execute(query,values)
db.commit()
print(cursor.rowcount,"rows inserted")

query="SELECT * FROM login"
cursor.execute(query)
records = cursor.fetchall()
for record in records:
    print(record)
    
query="SELECT name FROM login"
cursor.execute(query)
names=cursor.fetchall()
for name in names:
    print(name)

query="SELECT * FROM login WHERE name='Akhil'"
cursor.execute(query)
names=cursor.fetchall()
for name in names:
    print(name)
    
query="INSERT INTO login (name,email)VALUES(%s,%s)"
values = [
       ("Anil","Anil@gmail.com"),
          ("Jayanath","Jaynath@gmail.com"),
          ("Bharath","Bharath@gmail.com"),
          ("Mallikarjun","Mallikarjun@gmail.com")
          ]
cursor.executemany(query,values)
db.commit()
print(cursor.rowcount,"rows inserted")

query="SELECT * FROM login"
cursor.execute(query)
records = cursor.fetchall()
for record in records:
    print(record)