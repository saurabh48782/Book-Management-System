from tkinter import *
import time
import sqlite3
import tkinter.messagebox
from FBMS.pages.displaypage import summission

with sqlite3.connect("bookselves.db") as ab:
    cursur = ab.cursor()
cursur.execute("CREATE TABLE IF NOT EXISTS bookself (book_id INTEGER NOT NULL,book_name TEXT NOT NULL,day INTEGER NOT NULL,month INTEGER NOT NULL,user_name TEXT NOT NULL);")
cursur.execute("SELECT * FROM bookself")
ab.commit()
ab.close()

class submissions:
    def __init__(self, raw):
        self.conn=sqlite3.connect('bookselves.db')

        self.c=self.conn.cursor()

        self.raw = raw
        self.raw.title("Issue Page")
        self.raw.geometry("690x290+0+0")
        self.raw.configure(bg='gray')

        self.Mainframe=Frame(self.raw,bg='gray')
        self.Mainframe.pack(side=TOP)

        self.Titleframe =Frame(self.Mainframe,width=625,padx=10,bd=10,bg='orange')
        self.Titleframe.pack(side=TOP)

        self.Title =Label(self.Titleframe,width=20,bg='skyblue',fg='orange',font=('arial',20,'bold'),text="BOOK ISSUE",)
        self.Title.pack(side=TOP)

        

        self.Dataframe=Frame(self.Mainframe ,bd=10,width=750,height=500,bg='gray',padx=10,relief=RIDGE)
        self.Dataframe.pack(side=TOP)

       

        self.Buttonframe=Frame(self.Mainframe, bd=5, width=150,height=50,padx=10,relief=RIDGE)
        self.Buttonframe.pack(side=TOP)

        self.username=Label(self.Dataframe, font=('arial',16,'bold'),text="Username",padx=2,pady=2)
        self.username.grid(row=0,column=0)
        self.username=Entry(self.Dataframe,font=('arial',16,'bold'),width=25)
        self.username.grid(row=0,column=1)
        self.bookname=Label(self.Dataframe, font=('arial',16,'bold'),text="BookName",padx=2,pady=2)
        self.bookname.grid(row=1,column=0)
        self.bookname=Entry(self.Dataframe, font=('arial',16,'bold'),width=25)
        self.bookname.grid(row=1,column=1)
        self.bookid=Label(self.Dataframe, font=('arial',16,'bold'),text="BookId",padx=2,pady=2)
        self.bookid.grid(row=2,column=0)
        self.bookid=Entry(self.Dataframe, font=('arial',16,'bold'),width=25)
        self.bookid.grid(row=2,column=1)

        self.button=Button(self.Buttonframe, text='Issue Book',bg='skyblue',fg='orange',font=('arial',14,'bold'),width=20,bd=4, command = self.on_click)
        self.button.grid(row=0,column=0)
        self.button1=Button(self.Buttonframe, text='Go to My Books',bg='skyblue',fg='orange',font=('arial',14,'bold'),width=20,bd=4,command=self.some)
        self.button1.grid(row=0,column=1)
    def on_click(self):
        if len(self.username.get()) < 1:
            messagebox.showerror('Error',"Username should not be empty.")
        elif '@' not in self.username.get():
            messagebox.showerror("Error","Username must contain '@' in it")
        elif len(self.bookname.get()) < 1:
            messagebox.showerror('Error',"Book Name must be filled.")
        elif len(self.bookid.get()) < 1:
            messagebox.showerror('Error',"Book ID must be filled.")
        else:
            self.c.execute('INSERT INTO bookself (book_id,book_name,day,month,user_name) VALUES(?,?,?,?,?)',((self.bookid.get()),(self.bookname.get()),int(time.localtime()[2]),int(time.localtime()[1]),(self.username.get())))
            self.conn.commit()
            messagebox.showinfo('Successfull',"Your Book have been issued !!\nCheck for confirmation in My Books section")

    def some(self):
        self.raw.withdraw()
        self.root5=Toplevel(self.raw)
        summission(self.root5)

