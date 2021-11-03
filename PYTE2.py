import tkinter as tk
from tkinter.constants import BOTTOM, LEFT, RIGHT
import FPYTE2
#i will try to make both values in the same window so i don't complicate stuff that much

rootpyte = tk.Tk()
rootpyte.title("Value insertion...")
tptext = tk.Label(text="insert your values")
tpAtxt = tk.Label(text="VALUE A")
tpBtxt = tk.Label(text="VALUE B")
tpAent = tk.Entry(rootpyte)
tpBent = tk.Entry(rootpyte)

def resultdef():
    a = int(tpAent.get())
    b = int(tpBent.get())
    rootpyte.destroy()
 
    FPYTE2.runFPYTE2(a,b)

tpFbtn = tk.Button(text="done",command=resultdef)

tptext.pack()
tpAtxt.pack(side=LEFT)
tpBtxt.pack(side=RIGHT)
tpAent.pack(side=LEFT)
tpBent.pack(side=RIGHT)
tpFbtn.pack(side=BOTTOM)

rootpyte.mainloop()