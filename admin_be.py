import mysql.connector
import admin
import datetime
import admin as ad
from tkinter import *

#these functions are linked to the admin file
#connect to database
mydb= mysql.connector.connect(user="tamsynsteed", password="@Lifechoices314", database="lifechoicesonline", host="127.0.0.1", auth_plugin="mysql_native_password")

mycursor=mydb.cursor()

#show the date
current_date = datetime.datetime.now()

#create a table in a datase if it does not exist
def studentData():
   mydb= mysql.connector.connect(user="tamsynsteed", password="@Lifechoices314", database="lifechoicesonline", host="127.0.0.1", auth_plugin="mysql_native_password")

   mycursor=mydb.cursor()

   exe = "CREATE TABLE IF NOT EXISTS  users VALUES(ID int(35) NOT NULL AUTO_INCREMENT, full_name varchar(60) default null, user_name varchar(50) default null, password varchar(20) default null, mobile_number int(10) default null, status varchar(30) default not null, date_joined date, PRIMARY KEY(ID))"
   mycursor.execute(exe)
   mydb.commit()


fullname= ad.fullname1.get()
username1= ad.username.get()
password1= ad.password.get()
status1= ad.tkvar.get()
mobile1 =ad.mobile.get()


#allows users to eb added into the datase via the admin portal
def addRec(full_name, user_name, password, mobile_number, status):
    mydb= mysql.connector.connect(user="tamsynsteed", password="@Lifechoices314", database="lifechoicesonline", host="127.0.0.1", auth_plugin="mysql_native_password")

    mycursor=mydb.cursor()

    sql = "INSERT INTO users (full_name, user_name, password, mobile_number, status, date_joined) VALUES (%s, %s, %s, %s,%s,%s)"
    val = (fullname, username1,password1,mobile1,str(status1),current_date)

    mycursor.execute(sql, val)

    mydb.commit()


#view data in tables
def viewData():
    con = con = mysql.connector.connect(host="localhost", user="tamsynsteed", passwd="@Lifechoices314")
    cur = con.cursor()
    cur.execute("use lifechoicesonline")
    cur.execute("select * from users")
    row = cur.fetchall()
    con.close()
    return row
#delete record
def deleteRec(id):
    con = con = mysql.connector.connect(host="localhost", user="tamsynsteed", passwd="@Lifechoices314")
    cur = con.cursor()
    cur.execute("use lifechoicesonline")
    cur.execute("DELETE FROM users WHERE ID=%s", (id,))
    con.commit()
    con.close()











