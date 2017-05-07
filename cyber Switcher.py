from Tkinter import *
import time

class Slider(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master =  master
        self.grid
        self.empty_spot = (4, 4)
# checks if each combination was clicked and switches them, but only with their starting location that isnt random.
    def check(self):
        print "nope"
        if (a == 1 and b == 1):
            print "finally"
            
            aa = b1.grid_info()
            row1 = aa["row"]
            column1 = aa["column"]
            
            bb = b2.grid_info()
            row2 = bb["row"]
            column2 = bb["column"]
            b1.grid(row=row2, column=column2)
            b2.grid(row=row1, column=column1)
            
    def grid(self, z):
        grid_info = z.grid_info()
        print ("row:", grid_info["row"], "column:", grid_info["column"])
        print grid_info["column"]

# each of these (a through y) controll if a button was selected.
    def a(self, value):
        global a
        a = value
        self.check()

    def b(self, value):
        global b
        b = value
        self.check()

    def setupGUI(self):            
        global switch, img1, img2, b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16, b18, b19, b20, b21, b22, b23, b24, b25
#imports images.
        img1 = PhotoImage(file="test tile.gif")
        img2 = PhotoImage(file="test.gif")

        #switch = PhotoImage(file="Switch.gif")
#Places the buttons in there spots on the grid.
#Each one needs to be assigned a command still.
        b1 = Button(self.master, width=50, height=50, command=lambda *args: self.a(1))
        b1.config(image=img1)
        b1.grid(row=0, column=0)
        
        b2 = Button(self.master, width=50, height=50, command=lambda *args: self.b(1))
        b2.config(image=img1)
        b2.grid(row=1, column=0)
        
        b3 = Button(self.master, width=50, height=50)
        b3.config(image=img1)
        b3.grid(row=0, column=1)
        
        b4 = Button(self.master, width=50, height=50)
        b4.config(image=img1)
        b4.grid(row=1, column=1)

        b5 = Button(self.master, width=50, height=50)
        b5.config(image=img1)
        b5.grid(row=2, column=0)

        b6 = Button(self.master, width=50, height=50)
        b6.config(image=img1)
        b6.grid(row=0, column=2)

        b7 = Button(self.master, width=50, height=50)
        b7.config(image=img1)
        b7.grid(row=2, column=1)

        b8 = Button(self.master, width=50, height=50)
        b8.config(image=img1)
        b8.grid(row=1, column=2)

        b9 = Button(self.master, width=50, height=50)
        b9.config(image=img1)
        b9.grid(row=2, column=2)

        b10 = Button(self.master, width=50, height=50)
        b10.config(image=img1)
        b10.grid(row=3, column=0)

        b11 = Button(self.master, width=50, height=50)
        b11.config(image=img1)
        b11.grid(row=0, column=3)

        b12 = Button(self.master, width=50, height=50)
        b12.config(image=img1)
        b12.grid(row=3, column=1)

        b13 = Button(self.master, width=50, height=50)
        b13.config(image=img1)
        b13.grid(row=3, column=2)

        b14 = Button(self.master, width=50, height=50)
        b14.config(image=img1)
        b14.grid(row=1, column=3) 
        
        b15 = Button(self.master, width=50, height=50)
        b15.config(image=img1)
        b15.grid(row=2, column=3)

        b16 = Button(self.master, width=50, height=50)
        b16.config(image=img1)
        b16.grid(row=3, column=3)

        b17 = Button(self.master, width=50, height=50)
        b17.config(image=img1)
        b17.grid(row=4, column=0)

        b18 = Button(self.master, width=50, height=50)
        b18.config(image=img1)
        b18.grid(row=0, column=4)

        b19 = Button(self.master, width=50, height=50)
        b19.config(image=img1)
        b19.grid(row=4, column=1)

        b20 = Button(self.master, width=50, height=50)
        b20.config(image=img1)
        b20.grid(row=4, column=2)

        b21 = Button(self.master, width=50, height=50)
        b21.config(image=img1)
        b21.grid(row=4, column=3)

        b22 = Button(self.master, width=50, height=50)
        b22.config(image=img1)
        b22.grid(row=3, column=4)

        b23 = Button(self.master, width=50, height=50)
        b23.config(image=img1)
        b23.grid(row=2, column=4)

        b24 = Button(self.master, width=50, height=50)
        b24.config(image=img1)
        b24.grid(row=1, column=4)

        b25 = Button(self.master, width=50, height=50)
        b25.config(image=img2)
        b25.grid(row=4, column=4)

        #b26 = Button(self.master, width=50, height=50, command=lambda : self.check())
        #b26.config(image=switch)
        #b26.grid(row=5, column=5)

        


###################################################################################
WIDTH = 280
HEIGHT = 280
window = Tk()
window.geometry("{}x{}".format(WIDTH, HEIGHT))
window.title("Slider Puzzle")
t = Slider(window)
t.setupGUI()
window.mainloop()

