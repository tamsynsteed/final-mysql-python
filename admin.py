from tkinter import *
import mysql.connector
import tkinter as tk
from tkinter import messagebox, simpledialog
import datetime


mydb= mysql.connector.connect(user="tamsynsteed", password="@Lifechoices314", database="lifechoicesonline", host="127.0.0.1", auth_plugin="mysql_native_password")
#connect database

cursor=mydb.cursor()

x = datetime.datetime.now()

#this function displays all the data in the users table and logged table. the data is displayed in listboxes
def display():
        cursor.execute("SELECT ID FROM users")

        id = cursor.fetchall()

        for x in id:
            listbox_id.insert(END, x)

        listbox_id.insert(END, str(cursor.rowcount) + " rows")

        cursor.execute("SELECT full_name FROM users")

        name = cursor.fetchall()

        for x in name:
            listbox_fullname.insert(END, x)

        listbox_fullname.insert(END, str(cursor.rowcount) + " rows")

        cursor.execute("SELECT user_name FROM users")

        uName = cursor.fetchall()
        for x in uName:
            listbox_uname.insert(END, x)
        listbox_uname.insert(END, str(cursor.rowcount) + " rows")

        cursor.execute("SELECT password FROM users")

        pas = cursor.fetchall()
        for x in pas:
            listbox_pass.insert(END, x)
        listbox_pass.insert(END, str(cursor.rowcount) + " rows")

        cursor.execute("SELECT mobile_number FROM users")

        mobileno = cursor.fetchall()
        for x in mobileno:
            listbox_mobile.insert(END, x)
        listbox_mobile.insert(END, str(cursor.rowcount) + " rows")

        cursor.execute("SELECT status FROM users")

        cat = cursor.fetchall()
        for x in cat:
            listbox_status.insert(END, x)
        listbox_status.insert(END, str(cursor.rowcount) + " rows")

        cursor.execute("SELECT date_joined FROM users")

        date = cursor.fetchall()
        for x in date:
            listbox_date.insert(END, x)
        listbox_date.insert(END, str(cursor.rowcount) + " rows")

        cursor.execute("SELECT user_name FROM logged")

        Unamelogged = cursor.fetchall()
        for x in Unamelogged:
            listbox_user.insert(END, x)
        listbox_user.insert(END, str(cursor.rowcount) + " rows")

        cursor.execute("SELECT time_in FROM logged")

        timeIn = cursor.fetchall()
        for x in timeIn:
            listbox_timein.insert(END, x)
        listbox_timein.insert(END, str(cursor.rowcount) + " rows")

        cursor.execute("SELECT time_out FROM logged")

        timeOut = cursor.fetchall()
        for x in timeOut:
            listbox_timeout.insert(END, x)
        listbox_timeout.insert(END, str(cursor.rowcount) + " rows")



#add  function allows the admin to register a new user from the admin portal. the data is stored in users table
def add():
        comm3 = "INSERT INTO users (full_name, user_name, password, mobile_number, status, date_joined) VALUES (%s, %s, %s,%s, %s, %s)"
        user_info1 = str(fullname1.get()), str(username.get()), password.get(),mobile.get(),str(tkvar.get()),x
        cursor.execute(comm3, user_info1)
        mydb.commit()
        messagebox.showinfo("Confirmation", "User created successfully")

#this function clears all data in the listbox
def clear():
    listbox_timeout.delete(0,END)
    listbox_timein.delete(0,END)
    listbox_uname.delete(0,END)
    listbox_date.delete(0,END)
    listbox_status.delete(0, END)
    listbox_mobile.delete(0,END)
    listbox_pass.delete(0, END)
    listbox_fullname.delete(0,END)
    listbox_id.delete(0,END)
    listbox_user.delete(0,END)


def delete():

        fullname=fullname1.get()

        Delete="delete from users where full_name='%s'" %(fullname)
        cursor.execute(Delete)
        mydb.commit()
        messagebox.showinfo("Information","Record Deleted")

#this fucntion allows the admin user to make a registered user an admin.

#the admin user will input the user's ID. the user_name and password will be displayed in the admin table allowing the user to login as an admin
def makeAdmin():
    def make_admin_action():
        mydb= mysql.connector.connect(user="tamsynsteed", password="@Lifechoices314", database="lifechoicesonline", host="127.0.0.1", auth_plugin="mysql_native_password")

        mycursor = mydb.cursor()
        try:
            user_id=int(admin_id.get())

        except:
            messagebox.showerror("Error","Only enter a number for the ID")

        sql= "INSERT INTO admin (username, password) select user_name, password from users where id=%s"
        try:
            mycursor.execute(sql,[(user_id)])
            mydb.commit()
            messagebox.showinfo("Success", "Successfully made  user id="+str(user_id)+" an admin")
        except:
            messagebox.showerror("Error", "Error in my sql connection")


    newWindow = Tk()
    newWindow.title("Make User Admin")
    newWindow.geometry("350x150")

    newWindow.configure(background="black")


    lbl_id=Label(newWindow,text="Enter ID of user to add as Admin")
    lbl_id.place(x=5,y=5)

    admin_id=Entry(newWindow,width=10)
    admin_id.place(x=230,y=5)

    adminBtn=Button(newWindow, text="Make Admin",command=make_admin_action)
    adminBtn.place(x=220,y=30)

    newWindow.mainloop()

def  back():
    master.destroy()
    import loginpage

def sign_out():
    x = datetime.datetime.now()
    y = x.strftime("%H:%M")
    MsgBox = tk.messagebox.askquestion ('Sign Out','Are you sure you want to sign out?',icon = 'warning')
    if MsgBox == 'yes':

       x = datetime.datetime.now()
       y = x.strftime("%H:%M")
       myuser=simpledialog.askstring("Input", "Please re-enter username ", parent=master)
       exe = "UPDATE logged SET time_out = curtime()where user_name=%s"
       cursor.execute(exe, [myuser])
       mydb.commit()

       master.withdraw()
       import loginpage


master = tk.Tk()

master.title('Administration')
master.geometry("700x1000")
master.configure(background="black")

lbluser=tk.Label(master, text="Administration Portal", bg="cadet blue")
lbluser.pack(pady=10)

#labels
lblid=Label(master,text="ID", bg="grey")
lblid.place(x=50,y=40)

lblful=Label(master,text="Fullname", bg="grey")
lblful.place(x=120,y=40)

lblid=Label(master,text="Username", bg="grey")
lblid.place(x=200,y=40)

lblid=Label(master,text="Password", bg="grey")
lblid.place(x=300,y=40)

lblid=Label(master,text="Mobile no.", bg="grey")
lblid.place(x=385,y=40)

lblid=Label(master,text="Category", bg="grey")
lblid.place(x=480,y=40)

lblid=Label(master,text="Date Joined", bg="grey")
lblid.place(x=563,y=40)

#####################################################################################################
#logginDataLabels
#####################################################################################################
lblid=Label(master,text="Username", bg="grey")
lblid.place(x=25,y=260)

lblid=Label(master,text="Time In", bg="grey")
lblid.place(x=160,y=260)

lblid=Label(master,text="Time Out", bg="grey")
lblid.place(x=330,y=260)






#users

listbox_id = Listbox(master,bg="cadet blue",width=10, height=10,selectbackground="grey", selectforeground="black")
listbox_id.place(x=20,y=70)

listbox_fullname = Listbox(master,bg="cadet blue",width=10,selectbackground="grey", selectforeground="black")
listbox_fullname.place(x=110,y=70)

listbox_uname = Listbox(master,bg="cadet blue",width=10,selectbackground="grey", selectforeground="black")
listbox_uname.place(x=200,y=70)

listbox_pass = Listbox(master,bg="cadet blue",width=10,selectbackground="grey", selectforeground="black")
listbox_pass.place(x=290,y=70)

listbox_mobile = Listbox(master,bg="cadet blue",width=10,selectbackground="grey", selectforeground="black")
listbox_mobile.place(x=380,y=70)

listbox_status = Listbox(master,bg="cadet blue",width=10,selectbackground="grey", selectforeground="black")
listbox_status.place(x=470,y=70)

listbox_date = Listbox(master,bg="cadet blue",width=10,selectbackground="grey", selectforeground="black")
listbox_date.place(x=560,y=70)

#######################################################################################################################
#logindata

listbox_user = Listbox(master,bg="cadet blue",width=10, height=10,selectbackground="grey", selectforeground="black")
listbox_user.place(x=20,y=290)

listbox_timein = Listbox(master,bg="cadet blue",width=20, height=10,selectbackground="grey", selectforeground="black")
listbox_timein.place(x=110,y=290)

listbox_timeout = Listbox(master,bg="cadet blue",width=20, height=10,selectbackground="grey", selectforeground="black")
listbox_timeout.place(x=280,y=290)

################################################################################################################3######

lbluser=tk.Label(master, text="Enter Fullname")
lbluser.place(x=50, y=500)

fullname1= tk.Entry(master, width=30)
fullname1.place(x=165,y=500)

lblpasswd=tk.Label(master,text="Enter Username")
lblpasswd.place(x=50, y=540)

username = tk.Entry(master,width=30)
username.place(x=165, y=540)

lblpasswd=tk.Label(master,text="Enter Password")
lblpasswd.place(x=50, y=580)

password = tk.Entry(master,width=30)
password.place(x=165, y=580)

lblmobile=tk.Label(master,text="Mobile Number")
lblmobile.place(x=50, y=620)

mobile = tk.Entry(master,width=30)
mobile.place(x=165, y=620)

lblmobile=tk.Label(master,text="Category")
lblmobile.place(x=50, y=660)

tkvar = StringVar(master)

# Dictionary with options
choices = {'Visitor','Student','Employee'}
tkvar.set('Student') # set the default option

popupMenu = OptionMenu(master, tkvar, *choices)
popupMenu.place(x=165, y=660)



logbuttn=tk.Button(master,text="ADD RECORD",command=add)
logbuttn.place(x=55, y=780)

logbuttn=tk.Button(master,text="DELETE RECORD",command=delete)
logbuttn.place(x=190, y=780)

logbuttn=tk.Button(master,text="DISPLAY DATA", command=display)
logbuttn.place(x=350, y=780)

logbuttn=tk.Button(master,text="CLEAR", command=clear)
logbuttn.place(x=490,y=780)


logbuttn=tk.Button(master,text="MAKE ADMIN",command=makeAdmin)
logbuttn.place(x=180, y=840)

logbuttn=tk.Button(master,text="SIGN OUT", command=sign_out)
logbuttn.place(x=300,y=840)



master.mainloop()
