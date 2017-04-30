from Tkinter import *

class Slider(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master =  master
    def setupGUI(self):
        img1 = PhotoImage(file="test tile.gif")
        b1 = Button(self.master, width=50, height=50)
        b1.config(image=img1)
        b1.image = img1
        b1.place(x=0,y=0)
        
        b2 = Button(self.master, width=50, height=50)
        b2.config(image=img1)
        b2.image = img1
        b2.place(x=0,y=55)
        
        b3 = Button(self.master, width=50, height=50)
        b3.config(image=img1)
        b3.image = img1
        b3.place(x=55,y=0)
        
        b4 = Button(self.master, width=50, height=50)
        b4.config(image=img1)
        b4.image = img1
        b4.place(x=55,y=55)

        b5 = Button(self.master, width=50, height=50)
        b5.config(image=img1)
        b5.image = img1
        b5.place(x=110,y=0)

window = Tk()
t = Slider(window)
t.setupGUI()
window.mainloop()
