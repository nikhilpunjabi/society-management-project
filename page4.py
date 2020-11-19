from tkinter import *
from PIL import ImageTk,Image

from database import *


class Page4:
    def __init__(self,root,result):
        self.root=root
        self.frame = Frame(self.root,width=1000,height=625,bg="white")
        self.frame. pack()
        self.img1 = ImageTk.PhotoImage(Image.open("wallr.jpg"))
        self.lab2 = Label(self.frame, width=1000, height=625, image=self.img1)
        self.lab2.pack()
        self.c1=Canvas(self.frame,width=1000,height=50,bg="black")
        self.c1.place(x=0,y=10)
        self.b1=Button(self.c1,text="Logout",bg="black",fg="white",width=6,height=2,relief=FLAT,command=lambda:self.logout(self.root))
        self.b1.place(x=940,y=5)
        self.b2 = Button(self.c1, text="Entry Details", bg="black", fg="white", width=18, height=2, relief=FLAT,command=self.entryw)
        self.b2.place(x=25, y=5)
        self.b4 = Button(self.c1, text="About!", bg="black", fg="white", width=6, height=2, relief=FLAT,command=self.About)
        self.b4.place(x=170, y=5)
        self.la5=Label(self.lab2,text="Name :",width=7,height=1)
        self.la5.place(x=700,y=100)
        self.ea5=Entry(self.lab2,width=15)
        self.ea5.place(x=790,y=100)
        self.la1=Label(self.lab2,width=10,height=1,text="TIME IN :")
        self.la1.place(x=700,y=150)
        self.ea1=Entry(self.lab2,width=15)
        self.ea1.place(x=790,y=150)
        self.la2 = Label(self.lab2, width=10, height=1, text="TIME OUT :")
        self.la2.place(x=700, y=200)
        self.ea2 = Entry(self.lab2, width=15)
        self.ea2.place(x=790, y=200)
        self.la3= Label(self.lab2, width=10, height=1, text="REASON :")
        self.la3.place(x=700, y=250)
        self.ea3=Entry(self.lab2,width=30)
        self.ea3.place(x=790,y=250)
        self.la4 = Label(self.lab2, width=10, height=1, text="CONTACT :")
        self.la4.place(x=700, y=310)
        self.ea4 = Entry(self.lab2, width=25)
        self.ea4.place(x=790, y=310)
        self.ba1=Button(self.lab2,text="OK",width=5,height=1,relief=GROOVE,bg="light blue",command=lambda:self.ok(self.root))
        self.ba1.place(x=820,y=350)


    def entryw(self):

        wind=Toplevel()
        wind.geometry("610x650+200+100")
        fram=Frame(wind,width=610,height=650,bg="white")
        fram.pack()
        query="SELECT * from Entry"
        result=DatabaseHelper.get_all_data(query)
        print(result)
        mk1=Label(fram,text="Name",width=15,height=1,bg="light blue")
        mk1.grid(row=0,column=0,padx=5,pady=8)
        mk2 = Label(fram, text="Time In", width=15, height=1,bg="light blue")
        mk2.grid(row=0, column=1,padx=5,pady=8)
        mk3 = Label(fram, text="Time Out", width=15, height=1,bg="light blue")
        mk3.grid(row=0, column=2,padx=5,pady=8)
        mk4 = Label(fram, text="Reason", width=15, height=1,bg="light blue")
        mk4.grid(row=0, column=3,padx=5,pady=8)
        mk5 = Label(fram, text="Contact", width=15, height=1,bg="light blue")
        mk5.grid(row=0, column=4,padx=5,pady=8)
        fram.grid_propagate(0)
        color=['light blue','light grey']
        for i in range(len(result)):
            temp=result[i]
            Label(fram, text=temp[5], width=15, height=1,bg=color[(i+1)%2]).grid(row= i+1,column=0)
            Label(fram, text=temp[1], width=15, height=1,bg=color[(i+1)%2]).grid(row=i+1, column=1)
            Label(fram, text=temp[2], width=15, height=1,bg=color[(i+1)%2]).grid(row=i+1, column=2)
            Label(fram, text=temp[3], width=15, height=1,bg=color[(i+1)%2]).grid(row=i+1, column=3)
            Label(fram, text=temp[4], width=15, height=1,bg=color[(i+1)%2]).grid(row=i+1, column=4)

    def ok(self,root):
        t1=self.ea1.get()
        t2=self.ea2.get()
        r1=self.ea3.get()
        cn=self.ea4.get()
        nam=self.ea5.get()

        self.ea1.delete(0,END)
        self.ea2.delete(0, END)
        self.ea3.delete(0, END)
        self.ea4.delete(0, END)
        self.ea5.delete(0, END)




        query = "Insert into Entry(timein,timeout,Reason,contact,name1) Values ('%s','%s','%s','%s','%s')"
        args = (t1,t2,r1,cn,nam)
        print(args)
        DatabaseHelper.execute_query(query % args)





    def logout(self,root):
        #self.root.destroy()
        self.frame.destroy()
        import page1
        page1.Page1(self.root)
        print("Page 4 logout is called and window destroyed")



    def About(self):
        top = Toplevel()
        top.geometry("800x400+188+195")
        f = Frame(top, width=800, height=400, bg="black")
        f.pack()
        str = """>Before starting any civil work, carpentry, painting, renovation etc in their flats every member of the society needs to take proper permission of the committee. In case if anyone doesn’t follow this rule then he/she shall abide to pay certain amount of penalty.
    >Penalties are applied against the damaged caused while shifting the household goods in lifts, corridors, garden areas etc by any member of the society.
    >No member can occupy the area near their front doors, corridors, passage for their personal usage.
    >Every member of the society should park their vehicles in their respective allotted parking spaces only. If any illegal parking is done, then that person may cost a penalty for his mistake. Two wheelers should be parked separately. Only one or two vehicles of visitors or guests per flat are allowed to be parked in the premises of the apartment. Other vehicles are supposed to be parked out of the society’s boundary line.
    >Salesmen, vendors or any other sellers are not allowed to enter the premises. Owners residing are not allowed to rent their flats for any commercial use as this might create trouble to other society members.
    >After using the community hall for any event or function it should be cleaned and no damages should be caused. If any damage is cause strict action against the owner will be taken. Music systems should be played inside of the flats with low volume only.
    >Cricket, basket ball, badminton, football should be played only on the respective grounds. No children’s are allowed to play in the lobby area. In case of any property damage by the kid’s respective person or parents are held to be responsible.
    >Wastage and over usage of water is not allowed. Flat owners will be considered responsible for this act and they have to pay the penalty costs for the same.
    >Maintenance charges should be paid from to time. If failed after multiple warnings, any legal action can be processed against the respective person.
    >Smoking in lobbies, passage is not allowed. If any irresponsible person is found smoking in the no smoking zone, he/she shall be charged with penalty."""
        m = Message(f, width=700, text=str, fg="black", bg="white")
        m.place(x=50, y=50)



if __name__ == '__main__':
    root=Tk()
    result = (2,)
    p=Page4(root,result)
    root.mainloop()





