import tkinter as tk
from tkinter.constants import LEFT, RIGHT

form = ('Pythagorean Theoreum','Trigonometric Equation')

root = tk.Tk()
root.geometry("230x120")
root.title("Select your formula")

option_var = tk.StringVar()
textroot = tk.Label(text="Please select your formula")
OMroot = tk.OptionMenu(root, option_var, *form)
textroot2 = tk.Label(text="More is coming soon",fg="gray")

textPYTE2 = tk.Label(text="Please input your value for side B.")
valbinput = tk.Entry()
valbcont = tk.Button(text="Contiune",command=root.destroy)

def valacomp():
    textPYTE.destroy()
    valainput.destroy()
    valacont.destroy()

    textPYTE2.pack()
    valbinput.pack(side=LEFT)
    valbcont.pack(side=RIGHT)
    finalresultpyte = ((valainput.get()**2)+(valbinput.get()**0.5))
    finalresultlabelpyte = tk.Label(text="Result = {finalresultpyte}")
    finalresultbtnpyte = tk.Button(text="Ok",command=root.destroy)

    textPYTE2.destroy()
    valbinput.destroy()
    valbcont.destroy()

    finalresultlabelpyte.pack()
    finalresultbtnpyte.pack()

textPYTE = tk.Label(text="Please input your value for side A.")
valainput = tk.Entry()
valacont = tk.Button(text="Continue",command=valacomp)

def acceptbtndef():
    if option_var.get() == "Pythagorean Theoreum":
        textroot.destroy()
        OMroot.destroy()
        textroot2.destroy()
        acceptbtn.destroy()

        root.title("Input your values")
        root.geometry("280x120")
        textPYTE.pack()
        valainput.pack(side=LEFT)
        valacont.pack(side=RIGHT)
    else:
        root.destroy()

acceptbtn = tk.Button(text="Next", command=acceptbtndef)

textroot.pack()
OMroot.pack()
textroot2.pack()
acceptbtn.pack()

root.mainloop()