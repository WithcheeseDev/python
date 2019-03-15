from tkinter import *
from tkinter import ttk
from time import sleep   

Axes = [0,0,0,0,0,0]

gui = Tk()

def Incs_1():
    Axes[0] += 10
    Axes_1.set(Axes[0])

def Decs_1():
    Axes[0] -= 10
    Axes_1.set(Axes[0])
    
def Incs_2():
    Axes[1] += 10
    Axes_2.set(Axes[1])

def Decs_2():
    Axes[1] -= 10
    Axes_2.set(Axes[1])

Axes_1 = StringVar()
Axes_2 = StringVar()
Axes_3 = StringVar()
Axes_4 = StringVar()
Axes_5 = StringVar()
Axes_6 = StringVar()


Axes_1.set(Axes[0])
Axes_2.set(Axes[1])
Axes_3.set(Axes[2])
Axes_4.set(Axes[3])
Axes_5.set(Axes[4])
Axes_6.set(Axes[5])

#Configuraion
gui.geometry('450x300')
gui.title('SIMULATOR_STEPMOTOR_PROGRAM')

#Axes_1
lb_Axes_1 = ttk.Label(gui, text = 'Axes : 1')
lb_Axes_1.grid(row = 0, column = 0,padx = 10, pady = 20)

btn_Incs_Axes_1 = ttk.Button(gui, text = 'Incs', command = Incs_1)
btn_Incs_Axes_1.grid(row = 0, column = 1,padx = 20, pady = 20)

btn_Decs_Axes_1 = ttk.Button(gui, text = 'Decs', command = Decs_1)
btn_Decs_Axes_1.grid(row = 0, column = 2,padx = 5, pady = 20)

lb_Axes_1_Val = ttk.Label(gui, textvariable = Axes_1)
lb_Axes_1_Val.grid(row = 0, column = 3,padx = 70, pady = 20)

#Axes_2
lb_Axes_2 = ttk.Label(gui, text = 'Axes : 2')
lb_Axes_2.grid(row = 1, column = 0,padx = 10, pady = 20)

btn_Incs_Axes_2 = ttk.Button(gui, text = 'Incs', command = Incs_2)
btn_Incs_Axes_2.grid(row = 1, column = 1,padx = 20, pady = 20)

btn_Decs_Axes_2 = ttk.Button(gui, text = 'Decs', command = Decs_2)
btn_Decs_Axes_2.grid(row = 1, column = 2,padx = 5, pady = 20)

lb_Axes_2_Val = ttk.Label(gui, textvariable = Axes_2)
lb_Axes_2_Val.grid(row = 1, column = 3,padx = 70, pady = 20)

gui.mainloop()