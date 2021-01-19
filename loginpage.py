from tkinter import *
import mysql.connector
import tkinter as tk
from tkinter import messagebox
import time

time1 = ''

root = tk.Tk()

mydb= mysql.connector.connect(user="tamsynsteed", password="@Lifechoices314", database="", host="127.0.0.1", auth_plugin="mysql_native_password")
#connect database

mycursor=mydb.cursor()

#create function thats pulls all data from Login table in the hospital database
def verify():
    user_verification= Username.get()
    pass_verification = password.get()
    sql = "select * from users where username = %s and password = %s"
    mycursor.execute(sql,[(user_verification), (pass_verification)])
    results = mycursor.fetchall()
    if results:
        for i in results:
            logged()
            break
    else:
            failed()

def logged():
    messagebox.showinfo("Login successful", "Verified!")


def failed():
    messagebox.showerror("Login failed", "Please check your username and password.")


root.title('Login Page')

root.geometry("450x450")
root.configure(background="black")

lbluser=tk.Label(root, text="Life Choices Online: Log in", bg="cadet blue")
lbluser.pack(pady=10)


lbluser=tk.Label(root, text="Enter Username")
lbluser.place(x=50, y=100)

Username= tk.Entry(root, width=30)
Username.place(x=165,y=100)

lblpasswd=tk.Label(root,text="Enter Password")
lblpasswd.place(x=50, y=140)

password = tk.Entry(root,width=30)
password.place(x=165, y=140)

logbuttn=tk.Button(root,text="Login", command=verify)
logbuttn.place(x=145,y=200)

regbuttn=tk.Button(root,text="Register")
regbuttn.place(x=220,y=200)


import time

time1 = ''
clock = Label(root, font=('times', 18, 'bold'), )
clock.pack(pady=10)

def tick():
    global time1
    # get the current local time from the PC
    time2 = time.strftime('%H:%M:%S')
    # if time string has changed, update it
    if time2 != time1:
        time1 = time2
    clock.config(text=time2)
    # calls itself every 200 milliseconds
    # to update the time display as needed
    # could use >200 ms, but display gets jerky
    clock.after(200, tick)
tick()





root.mainloop()
