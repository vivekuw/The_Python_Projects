"""
Tkinter calculator 
this is calculator with the help of tkinter.
"""

# step 1: import tkinter
from tkinter import *

# step 2: gui interaction
windows = Tk()

# step 3:adding inputs
windows.geometry("500x500")

# entry

e = Entry(windows,width=54,borderwidth=5)
e.place(x=0,y=0)
'''
# FUNCTION
'''

def click(num):
    result = e.get()
    e.delete(0,END)
    e.insert(0, str(result) + str(num))
    
    
# " + " function code
def add():
    n1 = e.get()
    global math
    math = "addition"
    global i
    i = int(n1)
    e.delete(0,END)
    
# " - " function code
def sub():
    n1 = e.get()
    global math
    math = "subtraction"
    global i
    i = int(n1)
    e.delete(0,END)

# " * " function code
def mul():
    n1 = e.get()
    global math
    math = "multiplication"
    global i
    i = int(n1)
    e.delete(0,END)

# " / " function code
def div():
    n1 = e.get()
    global math
    math = "division"
    global i
    i = int(n1)
    e.delete(0,END)

# " = " function code
def equal():
    n2 = e.get()
    e.delete(0,END)
    if math == "addition":
        e.insert(0,i + int(n2))
    elif math == "subtraction":
        e.insert(0,i-int(n2))
    elif math == "multiplication":
        e.insert(0,i*int(n2))
    elif math == "division":
        e.insert(0,i/int(n2))
        
# "clean the box" function code
def clear():
    e.delete(0,END)
    
    
'''# button numerical or operations'''
button_1 = Button(windows,text="1",width=12,command=lambda:click(1))
button_1.place(x=10,y=60)

button_2 = Button(windows,text="2",width=12,command=lambda:click(2))
button_2.place(x=80,y=60)

button_3 = Button(windows,text="3",width=12,command=lambda:click(3))
button_3.place(x=170,y=60)

button_a = Button(windows,text="+",width=12,command=add)      # +
button_a.place(x=240,y=60)

button_4 = Button(windows,text="4",width=12,command=lambda:click(4))
button_4.place(x=10,y=120)

button_5 = Button(windows,text="5",width=12,command=lambda:click(5))
button_5.place(x=80,y=120)

button_6 = Button(windows,text="6",width=12,command=lambda:click(6))
button_6.place(x=170,y=120)

button_a = Button(windows,text="-",width=12,command=sub)    # -
button_a.place(x=240,y=120)

button_7 = Button(windows,text="7",width=12,command=lambda:click(7))
button_7.place(x=10,y=180)

button_8 = Button(windows,text="8",width=12,command=lambda:click(8))
button_8.place(x=80,y=180)

button_9 = Button(windows,text="9",width=12,command=lambda:click(9))
button_9.place(x=170,y=180)

button_a = Button(windows,text="*",width=12,command=mul)    # *
button_a.place(x=240,y=180)

button_0 = Button(windows,text="0",width=19,command=lambda:click(0))
button_0.place(x=10,y=240)

button_10 = Button(windows,text="=",width=19,command=equal)      # =
button_10.place(x=120,y=240)

button_a = Button(windows,text="/",width=12,command=div)    # /
button_a.place(x=240,y=240)

button_a = Button(windows,text="Clear",width=45,command=clear)  # CLEAR
button_a.place(x=10,y=300)


# step 4: main loop
mainloop()