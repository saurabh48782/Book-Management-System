from tkinter import *
from FBMS.pages.homepage import home
import sqlite3
from tkinter import messagebox as ms

with sqlite3.connect("login.db") as db:
    cursur = db.cursor()
cursur.execute("CREATE TABLE IF NOT EXISTS user (username TEXT NOT NULL,password TEXT NOT NULL,fullname TEXT NOT NULL,gender TEXT NOT NULL,mobile NOT NULL);")
cursur.execute("SELECT * FROM user")
db.commit()
db.close()

class main():
    def __init__(self,master):
        self.master = master
        
        self.master.config(bg='#f2debd')
        self.master.title('Book Management System')
        self.master.geometry('700x700')

        self.master.config(bg='#f2debd')

        self.username = StringVar()
        self.password = StringVar()
        self.n_username = StringVar()
        self.n_password = StringVar()
        self.fullname = StringVar()
        self.gender = IntVar()
        self.mobile = StringVar()
        self.widgets()

    def login(self):
        with sqlite3.connect("login.db") as db:
            cursur = db.cursor()
        find_user = ("SELECT * FROM user WHERE username = ? AND password = ?")
        cursur.execute(find_user,[(self.username.get()),(self.password.get())])
        results = cursur.fetchall()
        if results:
            self.Home()
            
            
        else:
            ms.showerror("Oops!!","Username or Password not matched !! ")
    def new_user(self):
        with sqlite3.connect("login.db") as db:
            cursur = db.cursor() 
        find_user = ("SELECT * FROM user WHERE username = ?")
        cursur.execute(find_user,[(self.username.get())])
        if cursur.fetchall():
            ms.showerror("Oops!","Username Taken!!")
        elif '@' not in self.n_username.get():
            ms.showerror("Error","Username must contain '@' in it")
        elif len(self.n_password.get()) < 6:
            ms.showerror("Error","Password must contain atleast six characters in it")
        elif len(self.mobile.get()) < 10:
            ms.showerror("Error","Enter valid Mobile Number")
        else:
            ms.showinfo('Success!!',"Your account has been created")
            self.log()
        insert = 'INSERT INTO user(username,password,fullname,gender,mobile) VALUES(?,?,?,?,?)'
        cursur.execute(insert,[(self.n_username.get()),(self.n_password.get()),(self.fullname.get()),(self.gender.get()),(self.mobile.get())])
        db.commit()

    def log(self):
        self.username.set("")
        self.password.set("")
        self.crf.pack_forget()
        self.head['text'] = "WELCOME TO BOOK MANAGEMENT SYSTEM"
        self.logf.pack()
    def cr(self):
        self.n_username.set("")
        self.n_password.set("")
        self.head['text'] = "WELCOME TO BOOK MANAGEMENT SYSTEM"
        self.logf.pack_forget()
        self.crf.pack()
        
    def widgets(self):
        self.head=Label(self.master,text='WELCOME TO BOOK MANAGEMENT SYSTEM',font=('Arial Bold',20),pady=10,padx=120,bg='#a1dbcd',relief=SUNKEN)
        self.head.pack()

        self.head1=Label(self.master,text='\n',bg='#f2debd')
        self.head1.pack()
        
        self.head2=Label(self.master,text='...Learning Made More Easy, Enjoy Learning With Us...',font=('Arial Bold',20),bg='yellow',fg='blue',relief=RAISED)
        self.head2.pack()

        self.head3=Label(self.master,text='\n\n\n\n',bg='#f2debd')
        self.head3.pack()

        self.logf = Frame(self.master,padx = 10,pady = 10)
        Label(self.logf,text="Enter Your Credentials Here...",font= ('ARIAL BOLD',20),padx=5,pady=5,bg='orange').grid(sticky=W)
        Label(self.logf,text="Username:",font= ('ARIAL BOLD',20),padx=5,pady=5).grid(row=1,column=0,sticky=W)
        Entry(self.logf,textvariable = self.username,bd=8,font = ('calibri',15,'bold')).grid(row=1,column=1,sticky=E)
        Label(self.logf,text="Password:",font= ('ARIAL BOLD',20),padx=5,pady=5).grid(row=2,column=0,sticky=W)
        Entry(self.logf,textvariable = self.password,bd=8,font = ('calibri',15,'bold'),show='*').grid(row=2,column=1,sticky=E)
        Button(self.logf,text=" Login ",bd=7,font = ("monaco",15,'bold'),padx=5,pady=5,fg='black',bg='red',command=self.login).grid(row=3)
        Button(self.logf,text=" Make New Account ",bd=7,font = ("monaco",15,'bold'),padx=5,pady=5,fg='white',bg='blue',command=self.cr).grid(row=3,column=1)
        self.logf.pack()

        self.crf = Frame(self.master,padx = 10,pady = 10)
        Label(self.crf,text="Sign Up Here...",font= ('ARIAL BOLD',20),padx=5,pady=5,bg='orange').grid(sticky=W)
        Label(self.crf,text="Username:",font= ('ARIAL BOLD',20),padx=5,pady=5).grid(row=1,column=0,sticky=W)
        Entry(self.crf,textvariable = self.n_username,bd=8,font = ('calibri',15,'bold')).grid(row=1,column=1,sticky=E)
        Label(self.crf,text="Password:",font= ('ARIAL BOLD',20),padx=5,pady=5).grid(row=2,column=0,sticky=W)
        Entry(self.crf,textvariable = self.n_password,bd=8,font = ('calibri',15,'bold'),show='*').grid(row=2,column=1,sticky=E)
        Label(self.crf,text="Full Name:",font= ('ARIAL BOLD',20),padx=5,pady=5).grid(row=3,sticky=W)
        Entry(self.crf,textvariable = self.fullname,bd=8,font = ('calibri',15,'bold')).grid(row=3,column=1,sticky=E)
        Label(self.crf,text="Gender:",font= ('ARIAL BOLD',20),padx=5,pady=5).grid(row=4,sticky=W)
        Radiobutton(self.crf, text="Male",padx = 5, variable=self.gender, value=1).grid(row=4,column=1)
        Radiobutton(self.crf, text="Female",padx = 20, variable=self.gender, value=2).grid(row=4,column=2,sticky=E)
        
        Label(self.crf,text="Mobile:",font= ('ARIAL BOLD',20),padx=5,pady=5).grid(row=5,column=0,sticky=W)
        Entry(self.crf,textvariable = self.mobile,bd=8,font = ('calibri',15,'bold')).grid(row=5,column=1,sticky=E)
        Button(self.crf,text=" Go To Login ",bd=7,font = ("monaco",15,'bold'),padx=5,pady=5,fg='white',bg='brown',command=self.log).grid(row=6)
        Button(self.crf,text=" Create Account ",bd=7,font = ("monaco",15,'bold'),padx=5,pady=5,fg='white',bg='brown',command=self.new_user).grid(row=6,column=1)
        self.logf.pack()

    def Home(self):
        self.master.withdraw()
        self.root2=Toplevel(self.master)
        home(self.root2)

root= Tk()
main(root)
root.mainloop()
        
        
