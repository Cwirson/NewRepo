from random import *
from tkinter import *

window = Tk()

players = ["x", "o"]
player = choice(players)


def playermove():
    pass

def empty_spaces():
    pass

def winner():
    for row in range(3):
        if gamemap[row][0]["text"] == gamemap[row][1]["text"] == gamemap[row][2]["text"] != "":
            return True
    for column in range(3):
        if gamemap[0][column]["text"] == gamemap[1][column]["text"] == gamemap[2][column]["text"] != "":
            return True
    if gamemap[0][0]["text"] == gamemap[1][1]["text"] == gamemap[2][2]["text"] != "":
        return True
    if gamemap[0][2]["text"] == gamemap[1][1]["text"] == gamemap[2][0]["text"] != "":
        return True
    elif empty_spaces() is False:
        return "Tie"
    else:
        return False

def next_turn(row, column):
    global player
    
    if gamemap[row][column]["text"] == "" and winner() is False:
        if player == players[0]:
            gamemap[row][column]["text"] = player
            if winner() is False:
                player = players[1]
                label.config(text=f"{players[1]} turn")
            elif winner() is True:
                label.config(text=f"{players[0]} wins")
            elif winner() == "Tie":
                label.config(text="tie, nobody wins")      
        else:
            gamemap[row][column]["text"] = player
            if winner() is False:
                player = players[0]
                label.config(text=f"{players[0]} turn")
            elif winner() is True:
                label.config(text=f"{players[1]} wins")
            elif winner() == "Tie":
                label.config(text="tie, nobody wins")
            
            
label = Label(window, text=f"{player} move", font=("consolas", 20))
label.pack(side="top")

restart_button = Button(window, text="Restart", font=("consolas", 20))
restart_button.pack(side="top")

gamemap = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

frames = Label(window)
frames.pack()

for column in range(3):
    for row in range(3):
        gamemap[row][column] = Button(frames, text="", font=("consolas", 40), width=5, height=2, command= lambda row = row, column = column: next_turn(row, column))
        gamemap[row][column].grid(row = row, column = column)

window.mainloop()