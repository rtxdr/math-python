import tkinter as tk

def treqrun():
    baseroot = tk.Tk()
    baseroot.title("Coming soon")
    label = tk.Label(text="""This feature is coming soon
    (i'm studying this for school so i can learn
    this better by implementing it in a code!!
    """)
    extbtn = tk.Button(text="Exit",command=baseroot.destroy)

    label.pack()
    extbtn.pack()

if __name__ == "__main__":
    treqrun()