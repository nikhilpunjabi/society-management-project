from tkinter import *
from PIL import ImageTk,Image
from database import *

from network import *
from tkinter import messagebox



class Page3:
    def __init__(self,root,result):
        print("Page 3 starts")
        self.root=root
        self.details=result
        self.frame = Frame(self.root,width=1000,height=625,bg="white")
        self.frame. pack()
        self.img1 = ImageTk.PhotoImage(Image.open("wallr.jpg"))
        self.lab2 = Label(self.frame, width=1000, height=625, image=self.img1)
        self.lab2.pack()
        self.c1=Canvas(self.frame,width=1000,height=50,bg="black")
        self.c1.place(x=0,y=10)
        self.b1=Button(self.c1,text="Logout",bg="black",fg="white",width=6,height=2,relief=FLAT,command=lambda:self.logout(self.root))
        self.b1.place(x=940,y=5)
        self.b2 = Button(self.c1, text="Pay Maintenance", bg="black", fg="white", width=20, height=2, relief=FLAT,command=self.pay)
        self.b2.place(x=7, y=5)
        self.b3 = Button(self.c1, text="Photos", bg="black", fg="white", width=6, height=2, relief=FLAT,command=self.Photo)
        self.b3.place(x=160, y=5)
        self.b4 = Button(self.c1, text="About!", bg="black", fg="white", width=6, height=2, relief=FLAT,command=self.About)
        self.b4.place(x=220, y=5)
        self.b5 = Button(self.c1, text="Send Email", bg="black", fg="white", width=18, height=2, relief=FLAT,command=self.mail)
        self.b5.place(x=300, y=5)
        self.b6 = Button(self.c1, text="Record", bg="black", fg="white", width=18, height=2, relief=FLAT,command=self.record)
        self.b6.place(x=420, y=5)



    def logout(self,root):
        #self.root.destroy()
        self.frame.destroy()
        import page1
        page1.Page1(self.root)
        print("Page 3 logout is called and window destroyed")

    def mail(self):
        sendw = Toplevel()
        sendw.geometry("550x300+260+150")
        sendw.focus_set()
        fr1 = Frame(sendw,bg="light yellow",width=550,height=550)
        fr1.pack()
        """self.img1 = ImageTk.PhotoImage(Image.open("wall(1).jpg"))
        l2 = Label(top, width=550, height=550, image=self.img1)
        l2.pack()"""
        l1 = Label(fr1, text="From:", width=10, height=2, bg="light yellow", fg="black")
        l1.place(x=20, y=30)
        self.e1 = Label(fr1, text="2017.avinash.bhawnani@ves.ac.in", width=30, height=1)
        self.e1.place(x=30, y=60)
        l3 = Label(fr1, text="To:", bg="light yellow", width=10, height=2)
        l3.place(x=20, y=80)
        self.e2 = Entry(fr1, width=45)
        self.e2.place(x=25, y=115)

        b1=Button(fr1,text="send",width=6,height=1,bg="light blue",command=lambda:self.send(sendw))
        b1.place(x=250,y=190)

    def send(self,window):
        str=self.e2.get()
        n=Network(str)
        messagebox.showinfo("Successful","Message Sent")

    def Photo(self):
        top = Toplevel()
        top.geometry("750x525+200+180")
        f = Frame(top, width=750,height=750, bg="black")
        f.pack()
        self.img5 = ImageTk.PhotoImage(Image.open("fuctions2 (1).jpg"))
        self.img2 = ImageTk.PhotoImage(Image.open("functions3(1).jpg"))
        self.img3 = ImageTk.PhotoImage(Image.open("functions4(1).jpg"))
        self.img4 = ImageTk.PhotoImage(Image.open("functions5(1).jpg"))
        label = Label(f, image=self.img5)
        label.grid(row=0, column=0, padx=20, pady=10)
        label2 = Label(f, image=self.img2)
        label2.grid(row=0, column=1, padx=20, pady=10)
        label3 = Label(f, image=self.img3)
        label3.grid(row=1, column=0, padx=20, pady=10)
        label4 = Label(f, image=self.img4)
        label4.grid(row=1, column=1, padx=20, pady=10)
        f.grid_propagate(0)

    def payment(self,top):
        amount = int(self.e1.get())
        cvv = self.e3.get()
        cardno = self.e2.get()
        month = self.e4.get()
        if (amount == "" or cvv == "" or cardno == "" or month == ""):
            messagebox.showwarning("Mandatory fields", "Please fill all the fields")
            top.focus_set()
        else:
            query = "Insert into  Maintainance(AdmintId,Amount,AsOfMonth) Values ('%d','%d','%s')"
            args = (self.details[0],amount, month)
            DatabaseHelper.execute_query(query % args)
            top.destroy()
            query ="Update Maintainance Set IsPaid=1 where AdmintId=%d"
            args= (self.details[0])
            DatabaseHelper.execute_query(query % args)
            messagebox.showinfo("Success", "Successfully paid")

    def record(self):
            wind1 = Toplevel()
            wind1.geometry("800x500+200+100")
            fram1 = Frame(wind1, width=800, height=500, bg="white")
            fram1.pack()
            query = "Select * from maintainance m join Admint a on m.AdmintId=a.AdmintId"
            result = DatabaseHelper.get_all_data(query)
            print(result)
            rc1 = Label(fram1, text="ADMINID", width=15, height=1, bg="light blue")
            rc1.grid(row=0, column=0, padx=5, pady=8)
            rc2 = Label(fram1, text="Amount", width=15, height=1, bg="light blue")
            rc2.grid(row=0, column=1, padx=5, pady=8)
            rc3 = Label(fram1, text="Month", width=15, height=1, bg="light blue")
            rc3.grid(row=0, column=2, padx=5, pady=8)
            rc4 = Label(fram1, text="Email-ID", width=35, height=1, bg="light blue")
            rc4.grid(row=0, column=3, padx=5, pady=8)
            rc5 = Label(fram1, text="Ispaid", width=15, height=1, bg="light blue")
            rc5.grid(row=0, column=4, padx=5, pady=8)
            fram1.grid_propagate(0)
            color = ['light blue', 'light grey']
            for i in range(len(result)):
                temp = result[i]
                Label(fram1, text=temp[1], width=15, height=1, bg=color[(i + 1) % 2]).grid(row=i + 1, column=0)
                Label(fram1, text=temp[2], width=15, height=1, bg=color[(i + 1) % 2]).grid(row=i + 1, column=1)
                Label(fram1, text=temp[3], width=15, height=1, bg=color[(i + 1) % 2]).grid(row=i + 1, column=2)
                Label(fram1, text=temp[8], width=35, height=1, bg=color[(i + 1) % 2]).grid(row=i + 1, column=3)
                Label(fram1, text="1", width=15, height=1, bg=color[(i + 1) % 2]).grid(row=i + 1, column=4)

    def pay(self):
        top = Toplevel()
        top.geometry("500x280+300+180")
        fr = Frame(top, width=500, height=500, bg="light yellow")
        fr.pack()
        l1 = Label(fr, text="Amount:", bg="light yellow", width=15, height=2)
        l1.place(x=17, y=20)
        self.e1 = Entry(fr, width=15)
        self.e1.place(x=100, y=30)
        l2 = Label(fr, text="Card No:", bg="light yellow", width=15, height=2)
        l2.place(x=17, y=60)
        self.e2 = Entry(fr, width=30)
        self.e2.place(x=100, y=70)
        l3 = Label(fr, text="CVV:", bg="light yellow", width=15, height=2)
        l3.place(x=17, y=100)
        self.e3 = Entry(fr, width=10)
        self.e3.place(x=100, y=110)
        l4 = Label(fr, text="Month:", bg="light yellow", width=15, height=2)
        l4.place(x=17, y=130)
        self.e4 = Entry(fr, width=20)
        self.e4.place(x=100, y=140)
        b = Button(fr, text="Pay", bg="thistle2", width=10, height=1, command=lambda:self.payment(top))
        b.place(x=230, y=190)



    def About(self):
        top = Toplevel()
        top.geometry("800x400+188+195")
        f = Frame(top, width=800, height=400, bg="black")
        f.pack()
        str = """> Before starting any civil work, carpentry, painting, renovation etc in their flats every member of the society needs to take proper permission of the committee. In case if anyone doesn’t follow this rule then he/she shall abide to pay certain amount of penalty.
    > Penalties are applied against the damaged caused while shifting the household goods in lifts, corridors, garden areas etc by any member of the society.
    > No member can occupy the area near their front doors, corridors, passage for their personal usage.
    > Every member of the society should park their vehicles in their respective allotted parking spaces only. If any illegal parking is done, then that person may cost a penalty for his mistake. Two wheelers should be parked separately. Only one or two vehicles of visitors or guests per flat are allowed to be parked in the premises of the apartment. Other vehicles are supposed to be parked out of the society’s boundary line.
    > Salesmen, vendors or any other sellers are not allowed to enter the premises. Owners residing are not allowed to rent their flats for any commercial use as this might create trouble to other society members.
    > After using the community hall for any event or function it should be cleaned and no damages should be caused. If any damage is cause strict action against the owner will be taken. Music systems should be played inside of the flats with low volume only.
    > Cricket, basket ball, badminton, football should be played only on the respective grounds. No children’s are allowed to play in the lobby area. In case of any property damage by the kid’s respective person or parents are held to be responsible.
    > Wastage and over usage of water is not allowed. Flat owners will be considered responsible for this act and they have to pay the penalty costs for the same.
    > Maintenance charges should be paid from to time. If failed after multiple warnings, any legal action can be processed against the respective person.
    > Smoking in lobbies, passage is not allowed. If any irresponsible person is found smoking in the no smoking zone, he/she shall be charged with penalty."""
        m = Message(f, width=700, text=str, fg="black", bg="white")
        m.place(x=50, y=50)

if __name__ == '__main__':
    root=Tk()
    result = (2,)
    p=Page3(root,result)
    root.mainloop()
