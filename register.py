from tkinter import *
import mysql.connector
import tkinter as tk
from tkinter import messagebox
import datetime

root = tk.Tk()

root.title("Registration")
root.geometry("500x500")
root.configure(background="black")



mydb= mysql.connector.connect(user="tamsynsteed", password="@Lifechoices314", database="lifechoicesonline", host="127.0.0.1", auth_plugin="mysql_native_password")
#connect database
mycursor=mydb.cursor()

x = datetime.datetime.now()

#this function allows a new user to register , data is inserted into the users table
def insert():

    fullname= fullname1.get()
    username1= username.get()
    password1= password.get()
    status1= tkvar.get()
    mobile1 =mobile.get()
    
    sql = "INSERT INTO users (full_name, user_name, password, mobile_number, status, date_joined) VALUES (%s, %s, %s, %s,%s,%s)"
    val = (fullname, username1,password1,mobile1,str(status1),x)

    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")
    messagebox.showinfo("Registration Complete","Please log in.")
    root.withdraw()
    import loginpage

def back():
    root.withdraw()
    import loginpage


lbluser=tk.Label(root, text="Welcome to LIfe Choices Online", bg="cadet blue", font="22")
lbluser.pack(pady=20)

lbluser=tk.Label(root, text="Please complete the form below.", bg="white", font="20")
lbluser.pack()

lbluser=tk.Label(root, text="Enter Fullname")
lbluser.place(x=50, y=120)

fullname1= tk.Entry(root, width=30)
fullname1.place(x=165,y=120)

lblpasswd=tk.Label(root,text="Enter Username")
lblpasswd.place(x=50, y=160)

username = tk.Entry(root,width=30)
username.place(x=165, y=160)

lblpasswd=tk.Label(root,text="Enter Password")
lblpasswd.place(x=50, y=200)

password = tk.Entry(root,width=30)
password.place(x=165, y=200)

lblmobile=tk.Label(root,text="Mobile Number")
lblmobile.place(x=50, y=240)

mobile = tk.Entry(root,width=30)
mobile.place(x=165, y=240)

lblstatus =Label(root, text="I am registering as a:")
lblstatus.pack(pady=200)

#dropdown
# Create a Tkinter variable
tkvar = StringVar(root)

# Dictionary with options
choices = {'Visitor','Student','Employee'}
tkvar.set('Student') # set the default option

popupMenu = OptionMenu(root, tkvar, *choices)
popupMenu.place(x=205, y=320)

logbuttn=tk.Button(root,text="Submit", command=insert)
logbuttn.place(x=215, y=420)

logbuttn=tk.Button(root,text="Back to login", command=back)
logbuttn.place(x=195, y=460)














root.mainloop()
