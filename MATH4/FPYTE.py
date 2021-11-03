import tkinter as tk

def runFPYTE(ansa,ansb):
    finalanswer = ((ansa**2)+(ansb**2))**0.5
    print(finalanswer)

    res = "The length of side C is {}."
    rootfinalpyte = tk.Tk()
    rootfinalpyte.title("Final result.")
    fpL = tk.Label(text=res.format(finalanswer))
    fpB = tk.Button(text="Quit",command=rootfinalpyte.destroy)

    fpL.pack()
    fpB.pack()

    rootfinalpyte.mainloop()

if __name__ == "__main__":
    runFPYTE()