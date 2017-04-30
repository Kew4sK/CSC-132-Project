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

        b6 = Button(self.master, width=50, height=50)
        b6.config(image=img1)
        b6.image = img1
        b6.place(x=0,y=110)

        b7 = Button(self.master, width=50, height=50)
        b7.config(image=img1)
        b7.image = img1
        b7.place(x=110,y=55)

        b8 = Button(self.master, width=50, height=50)
        b8.config(image=img1)
        b8.image = img1
        b8.place(x=55,y=110)

        b9 = Button(self.master, width=50, height=50)
        b9.config(image=img1)
        b9.image = img1
        b9.place(x=110,y=110)

        b10 = Button(self.master, width=50, height=50)
        b10.config(image=img1)
        b10.image = img1
        b10.place(x=0,y=165)

        b11 = Button(self.master, width=50, height=50)
        b11.config(image=img1)
        b11.image = img1
        b11.place(x=165,y=0)

        b12 = Button(self.master, width=50, height=50)
        b12.config(image=img1)
        b12.image = img1
        b12.place(x=55,y=165)

        b13 = Button(self.master, width=50, height=50)
        b13.config(image=img1)
        b13.image = img1
        b13.place(x=165,y=55)

        b14 = Button(self.master, width=50, height=50)
        b14.config(image=img1)
        b14.image = img1
        b14.place(x=110,y=165)
        
        b15 = Button(self.master, width=50, height=50)
        b15.config(image=img1)
        b15.image = img1
        b15.place(x=165,y=110)

        b16 = Button(self.master, width=50, height=50)
        b16.config(image=img1)
        b16.image = img1
        b16.place(x=165,y=165)

        b17 = Button(self.master, width=50, height=50)
        b17.config(image=img1)
        b17.image = img1
        b17.place(x=0,y=220)

        b18 = Button(self.master, width=50, height=50)
        b18.config(image=img1)
        b18.image = img1
        b18.place(x=220,y=0)

        b19 = Button(self.master, width=50, height=50)
        b19.config(image=img1)
        b19.image = img1
        b19.place(x=55,y=220)

        b20 = Button(self.master, width=50, height=50)
        b20.config(image=img1)
        b20.image = img1
        b20.place(x=220,y=55)

        b21 = Button(self.master, width=50, height=50)
        b21.config(image=img1)
        b21.image = img1
        b21.place(x=110,y=220)

        b22 = Button(self.master, width=50, height=50)
        b22.config(image=img1)
        b22.image = img1
        b22.place(x=220,y=110)

        b23 = Button(self.master, width=50, height=50)
        b23.config(image=img1)
        b23.image = img1
        b23.place(x=165,y=220)

        b24 = Button(self.master, width=50, height=50)
        b24.config(image=img1)
        b24.image = img1
        b24.place(x=220,y=165)

WIDTH = 275
HEIGHT = 275
window = Tk()
window.geometry("{}x{}".format(WIDTH, HEIGHT))
window.title("Slider Puzzle")
t = Slider(window)
t.setupGUI()
window.mainloop()
