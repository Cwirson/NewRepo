from tkinter import *

window = Tk()
window.geometry("600x400")
window.title("Clicker")
window.configure(bg="black")

score = 0

def click():
    global score
    score += 1
    label.config(text=score)

label = Label(window, text="", padx=20, pady=40, font=("Times", "40", "bold italic"), fg="white", background="black")
label.pack()

clickbutton = Button(window, text="klikaj huju", font=("Times", "40", "bold italic"), fg="white", background="black", command=click)
clickbutton.pack()

window.mainloop()