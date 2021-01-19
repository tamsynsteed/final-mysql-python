import mysql.connector

mydb= mysql.connector.connect(user="tamsyn", password="@Tammy1234", database="hospital", host="127.0.0.1", auth_plugin="mysql_native_password")
#connect database

mycursor=mydb.cursor()


mycursor.execute("SELECT * FROM Login")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
