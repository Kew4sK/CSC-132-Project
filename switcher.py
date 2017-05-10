from Tkinter import *
import time
from random import randint


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

        elif (click1 == 1 and a != value):      #also covers double clicks
            global b
            b = value
            click1 = 0
            self.check()

#This function randomizes two lists: one called "rows" and the other "columns"

    def buildGrid(self):
        rows = []       
        #will continue until the length of the list is 5
        while (len(rows) < 5):
            number = randint(0,4)
            found = 0
#If the number is already in the list, the "found" variable will be set to 1, and the number will not be re-added to the list
            for n in range(len(rows)):
                if (number == rows[n]):
                    found = 1

            if (found == 0):
                rows.append(number)

        columns = []
        while (len(columns) < 5):
            number = randint(0,4)
            found = 0

            for n in range(len(columns)):
                if (number == columns[n]):
                    found = 1

            if (found == 0):
                columns.append(number)

        global rows, columns


    def setupGUI(self):            
        global click1, b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16, b18, b19, b20, b21, b22, b23, b24, b25
        global  i1, i2, i3 ,i4, i5, i6, i7, i8, i9, i10, i11, i12, i13, i14, i15, i16, i17, i18, i19, i20, i21, i22, i23, i24, i25
        self.buildGrid()
#imports images.
        i1 = PhotoImage(file="1.gif")
        i2 = PhotoImage(file="2.gif")
        i3 = PhotoImage(file="3.gif")
        i4 = PhotoImage(file="4.gif")
        i5 = PhotoImage(file="5.gif")
        i6 = PhotoImage(file="6.gif")
        i7 = PhotoImage(file="7.gif")
        i8 = PhotoImage(file="8.gif")
        i9 = PhotoImage(file="9.gif")
        i10 = PhotoImage(file="10.gif")
        i11 = PhotoImage(file="11.gif")
        i12 = PhotoImage(file="12.gif")
        i13 = PhotoImage(file="13.gif")
        i14 = PhotoImage(file="14.gif")
        i15 = PhotoImage(file="15.gif")
        i16 = PhotoImage(file="16.gif")
        i17 = PhotoImage(file="17.gif")
        i18 = PhotoImage(file="18.gif")
        i19 = PhotoImage(file="19.gif")
        i20 = PhotoImage(file="20.gif")
        i21 = PhotoImage(file="21.gif")
        i22 = PhotoImage(file="22.gif")
        i23 = PhotoImage(file="23.gif")
        i24 = PhotoImage(file="24.gif")
        i25 = PhotoImage(file="25.gif")
        click1 = 0
#Places the buttons in there spots on the grid.
#Each one needs to be assigned a command still.
#Each variable will call the same function when clicked (the "a" function). This will be fixed with the click1 variable.
        b1 = Button(self.master, highlightthickness=0, bd=0, width=100, height=100, command=lambda *args: self.a(b1))
        b1.config(image=i1)
        b1.grid(row=rows[0], column=columns[0])
        
        b2 = Button(self.master, highlightthickness=0, bd=0, width=100, height=100, command=lambda *args: self.a(b2))
        b2.config(image=i2)
        b2.grid(row=rows[1], column=columns[0])
        
        b3 = Button(self.master, highlightthickness=0, bd=0, width=100, height=100, command=lambda *args: self.a(b3))
        b3.config(image=i3)
        b3.grid(row=rows[0], column=columns[1])
        
        b4 = Button(self.master, highlightthickness=0, bd=0, width=100, height=100, command=lambda *args: self.a(b4))
        b4.config(image=i4)
        b4.grid(row=rows[1], column=columns[1])

        b5 = Button(self.master, highlightthickness=0, bd=0, width=100, height=100, command=lambda *args: self.a(b5))
        b5.config(image=i5)
        b5.grid(row=rows[2], column=columns[0])

        b6 = Button(self.master, highlightthickness=0, bd=0, width=100, height=100, command=lambda *args: self.a(b6))
        b6.config(image=i6)
        b6.grid(row=rows[0], column=columns[2])

        b7 = Button(self.master, highlightthickness=0, bd=0, width=100, height=100, command=lambda *args: self.a(b7))
        b7.config(image=i7)
        b7.grid(row=rows[2], column=columns[1])

        b8 = Button(self.master, highlightthickness=0, bd=0, width=100, height=100, command=lambda *args: self.a(b8))
        b8.config(image=i8)
        b8.grid(row=rows[1], column=columns[2])

        b9 = Button(self.master, highlightthickness=0, bd=0, width=100, height=100, command=lambda *args: self.a(b9))
        b9.config(image=i9)
        b9.grid(row=rows[2], column=columns[2])

        b10 = Button(self.master, highlightthickness=0, bd=0, width=100, height=100, command=lambda *args: self.a(b10))
        b10.config(image=i10)
        b10.grid(row=rows[3], column=columns[0])

        b11 = Button(self.master, highlightthickness=0, bd=0, width=100, height=100, command=lambda *args: self.a(b11))
        b11.config(image=i11)
        b11.grid(row=rows[0], column=columns[3])

        b12 = Button(self.master, highlightthickness=0, bd=0, width=100, height=100, command=lambda *args: self.a(b12))
        b12.config(image=i12)
        b12.grid(row=rows[3], column=columns[1])

        b13 = Button(self.master, highlightthickness=0, bd=0, width=100, height=100, command=lambda *args: self.a(b13))
        b13.config(image=i13)
        b13.grid(row=rows[3], column=columns[2])

        b14 = Button(self.master, highlightthickness=0, bd=0, width=100, height=100, command=lambda *args: self.a(b14))
        b14.config(image=i14)
        b14.grid(row=rows[1], column=columns[3]) 
        
        b15 = Button(self.master, highlightthickness=0, bd=0, width=100, height=100, command=lambda *args: self.a(b15))
        b15.config(image=i15)
        b15.grid(row=rows[2], column=columns[3])

        b16 = Button(self.master, highlightthickness=0, bd=0, width=100, height=100, command=lambda *args: self.a(b16))
        b16.config(image=i16)
        b16.grid(row=rows[3], column=columns[3])

        b17 = Button(self.master, highlightthickness=0, bd=0, width=100, height=100, command=lambda *args: self.a(b17))
        b17.config(image=i17)
        b17.grid(row=rows[4], column=columns[0])

        b18 = Button(self.master, highlightthickness=0, bd=0, width=100, height=100, command=lambda *args: self.a(b18))
        b18.config(image=i18)
        b18.grid(row=rows[0], column=columns[4])

        b19 = Button(self.master, highlightthickness=0, bd=0, width=100, height=100, command=lambda *args: self.a(b19))
        b19.config(image=i19)
        b19.grid(row=rows[4], column=columns[1])

        b20 = Button(self.master, highlightthickness=0, bd=0, width=100, height=100, command=lambda *args: self.a(b20))
        b20.config(image=i20)
        b20.grid(row=rows[4], column=columns[2])

        b21 = Button(self.master, highlightthickness=0, bd=0, width=100, height=100, command=lambda *args: self.a(b21))
        b21.config(image=i21)
        b21.grid(row=rows[4], column=columns[3])

        b22 = Button(self.master, highlightthickness=0, bd=0, width=100, height=100, command=lambda *args: self.a(b22))
        b22.config(image=i22)
        b22.grid(row=rows[3], column=columns[4])

        b23 = Button(self.master, highlightthickness=0, bd=0, width=100, height=100, command=lambda *args: self.a(b23))
        b23.config(image=i23)
        b23.grid(row=rows[2], column=columns[4])

        b24 = Button(self.master, highlightthickness=0, bd=0, width=100, height=100, command=lambda *args: self.a(b24))
        b24.config(image=i24)
        b24.grid(row=rows[1], column=columns[4])

        b25 = Button(self.master, highlightthickness=0, bd=0, width=100, height=100, command=lambda *args: self.a(b25))
        b25.config(image=i25)
        b25.grid(row=rows[4], column=columns[4])

######################################################################################
WIDTH = 500
HEIGHT = 500
window = Tk()
window.geometry("{}x{}".format(WIDTH, HEIGHT))
window.title("Slider Puzzle")
t = Slider(window)
t.setupGUI()
window.mainloop()
