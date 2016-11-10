import Tkinter as tk
from Tkinter import *

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        lbl_result = Label(self, fg='Blue',text='I am displaying this label', font='freesansbold, 18') #textvariable=cvt_to, font='freesansbold, 16', fg='Blue')
        lbl_result.pack(side=BOTTOM)#fill=BOTH, expand=1)


if __name__ == "__main__":
    root = tk.Tk()
    root.minsize(600,700)
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
