from Tkinter import *
root = Tk()#initlize
frame = Frame(root, width=300, height=300)
frame.pack()


userInputH = StringVar()#Height Stuff
heightLabel=Label(root,text="Height")
heightLabel.pack()
heightLabel.place(x=20,y=150)
height = Entry(root, text="Black", fg="black",textvariable=userInputH)
height.place(x=60,y=150)

userInputW = StringVar()#width
widthLabel=Label(root,text="Width")
widthLabel.place(x=20,y=100)
width = Entry(root, text="Black", fg="black",textvariable=userInputW)
width.place(x=60,y=100)

userInputP = StringVar()#picture box
pictureLabel=Label(root,text="Picture File")
pictureLabel.place(x=20,y=20)
picture = Entry(root, text="Black", fg="black",textvariable=userInputP)
picture.place(x=90,y=20)

#get resolution button
def getResolution():
    userInputP.get()
    resolution =0
    resolutionLabel=Label(root,text="Resolution: "+str(resolution))
    resolutionLabel.pack()
    resolutionLabel.place(x=150,y=60)
getResolution= Button(root, text ="Get Resolution", command = getResolution)
getResolution.pack()
getResolution.place(x=30,y=60)

#drawPciture button
def drawPicture():
   userInputH.get()
   userInputW.get()
   userInputP.get()

drawPicture = Button(root, text ="Draw picture", command = drawPicture)
drawPicture.pack()
drawPicture.place(x=75,y=200)

root.mainloop()#drawn

#userInput = stringVar()
#userEntry = Entry(master, variable=userInput) #creates an entry box
#userInput.get() # returns what is in the entry box
