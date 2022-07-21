import mysql.connector as con
mydb = con.connect(host="localhost",user="root",passwd="anuj",database="anuj")
cursor = mydb.cursor()
a="show databases"
cursor.execute(a)
cursor.fetchall()
s= "show tables"
cursor.execute(s)
for i in cursor.fetchall():
    print(i)