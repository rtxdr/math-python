import tkinter as tk
from tkinter.constants import LEFT, RIGHT
import PYTE
import TREQ

form = ('Pythagorean Theoreum','Trigonometric Equation')

root = tk.Tk()
root.geometry("230x120")
root.title("Select your formula")

option_var = tk.StringVar()

textroot = tk.Label(text="Please select your formula")
OMroot = tk.OptionMenu(root, option_var, *form)
textroot2 = tk.Label(text="More is coming soon",fg="gray")

def acceptbtndef():
    if option_var.get() == "Pythagorean Theoreum":
        root.destroy()
        PYTE.runpyte()
    elif option_var.get() == "Trigonometric Equation":
        root.destroy()
        TREQ.treqrun()
    else:
        root.destroy()

acceptbtn = tk.Button(text="Next", command=acceptbtndef)

textroot.pack()
OMroot.pack()
textroot2.pack()
acceptbtn.pack()

root.mainloop()