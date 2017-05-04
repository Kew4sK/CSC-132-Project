from Tkinter import *

class Slider(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master =  master
        self.grid
    def setupGUI(self):
        img1 = PhotoImage(file="test tile.gif")
        b1 = Button(self.master, width=50, height=50, command=lambda : remove())
        b1.config(image=img1)
        b1.image = img1
        b1.grid(row=0, column=0)
        
        b2 = Button(self.master, width=50, height=50)
        b2.config(image=img1)
        b2.image = img1
        b2.grid(row=1, column=0)
        
        b3 = Button(self.master, width=50, height=50)
        b3.config(image=img1)
        b3.image = img1
        b3.grid(row=0, column=1)
        
        b4 = Button(self.master, width=50, height=50)
        b4.config(image=img1)
        b4.image = img1
        b4.grid(row=1, column=1)

        b5 = Button(self.master, width=50, height=50)
        b5.config(image=img1)
        b5.image = img1
        b5.grid(row=2, column=0)

        b6 = Button(self.master, width=50, height=50)
        b6.config(image=img1)
        b6.image = img1
        b6.grid(row=0, column=2)

        b7 = Button(self.master, width=50, height=50)
        b7.config(image=img1)
        b7.image = img1
        b7.grid(row=2, column=1)

        b8 = Button(self.master, width=50, height=50)
        b8.config(image=img1)
        b8.image = img1
        b8.grid(row=1, column=2)

        b9 = Button(self.master, width=50, height=50)
        b9.config(image=img1)
        b9.image = img1
        b9.grid(row=2, column=2)

        b10 = Button(self.master, width=50, height=50)
        b10.config(image=img1)
        b10.image = img1
        b10.grid(row=3, column=0)

        b11 = Button(self.master, width=50, height=50)
        b11.config(image=img1)
        b11.image = img1
        b11.grid(row=0, column=3)

        b12 = Button(self.master, width=50, height=50)
        b12.config(image=img1)
        b12.image = img1
        b12.grid(row=3, column=1)

        b13 = Button(self.master, width=50, height=50)
        b13.config(image=img1)
        b13.image = img1
        b13.grid(row=3, column=2)

        b14 = Button(self.master, width=50, height=50)
        b14.config(image=img1)
        b14.image = img1
        b14.grid(row=1, column=3) 
        
        b15 = Button(self.master, width=50, height=50)
        b15.config(image=img1)
        b15.image = img1
        b15.grid(row=2, column=3)

        b16 = Button(self.master, width=50, height=50)
        b16.config(image=img1)
        b16.image = img1
        b16.grid(row=3, column=3)

        b17 = Button(self.master, width=50, height=50)
        b17.config(image=img1)
        b17.image = img1
        b17.grid(row=4, column=0)

        b18 = Button(self.master, width=50, height=50)
        b18.config(image=img1)
        b18.image = img1
        b18.grid(row=0, column=4)

        b19 = Button(self.master, width=50, height=50)
        b19.config(image=img1)
        b19.image = img1
        b19.grid(row=4, column=1)

        b20 = Button(self.master, width=50, height=50)
        b20.config(image=img1)
        b20.image = img1
        b20.grid(row=4, column=2)

        b21 = Button(self.master, width=50, height=50)
        b21.config(image=img1)
        b21.image = img1
        b21.grid(row=4, column=3)

        b22 = Button(self.master, width=50, height=50)
        b22.config(image=img1)
        b22.image = img1
        b22.grid(row=3, column=4)

        b23 = Button(self.master, width=50, height=50)
        b23.config(image=img1)
        b23.image = img1
        b23.grid(row=2, column=4)

        b24 = Button(self.master, width=50, height=50)
        b24.config(image=img1)
        b24.image = img1
        b24.grid(row=1, column=4)

WIDTH = 275
HEIGHT = 275
window = Tk()
window.geometry("{}x{}".format(WIDTH, HEIGHT))
window.title("Slider Puzzle")
t = Slider(window)
t.setupGUI()
window.mainloop()
