import tkinter
import tkinter.ttk

root=tkinter.Tk()
screen_width = root.winfo_screenwidth()/2
screen_height = root.winfo_screenheight()/2

#print (screen_width, 'x', screen_height) Debug for screenres

if screen_height>screen_width:
    minres=screen_width
else:
    minres=screen_height

def on_button_click(event):
    button=event.widget
    button.config(text="X")

def check_button_text():
    button_text = button.cget("text")
    print(f"The text on the button is: {button_text}")

minres=int(minres)
root.title("Tic Tac Toe")
root.geometry(str(minres)+"x"+str(minres))

""" Another way I tried to make the buttons
btn0 = tkinter.Button(root,text="Apasa!",command = on_button_click,width=int(minres/50),height=int(minres/100))
#btn0.pack()
btn1 = tkinter.Button(root,text="Apasa!",command = on_button_click,width=int(minres/50),height=int(minres/100))
#btn1.pack()
btn2 = tkinter.Button(root,text="Apasa!",command = on_button_click,width=int(minres/50),height=int(minres/100))
#btn2.pack()
btn3 = tkinter.Button(root,text="Apasa!",command = on_button_click,width=int(minres/50),height=int(minres/100))
#btn3.pack()
btn4 = tkinter.Button(root,text="Apasa!",command = on_button_click,width=int(minres/50),height=int(minres/100))
#btn4.pack()
btn5 = tkinter.Button(root,text="Apasa!",command = on_button_click,width=int(minres/50),height=int(minres/100))
#btn5.pack()
btn6 = tkinter.Button(root,text="Apasa!",command = on_button_click,width=int(minres/50),height=int(minres/100))
#btn6.pack()
btn7 = tkinter.Button(root,text="Apasa!",command = on_button_click,width=int(minres/50),height=int(minres/100))
#btn7.pack()
btn8 = tkinter.Button(root,text="Apasa!",command = on_button_click,width=int(minres/50),height=int(minres/100))
#btn8.pack()"""

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