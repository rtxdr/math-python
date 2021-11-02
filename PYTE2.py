import tkinter as tk
from tkinter.constants import LEFT, RIGHT
#i will try to make both values in the same window so i don't complicate stuff that much

rootpyte = tk.Tk()
tptext = tk.Label(text="insert your values")
tpAtxt = tk.Label(text="VALUE A")
tpBtxt = tk.Label(text="VALUE B")
tpAent = tk.Entry()
tpBent = tk.Entry()

def resultdef():
    print("this sucks")

tpFbtn = tk.Button(text="done",command=resultdef)

rootpyte.pack()
tptext.pack()
tpAtxt.pack(side=LEFT)
tpBtxt.pack(side=RIGHT)
tpAent.pack(side=LEFT)
tpBent.pack(side=RIGHT)

rootpyte.mainloop()