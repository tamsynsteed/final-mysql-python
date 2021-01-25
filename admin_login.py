from tkinter import *
import mysql.connector
import tkinter as tk
from tkinter import messagebox, simpledialog
from datetime import datetime

mydb= mysql.connector.connect(user="tamsynsteed", password="@Lifechoices314", database="lifechoicesonline", host="127.0.0.1", auth_plugin="mysql_native_password")
#connect database

cursor = mydb.cursor()

#function that checks if the admin login details match the data in the admin table
def verify():
    user_verification= username.get()
    pass_verification = password.get()
    sql = "select * from admin where username = %s and password = %s"
    cursor.execute(sql,[(user_verification), (pass_verification)])
    results = cursor.fetchall()
    if results:
        for i in results:
            logged()
            break
    else:
            failed()

def failed():
    messagebox.showerror("Login failed", "Please check your username and password.")

#if the data matches, the login time is inserted into logged table
def logged():
    x = datetime.now()
    y = x.strftime("%H:%M")
    myuser=simpledialog.askstring("Input", "Please re-enter username ", parent=root)
    exe = "INSERT INTO logged VALUES (%s, curtime(), NULL)"
    cursor.execute(exe, [myuser])
    mydb.commit()
    messagebox.showinfo("Successful", "You have successfully logged in")

    root.withdraw()
    import admin

def back():
    root.withdraw()
    import loginpage

root = tk.Tk()

root.title('Login: Admin')

root.geometry("450x450")
root.configure(background="black")

lbluser=tk.Label(root, text="Life Choices Online: Admin Log in", bg="cadet blue")
lbluser.pack(pady=10)

lbluser=tk.Label(root, text="Enter Username")
lbluser.place(x=50, y=100)

username= tk.Entry(root, width=30)
username.place(x=165,y=100)

lblpasswd=tk.Label(root,text="Enter Password")
lblpasswd.place(x=50, y=140)

password = tk.Entry(root,width=30)
password.place(x=165, y=140)

logbuttn=tk.Button(root,text="Sign In", command=verify)
logbuttn.place(x=145,y=200)

logbuttn=tk.Button(root,text="Back", command=back)
logbuttn.place(x=220,y=200)

lbluser=tk.Label(root, text="Admin login details:\n\nusername: admin\n\npassword: 1234")
lbluser.place(x=155, y=300)


root.mainloop()
