from tkinter import *
from tkinter.ttk import *
import sys

class Window():
    def __init__(self):
        self.window = Tk()
        self.lbl = None
        
    def title(self, title):
        if isinstance(title, str):
            self.window.title(title)
        else:
            print('ingrese un titulo adecuado')
    
    def label(self, labeltxt):
        if isinstance(labeltxt, str):
            self.lbl = Label(self.window, text=labeltxt, style="BW.TLabel")
            self.lbl.grid(column=0, row=0)
        else:
            print('ingrese un label adecuado')

    def styleForDarkcula(self):
        self.style = Style()
        self.style.configure("BW.TLabel", foreground="black", background="white")

        """ 
        Example:
            l1 = ttk.Label(text="Test", style="BW.TLabel")
            l2 = ttk.Label(text="Test", style="BW.TLabel")
        """

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    myapp = Window()
    myapp.title(sys.argv[1])
    myapp.styleForDarkcula()
    myapp.label(sys.argv[2])
    myapp.run()
