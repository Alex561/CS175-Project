from Tkinter import *
root = Tk()#initlize


heightLabel=Label(root,text="Height")
heightLabel.pack()
heightLabel.place(x=20,y=150)
height = Entry(root, text="Black", fg="black")
height.place(x=60,y=150)

widthLabel=Label(root,text="Width")
widthLabel.place(x=20,y=100)
width = Entry(root, text="Black", fg="black")
width.place(x=60,y=100)

widthLabel=Label(root,text="Picture File")
widthLabel.place(x=65,y=30)
width = Entry(root, text="Black", fg="black")
width.place(x=40,y=50)

root.mainloop()
