from tkinter import *

tk=Tk()
tk.geometry("150x150")

button_1= Button(tk,text="Hey there.",command=print("I want to die"))

button_1.pack()

tk.mainloop()
