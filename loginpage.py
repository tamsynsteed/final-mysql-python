from tkinter import *
import mysql.connector
import tkinter as tk
from tkinter import messagebox, simpledialog
from datetime import datetime






mydb= mysql.connector.connect(user="tamsynsteed", password="@Lifechoices314", database="lifechoicesonline", host="127.0.0.1", auth_plugin="mysql_native_password")
#connect database

mycursor=mydb.cursor()

#create fucntion that checks if input is in the users table
def verify():
    user_verification= username.get()
    pass_verification = password.get()
    sql = "select * from users where user_name = %s and password = %s"
    mycursor.execute(sql,[(user_verification), (pass_verification)])
    results = mycursor.fetchall()
    if results:
        for i in results:
            logged()
            break
    else:
            failed()

now = datetime.now()  #display the current time

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)
x = datetime.now()

def logged():  #if loggin details are correct, insert the username and times into the logged table
    x = datetime.now()
    y = x.strftime("%H:%M")
    myuser=simpledialog.askstring("Input", "Please re-enter username ", parent=mywindow)
    exe = "INSERT INTO logged VALUES (%s, curtime(), NULL)"
    mycursor.execute(exe, [myuser])
    mydb.commit()
    messagebox.showinfo("Successful", "You have successfully logged in")



    window = tk.Tk()  #create window that displays the logged in user and sign out button

    window.title('Logged In')

    window.geometry("450x450")
    window.configure(background="black")

    lbluser=tk.Label(window, text="Life Choices Online: Logged in", bg="cadet blue")
    lbluser.pack(pady=10)

    lbluser=tk.Label(window, text="You are currently LOGGED IN as:\n\n"+ username.get(), bg="grey")
    lbluser.pack(pady=10)

    regbuttn=tk.Button(window,text="Sign Out", command=sign_out)
    regbuttn.pack(pady=60)



    window.mainloop()







#if the login input is not in the user table, show an error
def failed():
    messagebox.showerror("Login failed", "Please check your username and password.")

#import the register window
def register():
    mywindow.withdraw()
    import register


#sign out of the login. sign out time will be inserted into the logged in table
def sign_out():
    x = datetime.now()
    y = x.strftime("%H:%M")
    MsgBox = tk.messagebox.askquestion ('Sign Out','Are you sure you want to sign out?',icon = 'warning')
    if MsgBox == 'yes':

       x = datetime.now()
       y = x.strftime("%H:%M")
       myuser=simpledialog.askstring("Input", "Please re-enter username ", parent=mywindow)
       exe = "UPDATE logged SET time_out = curtime()where user_name=%s"
       mycursor.execute(exe, [myuser])
       mydb.commit()


       messagebox.showinfo("Signed Out", "You have successfully signed out")
       window.withdraw()
       import loginpage


    else:
        tk.messagebox.showinfo('Return','You will now return to the application screen')







mywindow = tk.Tk()

mywindow.title('Login Page')

mywindow.geometry("450x450")
mywindow.configure(background="black")

lbluser=tk.Label(mywindow, text="Life Choices Online: Log in", bg="cadet blue")
lbluser.pack(pady=10)

#created labels and entry boxes for the input
lbluser=tk.Label(mywindow, text="Enter Username")
lbluser.place(x=50, y=100)

username= tk.Entry(mywindow, width=30)
username.place(x=165,y=100)

lblpasswd=tk.Label(mywindow,text="Enter Password")
lblpasswd.place(x=50, y=140)

password = tk.Entry(mywindow,width=30)
password.place(x=165, y=140)

logbuttn=tk.Button(mywindow,text="Sign In", command=verify)
logbuttn.place(x=145,y=200)

regbuttn=tk.Button(mywindow,text="Register", command=register)
regbuttn.place(x=220,y=200)

lblpasswd=tk.Label(mywindow,text="Press 'control a' to login as admin user")
lblpasswd.place(x=100, y=400)



import time

time1 = ''
clock = Label(mywindow, font=('times', 18, 'bold'), )
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

keyspressed=""
def key():
    global keyspressed
    mywindow.destroy()
    import admin_login

mywindow.bind("<Control-a>",lambda x: key())





mywindow.mainloop()
