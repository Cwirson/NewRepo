import time 
from tkinter import *


root = Tk()
root.geometry("600x400")

def update():
    hour = time.strftime("%H")
    minute = time.strftime("%M")
    second = time.strftime("%S")
    timer = f"{hour} {minute} {second}"
    print(timer)
    label.config(text=timer)
    
label = Label(root, text="", padx=20, pady=20)
label.pack()
label.after(1000, update)

root.mainloop()