from tkinter import *
from deafult import *
from page2 import *
from page3 import *
from page4 import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from database import *

class Page1(Default):
    def __init__(self,root):
        self.root=root
        super().__init__(self.root)
        self.add_widgets()


    def login(self):
        print("login function called")
        top1=Toplevel()
        top1.geometry("500x200+330+275")
        fr=Frame(top1,width=500,height=200,bg="light yellow")
        fr.pack()
        username=Label(fr,text="Username :",width=10,height=2,bg="light yellow",font="Times 13")
        username.place(x=35,y=30)
        self.e1=Entry(fr,width=40,bg="white")
        self.e1.place(x=125,y=40)
        password=Label(fr,text="Password :",width=10,height=2,bg="light yellow",font="Times 13")
        password.place(x=35,y=80)
        self.e2=Entry(fr,width=40,bg="white",show="*")
        self. e2.place(x=125,y=90)

        b3=Button(fr,text="Proceed",width=10,height=1,bg="thistle2",relief=RAISED,borderwidth=3,command=lambda:self.Validate(top1))
        b3.place(x=215,y=130)

    def Validate(self,top1):
        name=self.e1.get()
        pwd=self.e2.get()
        query="Select * from Admint where AdmintName='%s' and AdmintPassword='%s'"
        params=(name,pwd)
        result=DatabaseHelper.get_data(query,params)
        if(result is None or len(result)==0):
            messagebox.showerror("Login Failed","Incorrect credentials")
        else:
            top1.destroy()
            self.frame.destroy()
            print(result)
            if (result[7] == "Committe Member"):
                print("redirecting to page 3")
                self.redirect = Page3(self.root,result)
            elif(result[7]== "Resident"):
                print("redirecting to page 2")
                self.redirect = Page2(self.root,result)
                print("Page 2 is destroyed and page 1 reaches line 59")
            else:
                print("redirecting to page 4")
                self.redirect =Page4(self.root,result)

    def signup(self):
        top2 = Toplevel()
        top2.geometry("800x400+188+195")
        f = Frame(top2, width=800, height=400, bg="light yellow")
        f.pack()
        name = Label(f, text="Name :", width=10, height=2, bg="light yellow", font="Times 13")
        name.place(x=28, y=30)
        self.e3 =Entry(f, width=60, bg="white")
        self.e3.place(x=48, y=64)
        email= Label(f, text="Email_Id :", width=10, height=2, bg="light yellow", font="Times 13")
        email.place(x=35, y=80)
        self.e4 = Entry(f, width=60, bg="white")
        self.e4.place(x=48, y=114)
        r1=Radiobutton(f,text="Male",bg="light yellow",value=2,font="Times 13")
        r1.place(x=38,y=140)
        r2 = Radiobutton(f, text="Female",bg="light yellow",value=1,font="Times 13")
        r2.place(x=118, y=140)
        phone = Label(f, text=" Contact Details :", width=14, height=2, bg="light yellow", font="Times 13")
        phone.place(x=37, y=163)
        self.e5 = Entry(f, width=40, bg="white")
        self.e5.place(x=47, y=198)
        pw = Label(f, text="Password :", width=10, height=2, bg="light yellow", font="Times 13")
        pw.place(x=35, y=218)
        self.e6 = Entry(f, width=60, bg="white")
        self.e6.place(x=48, y=255)
        v=["101","102","103","104","201","202","203","204","301","302","303","304","401","402","403","404","501","502","503","504"]
        self.combo1 = Combobox(f, values=v, width=25)
        self.combo1.set("FLAT NO*")
        self.combo1.place(x=460,y=55)
        v2=["Resident","Committe Member","Staff"]
        self.role = Combobox(f, values=v2, width=25)
        self.role.set("Your role in society*")
        self.role.place(x=460, y=110)
        v1=["A","B","C","D"]
        self.combo = Combobox(f, values=v1, width=15)
        self.combo.set("Wing*")
        self.combo.place(x=650, y=55)

        b4 = Button(f, text="Submit", width=10, height=1, bg="thistle2", relief=RAISED, borderwidth=3,command=lambda:self.register_user(top2))
        b4.place(x=350, y=295)

    def register_user(self,top2):
        name = self.e3.get()
        contact = self.e5.get()
        email = self.e4.get()
        pwd = self.e6.get()
        flat=self.combo1.get()
        wing=self.combo.get()
        r=self.role.get()
        if (name == "" or contact == "" or email == "" or pwd == ""):
            messagebox.showwarning("Mandatory fields", "Please fill all the fields")
            top2.focus_set()
        else:
            query = "Insert into Admint(AdmintName,AdmintPassword,AdmintEmail,AdmintContact,AdmintFlat,AdmintWing,AdmintRole) Values ('%s','%s','%s','%s','%s','%s','%s')"
            args = (name, pwd, email,contact,flat,wing,r)
            DatabaseHelper.execute_query(query % args)
            messagebox.showinfo("Success", "User registered successfully. Please login")
            top2.destroy()

    def add_widgets(self):
        print("xyz")
        self.b1=Button(self.label,text="LOGIN",width=18,height=2,activebackground="light green",activeforeground="black",bg="misty rose",font="Times 10 bold",command=self.login)
        self.b1.place(x=700,y=550)
        self.b2 = Button(self.label, text="SIGN UP", width=18, height=2, activebackground="light green", activeforeground="black",bg="misty rose",font="Times 10 bold",command=self.signup)
        self.b2.place(x=850, y=550)
        """self.c=Canvas(self.label,height=50,width=150)
        self.mytxt=self.c.create_text(10,50,anchor="nw")
        self.c.itemconfig(mytxt,text="ELEGANCE IS IRRESISITABLE")
        self.c.place(x=700,y=200)"""

"""root = Tk()
root.geometry("1000x625+100+100")
p=Page1(root)
root.mainloop()"""