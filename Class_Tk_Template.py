# Ben woodfield
# I found this when I wanted to wrap a few of my Tk projects into classes
# I hoped to come up with a template I can use to start projects quickly
# This seemed a bit overkill really as the number of argumentsseems a bit much for my 
# level of writing. If this is what you were after (A Tkinter class template) look through
# my repositories because I have dedicated a repo to a lightweight, efficient and working
# Tkinter class-template ready to write a project straight into. This one does work though

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
