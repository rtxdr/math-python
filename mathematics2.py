import tkinter as tk

vala=int(input("how long is side A"))
valb=int(input("how long is side B"))

valc = ((vala**2)+(valb**2))**0.5

res = "hypothenus is",valc,"long, i don't know what unit though"
#i added humour in my code because this code really is boring

result = tk.Tk()
rtxt = tk.Label(text=res)
rbtn = tk.Button(text="nice",command=result.destroy)

#for some reason there's some stupid brackets in the result I HATE THIS CODE!!!!!

rtxt.pack()
rbtn.pack()

result.mainloop()