from Tkinter import *
import time


class Slider(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master =  master
        self.grid
        
# checks if each combination was clicked and switches them, but only with their starting location that isnt random.
    def check(self):
            aa = a.grid_info()
            row1 = aa["row"]
            column1 = aa["column"]
            
            bb = b.grid_info()
            row2 = bb["row"]
            column2 = bb["column"]
            a.grid(row=row2, column=column2)
            b.grid(row=row1, column=column1)

# each of these (a through y) controll if a button was selected.<- (before hand)
#not the best user of global variables
#click1 is set to 0, and the first button passed in will be set to a, then click1 is incremented by 1
#when click1 is 1, the button passed in will be set to be, and the check function above will be activated
#note that it appears, when a and b are set to the button passed in (value), the button is also set to a and b.
#this means that whatever happens to the variable a and b happens to their respective buttons apparently???
    def a(self, value):
        global click1

        if (click1 == 0):
            global a
            a = value
            click1 += 1

        elif (click1 == 1):
            global b
            b = value
            click1 = 0
            self.check()

    def setupGUI(self):            
        global click1, img1, img2, b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16, b18, b19, b20, b21, b22, b23, b24, b25
#imports images.
        img1 = PhotoImage(file="test tile.gif")
        img2 = PhotoImage(file="test.gif")
        click1 = 0
#Places the buttons in there spots on the grid.
#Each one needs to be assigned a command still.
#Each variable will call the same function when clicked (the "a" function). This will be fixed with the click1 variable.
        b1 = Button(self.master, width=50, height=50, command=lambda *args: self.a(b1))
        b1.config(image=img2)
        b1.grid(row=0, column=0)
        
        b2 = Button(self.master, width=50, height=50, command=lambda *args: self.a(b2))
        b2.config(image=img1)
        b2.grid(row=1, column=0)
        
        b3 = Button(self.master, width=50, height=50, command=lambda *args: self.a(b3))
        b3.config(image=img1)
        b3.grid(row=0, column=1)
        
        b4 = Button(self.master, width=50, height=50, command=lambda *args: self.a(b4))
        b4.config(image=img1)
        b4.grid(row=1, column=1)

        b5 = Button(self.master, width=50, height=50, command=lambda *args: self.a(b5))
        b5.config(image=img1)
        b5.grid(row=2, column=0)

        b6 = Button(self.master, width=50, height=50, command=lambda *args: self.a(b6))
        b6.config(image=img1)
        b6.grid(row=0, column=2)

        b7 = Button(self.master, width=50, height=50, command=lambda *args: self.a(b7))
        b7.config(image=img1)
        b7.grid(row=2, column=1)

        b8 = Button(self.master, width=50, height=50, command=lambda *args: self.a(b8))
        b8.config(image=img1)
        b8.grid(row=1, column=2)

        b9 = Button(self.master, width=50, height=50, command=lambda *args: self.a(b9))
        b9.config(image=img1)
        b9.grid(row=2, column=2)

        b10 = Button(self.master, width=50, height=50, command=lambda *args: self.a(b10))
        b10.config(image=img1)
        b10.grid(row=3, column=0)

        b11 = Button(self.master, width=50, height=50, command=lambda *args: self.a(b11))
        b11.config(image=img1)
        b11.grid(row=0, column=3)

        b12 = Button(self.master, width=50, height=50, command=lambda *args: self.a(b12))
        b12.config(image=img1)
        b12.grid(row=3, column=1)

        b13 = Button(self.master, width=50, height=50, command=lambda *args: self.a(b13))
        b13.config(image=img1)
        b13.grid(row=3, column=2)

        b14 = Button(self.master, width=50, height=50, command=lambda *args: self.a(b14))
        b14.config(image=img1)
        b14.grid(row=1, column=3) 
        
        b15 = Button(self.master, width=50, height=50, command=lambda *args: self.a(b15))
        b15.config(image=img1)
        b15.grid(row=2, column=3)

        b16 = Button(self.master, width=50, height=50, command=lambda *args: self.a(b16))
        b16.config(image=img1)
        b16.grid(row=3, column=3)

        b17 = Button(self.master, width=50, height=50, command=lambda *args: self.a(b17))
        b17.config(image=img1)
        b17.grid(row=4, column=0)

        b18 = Button(self.master, width=50, height=50, command=lambda *args: self.a(b18))
        b18.config(image=img1)
        b18.grid(row=0, column=4)

        b19 = Button(self.master, width=50, height=50, command=lambda *args: self.a(b19))
        b19.config(image=img1)
        b19.grid(row=4, column=1)

        b20 = Button(self.master, width=50, height=50, command=lambda *args: self.a(b20))
        b20.config(image=img1)
        b20.grid(row=4, column=2)

        b21 = Button(self.master, width=50, height=50, command=lambda *args: self.a(b21))
        b21.config(image=img1)
        b21.grid(row=4, column=3)

        b22 = Button(self.master, width=50, height=50, command=lambda *args: self.a(b22))
        b22.config(image=img1)
        b22.grid(row=3, column=4)

        b23 = Button(self.master, width=50, height=50, command=lambda *args: self.a(b23))
        b23.config(image=img1)
        b23.grid(row=2, column=4)

        b24 = Button(self.master, width=50, height=50, command=lambda *args: self.a(b24))
        b24.config(image=img1)
        b24.grid(row=1, column=4)

        b25 = Button(self.master, width=50, height=50, command=lambda *args: self.a(b25))
        b25.config(image=img2)
        b25.grid(row=4, column=4)

######################################################################################
WIDTH = 340
HEIGHT = 340
window = Tk()
window.geometry("{}x{}".format(WIDTH, HEIGHT))
window.title("Slider Puzzle")
t = Slider(window)
t.setupGUI()
window.mainloop()
