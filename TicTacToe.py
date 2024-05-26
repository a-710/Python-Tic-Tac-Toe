import tkinter
import tkinter.ttk
import random
import time

root=tkinter.Tk()
screen_width = root.winfo_screenwidth()/2
screen_height = root.winfo_screenheight()/2

# Label to display the winner
winner_label = tkinter.Label(root, text="", font=("Helvetica", 16))
winner_label.grid(row=3, column=0, columnspan=3, pady=10)

#print (screen_width, 'x', screen_height) Debug for screenres

if screen_height>screen_width:
    minres=screen_width
else:
    minres=screen_height

def check_winner():
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
        (0, 4, 8), (2, 4, 6)  # diagonals
    ]
    for a, b, c in winning_combinations:
        if buttons[a].cget("text") == buttons[b].cget("text") == buttons[c].cget("text") != " ":
            return buttons[a].cget("text")
    return None

def on_button_click(event):
     button=event.widget
     if button.cget("text")==" ":
        button.config(text="X")
        winner = check_winner()
        if winner:
            game_over(winner)
        else:
            root.after(1,computer_click)
    

def computer_click():
    empty_buttons = [button for button in buttons if button.cget("text") == " "]
    if empty_buttons:
        button = random.choice(empty_buttons)
        button.config(text="O")
        winner = check_winner()
        if winner:
            game_over(winner)

'''def check_button_text(): #More debug func
    button_text = button.cget("text")
    print(f"The text on the button is: {button_text}")'''

def game_over(winner):
    winner_label.config(text=f"The winner is {winner}!")
    for button in buttons:
        button.config(state="disabled") # Disables all the buttons to prevent bugs
    root.after(2000,exit)
    
minres=int(minres)
root.title("Tic Tac Toe")
root.geometry(str(minres)+"x"+str(minres))

buttons = []
butoncounter=0
for i in range(3):
    for j in range(3):
        button = tkinter.Button(root, text=f" ",width=int(minres/50),height=int(minres/100))
        butoncounter+=1
        button.grid(row=i,column=j)
        button.bind("<Button-1>", on_button_click)
        buttons.append(button)


root.mainloop()