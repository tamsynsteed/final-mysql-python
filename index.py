from tkinter import *
import mysql.connector
import tkinter as tk
from tkinter import messagebox


def login_home():
    root.withdraw()
    import loginpage

def register():
    root.withdraw()
    import register


root = tk.Tk()

root.title('Home Page')

root.geometry("450x450")
root.configure(background="black")

lbluser=tk.Label(root, text="Welcome to LIfe Choices Online", bg="cadet blue", font="22")
lbluser.pack(pady=20)

lbluser=tk.Label(root, text="Please login")
lbluser.pack(pady=20)

logbuttn=tk.Button(root,text="Login", command=login_home)
logbuttn.pack(pady=10)

lbluser=tk.Label(root, text="New visitors, please register your details below.")
lbluser.pack(pady=20)

logbuttn=tk.Button(root,text="Register", command=register)
logbuttn.pack(pady=10)

logbuttn=tk.Button(root,text="Sign Out")
logbuttn.pack(pady=60)


root.mainloop()
