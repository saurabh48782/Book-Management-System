from tkinter import *
import time
import sqlite3
import tkinter.messagebox

class summission:
    def __init__(self, root10):
        self.conn=sqlite3.connect('bookselves.db')

        self.c=self.conn.cursor()

        self.root10 = root10
        self.root10.title("My Books")
        self.root10.geometry("690x290+0+0")
        self.root10.configure(bg='gray')

        self.Mainframe=Frame(self.root10,bg='gray')
        self.Mainframe.pack(side=TOP)

        self.Titleframe =Frame(self.Mainframe,width=625,padx=10,bd=10,bg='orange')
        self.Titleframe.pack(side=TOP)

        self.Title =Label(self.Titleframe,width=20,bg='skyblue',fg='orange',font=('arial',20,'bold'),text="BOOKS ISSUED FOR ME",)
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
        

        self.button=Button(self.Buttonframe, text='View Books',bg='skyblue',fg='orange',font=('arial',14,'bold'),width=20,bd=4,command = self.display)
        self.button.grid(row=0,column=0)
        self.button1=Button(self.Buttonframe, text='Logout from account',bg='skyblue',fg='orange',font=('arial',14,'bold'),width=20,bd=4,command=self.quit)
        self.button1.grid(row=0,column=1)
    def display(self):
        if len(self.username.get()) < 1 :
            messagebox.showerror("Error!!","Please enter Username")
        elif '@' not in self.username.get():
            messagebox.showerror("Error","Username must contain '@' in it")
        else:
            for row in self.c.execute("select book_name from bookself where user_name = '" + str(self.username.get()) + "'"):
                self.x = Label(self.Dataframeright,text = row[0], font=('arial',14,'bold'),width=20,bd=4,bg='red',fg='blue')
                self.x.pack(side = 'top')
    def quit(self):
        self.root10.withdraw()
        messagebox.showinfo('Logout confirmation',"Are you sure you want to logout ??\n Press OK to confirm")
        messagebox.showinfo('Successfull',"You have been Logged Out successfully.")


        
