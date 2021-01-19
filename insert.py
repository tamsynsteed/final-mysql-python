import mysql.connector

mydb= mysql.connector.connect(user="tamsynsteed", password="@Lifechoices314", database="lifechoicesonline", host="127.0.0.1", auth_plugin="mysql_native_password")
#connect database

mycursor=mydb.cursor()

sql = "INSERT INTO admin (full_name, user_name, password, status) VALUES (%s, %s, %s, %s)"
val = ("tamsynsteed","tamsynsteed","12345", "admin")

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
