from tkinter import *

from tkinter import simpledialog ,messagebox


#window
tkWindow = Tk()
tkWindow.geometry('350x150')
tkWindow.title('Log In Form')
tkWindow.configure(background="pink", relief="solid")
tkWindow.geometry("700x500")

def login():
    users={"user1" : "1","user2":"2", "user3":"3", "user4":"4", "user5":"5"}
    username=usernameEntry.get()
    password=passwordEntry.get()


    if (username, password)  in users.items():
        messagebox.showinfo("Login status", "Login successful")
        tkWindow.withdraw()
        import Flight
        Flight.qualify()
    else:
        messagebox.showerror("Login Status","Incorrect password or username")
        usernameEntry.delete(0,END)
        passwordEntry.delete(0,END)

lbh=Label(tkWindow,text="LogIn Page:", font="arial 18 bold")
lbh.pack()
#username label and text entry box
usernameLabel = Label(tkWindow, text="User Name")
usernameLabel.pack(pady=20, )

usernameEntry = Entry(tkWindow)
usernameEntry.pack(pady=10)

#password label and password entry box
passwordLabel = Label(tkWindow,text="Password")
passwordLabel .pack(pady=20)

passwordEntry = Entry(tkWindow, show='*')
passwordEntry.pack(pady=10)



#login button
loginButton = Button(tkWindow, text="Login", command=login)
loginButton.pack(pady=20)

tkWindow.mainloop()
