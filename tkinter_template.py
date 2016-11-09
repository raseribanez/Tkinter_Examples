#se Tkinter for python 2, tkinter for python 3
import Tkinter as tk
from Tkinter import * 

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        # <create the rest of your GUI here>

        btn_exit = Button(self, text='Exit', command=quit)
        btn_exit.pack(side=BOTTOM)

if __name__ == "__main__":
    root = tk.Tk()
    root.minsize(300,300)
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
