import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root",passwd="Goutham@1005", database="user_database")
mycursor = mydb.cursor()

mycursor.execute("select * from user_details;")

for i in mycursor:
    print(i)
                