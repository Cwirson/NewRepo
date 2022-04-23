import time 
from tkinter import *

root = Tk()
root.title("Zegar")
root.geometry("600x400")
root.configure(background="black")

def timer():
    hour = time.strftime("%H")
    minute = time.strftime("%M")
    second = time.strftime("%S")
    day = time.strftime("%d")
    month = time.strftime("%B")
    label.config(text=hour + ":" + minute + ":" + second)
    label2.config(text=f"It's {day}th day of {month}")
    label.after(1000, timer)

label = Label(root, text="", padx=20, pady=20, font=("Times", "40", "bold italic"), fg="white", background="black")
label.pack()
label2 = Label(root, text="", font=("Times", "20", "bold italic"), fg="white", background="black")
label2.pack()
timer()

root.mainloop()

