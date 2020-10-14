from tkinter import *
import time
import sqlite3
import tkinter.messagebox

class submission:
    def __init__(self, roots):
        self.conn=sqlite3.connect('bookselves.db')

        self.c=self.conn.cursor()

        self.roots = roots
        self.roots.title("Book Management System")
        self.roots.geometry("690x290+0+0")
        self.roots.configure(bg='gray')

        self.Mainframe=Frame(self.roots,bg='gray')
        self.Mainframe.pack(side=TOP)

        self.Titleframe =Frame(self.Mainframe,width=625,padx=10,bd=10,bg='orange')
        self.Titleframe.pack(side=TOP)

        self.Title =Label(self.Titleframe,width=20,bg='skyblue',fg='orange',font=('arial',20,'bold'),text="SUBMITTING THE BOOK",)
        self.Title.pack(side=TOP)

        

        self.Dataframe=Frame(self.Mainframe ,bd=10,width=650,height=300,bg='gray',padx=10,relief=RIDGE)
        self.Dataframe.pack(side=TOP)

        self.Dataframeleft= LabelFrame(self.Dataframe,bd=8,width=400,height=200,padx=10,relief=RIDGE,fg='orange',font=('arial',14,'bold'),text="Details of book:",)
        self.Dataframeleft.pack(side=LEFT)

        self.Dataframeright= LabelFrame(self.Dataframe,bd=8,width=250,height=150,padx=10,relief=RIDGE,fg='orange',font=('arial',14,'bold'),text="LOG:",)
        self.Dataframeright.pack(side=LEFT)

        self.Buttonframe=Frame(self.Mainframe, bd=5, width=150,height=50,padx=10,relief=RIDGE)
        self.Buttonframe.pack(side=TOP)

        self.username=Label(self.Dataframeleft, font=('arial',12,'bold'),text="Username",padx=2,pady=2)
        self.username.grid(row=0,column=0)
        self.username=Entry(self.Dataframeleft,font=('arial',12,'bold'),width=15)
        self.username.grid(row=0,column=1)
        self.bookname=Label(self.Dataframeleft, font=('arial',12,'bold'),text="Book Name",padx=2,pady=2)
        self.bookname.grid(row=1,column=0)
        self.bookname=Entry(self.Dataframeleft, font=('arial',12,'bold'),width=15)
        self.bookname.grid(row=1,column=1)
        self.bookid=Label(self.Dataframeleft, font=('arial',12,'bold'),text="BookId",padx=2,pady=2)
        self.bookid.grid(row=2,column=0)
        self.bookid=Entry(self.Dataframeleft, font=('arial',12,'bold'),width=15)
        self.bookid.grid(row=2,column=1)

        self.button=Button(self.Buttonframe, text='SUBMIT',bg='skyblue',fg='orange',font=('arial',14,'bold'),width=20,bd=4, command = self.dis)
        self.button.grid(row=0,column=0)
        self.button1=Button(self.Buttonframe, text='LOGOUT',bg='skyblue',fg='orange',font=('arial',14,'bold'),width=20,bd=4,command = self.quit)
        self.button1.grid(row=0,column=1)
        
    def dis(self):
        if len(self.username.get()) < 1:
            messagebox.showerror('Error',"Username should not be empty.")
        elif '@' not in self.username.get():
            messagebox.showerror("Error","Username must contain '@' in it")
        elif len(self.bookname.get()) < 1:
            messagebox.showerror('Error',"Book Name must be filled.")
        elif len(self.bookid.get()) < 1:
            messagebox.showerror('Error',"Book ID must be filled.")
        else:
            for row in self.c.execute('SELECT * FROM bookself'):
                day=28
                month=10
                if(row[3] == month):
                    if((row[2]-day) < 10):
                        self.fine = Label(self.Dataframeright, text = "Submmited Successfully")
                        self.c.execute("DELETE FROM bookself WHERE book_name = 'self.bookname.get()' ")
                    else:
                        self.fine = Label(self.Dataframeright, text = "you are fined with 100/-")
                else:
                    self.fine = Label(self.Dataframeright, text = "you are fined.. with 100/-")
            self.fine.pack(side = TOP)

    def quit(self):
        self.roots.withdraw()
        messagebox.showinfo('Logout confirmation',"Are you sure you want to logout ??\n Press OK to confirm")
        messagebox.showinfo('Successfull',"You have been Logged Out successfully.")
