from tkinter import *
from tkinter import messagebox
from FBMS.pages.issuepage import submissions
from FBMS.pages.submitpg import submission
from FBMS.pages.displaypage import summission
import sqlite3

class home():
    def __init__(self,home1):
        self.home1= home1
        
        self.home1.config(bg='#f2debd')
        self.home1.geometry('900x900')
        self.home1.title("Home Page")

        self.c = StringVar()

        def database(self):
            country=self.c.get()


        self.label_0 = Label(home1, text='Welcome to Book Management System',width=33,font=("Arial bold",20),pady=10,padx=120,bg='#a1dbcd',relief=SUNKEN)
        self.label_0.place(x=60,y=0)

        self.label_1 = Label(home1, text='...Learning Made More Easy, Enjoy Learning With Us...',font=('Arial Bold',20),bg='yellow',fg='blue',relief=RAISED)
        self.label_1.place(x=95,y=85)


        self.label_2 = Label(home1, text='Welcome !!, Have a Nice Day',width=30,font=('Arial Bold',15),bg='red',fg='white',relief=RAISED)
        self.label_2.place(x=250,y=155)

        self.label_21 = Label(home1, text='Quotes on Books',width=20,font=("calibri italic",20),bg='blue',fg='white')
        self.label_21.place(x=10,y=230)

        self.label_22 = Label(home1, text='1. There is no FRIEND as loyal as a BOOK.',width=34,font=("bold",12))
        self.label_22.place(x=10,y=285)

        self.label_3 = Label(home1, text=' 2. A BOOK is a gift you can open again and again. ',width=39,font=("bold",12))
        self.label_3.place(x=10,y=325)

        self.label_4 = Label(home1, text=" 3. Reading a good BOOK is like taking a JOURNEY.",width=40,font=("bold",12))
        self.label_4.place(x=10,y=365)

        self.label_5 = Label(home1, text="5. BOOKS have to be heavy because the whole WORLD is inside them.",width=55,font=("bold",12))
        self.label_5.place(x=10,y=445)

        self.label_6 = Label(home1, text="4. A BOOK is a DREAM that you hold in your hands.",width=40,font=("bold",12))
        self.label_6.place(x=10,y=405)

        self.label_7 = Label(home1, text='Available Books: ',width=20,font=("ARIAL Bold",12),bg='#f2debd')
        self.label_7.place(x=420,y=250)

        list1 = ['Data Structures','Python','Database Management System','Computer Organization and Design','Discrete Mathematics','Unity','Software Engineering','Operating Systems','Theory of Computation','C Programming','JAVA from scratch'];
        c=StringVar()
        droplist=OptionMenu(home1,c,*list1)
        droplist.config(width=35,bg='red',fg='black')
        c.set('Category of books available')
        droplist.place(x=600,y=245)

        Button(home1, text='Issue Books',width=15,bg='brown',fg='white',command=self.issue).place(x=550,y=310)
        Button(home1, text='Submit Books',width=15,bg='brown',fg='white',command=self.submit).place(x=710,y=310)

        self.label_8 = Label(home1, text='Books in my Account: ',width=20,font=("ARIAL Bold",14))
        self.label_8.place(x=75,y=510)
        Button(home1, text='My Books',width=15,bg='orange',fg='white',command=self.disp).place(x=350,y=510)

    def issue(self):
        self.home1.withdraw()
        self.root2=Toplevel(self.home1)
        submissions(self.root2)

    def submit(self):
        self.home1.withdraw()
        self.root3=Toplevel(self.home1)
        submission(self.root3)
        
    def disp(self):
        self.home1.withdraw()
        self.root4=Toplevel(self.home1)
        summission(self.root4)
