from tkinter import *
        
class MainGui:

    def __init__(self, root):
        self.AxesVal = [0,0,0,0,0,0]
        self.AxesVal_1 = StringVar()
        self.AxesVal_1.set(self.AxesVal[0])
        
        def InscAxes_1():
            self.AxesVal[0] += 10
      
        fm = Frame(root, width=300, height=200, bg = "yellow")
        fm.grid(padx = 10, pady = 10, row = 0, column = 0)
    
        self.lbAxesVal_1 = Label(fm, textvariable=self.AxesVal_1)
        self.lbAxesVal_1.grid(padx = 10, pady = 10, row = 0, column = 0)
    
    
        self.btnInscAxes_1 = Button(fm, text="Insc", command = InscAxes_1)
        self.btnInscAxes_1.grid(padx = 10, pady = 10, row = 0, column = 1)
    
        btnDescAxes_2 = Button(fm, text="Desc")
        btnDescAxes_2.grid(padx = 10, pady = 10, row = 0, column = 2)
      
        root.geometry("400x300")




if __name__ == "__main__":
    root = Tk()
    MainApp = MainGui(root)
    root.mainloop()
    
