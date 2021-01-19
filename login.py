from tkinter import *
import mysql.connector
import tkinter as tk

root = tk.Tk()

mydb= mysql.connector.connect(user="tamsynsteed", password="@Lifechoices314", database="hospital", host="127.0.0.1", auth_plugin="mysql_native_password")

mycursor=mydb.cursor()

root.title('Login Page')

root.geometry("450x450")
root.configure(background="black")


lbluser=tk.Label(root, text="Enter username")
lbluser.pack(x=50,y=20)




root.mainloop()
