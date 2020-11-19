from tkinter import *
from PIL import ImageTk,Image

class Default:
    def __init__(self,root):
        self.root=root
        self.root.title("Society Management System")
        self.frame=Frame(self.root,width=1000,height=625)
        self.frame.pack()
        self.building_background=ImageTk.PhotoImage(Image.open("pic1r.jpg"))
        self.label=Label(self.frame,image=self.building_background)
        self.label.pack()
        self.msg=Message(self.frame,width=700,font="Fixedsys 20 bold italic",text="ELEGANT TOWER",bg="midnight blue",fg="plum1",highlightcolor="blue",borderwidth=2)
        self.msg.place(x=600,y=20)


#root=Tk()
#d=Default(root)

#root.mainloop()