import tkinter as tk

def key(event):
    """shows key or tk code for the key"""
    if event.keysym == 'Escape':
        root.destroy()
    print(event.keysym)
root = tk.Tk()
print('Press a key (Escape key to exit):')
root.bind_all('<Key>', key)
root.withdraw()
root.mainloop()
