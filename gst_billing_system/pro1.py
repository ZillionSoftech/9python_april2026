import mysql.connector
connection = mysql.connector.connect(host="localhost",user="root",passwd="kamal",db="classicmodels")
mycursor = connection.cursor()
mycursor.execute("show tables")
result=mycursor.fetchall()

for table in result:
    print(table)