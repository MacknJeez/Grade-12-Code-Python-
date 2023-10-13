#DOESN'T WORK!!!!! i'll fix later
import tkinter

from tkinter.constants import *
stack=[]
def push(push_val):
    stack.append(push_val)
    print(stack)
def pop(n):
    stack.pop()
    if stack==[]:
        print("List is empty.")
    else:
        print("Deleted Element:", stack.pop())
def display(n):
    for i in range(len(stack)-1,-1,-1):
        print(stack(i))

tk = tkinter.Tk()

#For gui(pronounced guuu-eeee)
frame = tkinter.Frame(tk, relief=RIDGE, borderwidth=2)
frame.pack(fill=BOTH,expand=1)

#For name of gui
label = tkinter.Label(frame, text="Stack Commands")
label.pack(fill=X, expand=1)

#Entry values
Label(tk, text="Enter Value:").grid(row=0)
entry=Entry(tk)
entry.grid(row=0,column=1)

#For the buttons
button_push= tkinter.Button(frame,text="Push",command=push(entry))
button_push.pack(side=RIGHT)

button_pop= tkinter.Button(frame,text="Pop",command=pop(entry))
button_pop.pack()

button_disp= tkinter.Button(frame,text="Display",command=display(entry))
button_disp.pack(side=RIGHT)


tk.mainloop()
