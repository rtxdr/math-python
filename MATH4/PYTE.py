import tkinter as tk
from tkinter.constants import BOTTOM, LEFT, RIGHT
import FPYTE
#i will try to make both values in the same window so i don't complicate stuff that much

def runpyte():
    rootpyte = tk.Tk()
    rootpyte.title("Value insertion...")
    tptext = tk.Label(text="Please insert your values")
    tpAtxt = tk.Label(text="Value A")
    tpBtxt = tk.Label(text="Value B")
    tpAent = tk.Entry(rootpyte)
    tpBent = tk.Entry(rootpyte)
    #error text will be implemented later in the future
    #errortext = tk.Label(text="Error!",fg="red")

    def resultdef():
        a = int(tpAent.get())
        b = int(tpBent.get())
        rootpyte.destroy()
    
        FPYTE.runFPYTE(a,b)

    tpFbtn = tk.Button(text="done",command=resultdef)

    tptext.grid(column=2,row=1)
    tpAtxt.grid(column=1,row=2)
    tpBtxt.grid(column=3,row=2)
    tpAent.grid(column=1,row=3)
    tpBent.grid(column=3,row=3)
    tpFbtn.grid(column=2,row=4)
    #errortext.grid(column=2,row=5)
    #error text will be implemented in the future
    #errortext.pack()
    tptext.pack()
    tpAtxt.pack()
    tpBtxt.pack()
    tpAent.pack()
    tpBent.pack()
    tpFbtn.pack(side=BOTTOM)

    rootpyte.mainloop()

if __name__ == "__main__":
    runpyte()
