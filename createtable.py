import mysql.connector

mydb= mysql.connector.connect(user="tamsynsteed", password="@Lifechoices314", database="hospital", host="127.0.0.1", auth_plugin="mysql_native_password")
#connect database

mycursor=mydb.cursor()

mycursor.execute("CREATE TABLE Admin (username VARCHAR(255), password VARCHAR(255))")
