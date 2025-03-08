import tkinter
from tkinter import *
window =Tk()
window.geometry("600x800")
window.title("Basic_Calculator")

var =StringVar()
label = Label(window,textvariable=var, background= "white", width=200,height=10, borderwidth=12,relief="sunken",font=58)
label.pack(expand = True)

button_box = Frame(window,height=200,width=500, bg="White")
button_box.pack(fill= "both", expand = True)

var_str =" "
def button_press(num):
    global var_str
    var_str =var_str+ str(num)
    var.set(var_str)

def equal():
    global var_str
    try:
        total = str(eval(var_str))
        var.set(total)
    except ZeroDivisionError:
        var.set("Error")
    except SyntaxError:
        var.set("Syntax Error")

def clear():
    global var_str
    var_str = " "
    var.set(var_str)

buttons = [('1',0,0),('2',0,1),('3',0,2),
           ('4',1,0),('5',1,1),('6',1,2),
           ('7',2,0),('8',2,1),('9',2,2),
           ('0',3,0),('+',3,1),('-',0,3),
           ('/',1,3),('*',2,3),('=',3,3),
           ("Cls",3,2)]

for text, row, column in buttons:
    if text == "=":
        button = Button(button_box, text="=",width=10, height= 5, font= 16, command=equal)
    elif text == "Cls":
        button = Button(button_box, text="Cls",width=10, height= 5, font= 16, command= clear)
    else:
        button = Button(button_box,text= text,relief=RAISED, width=10, height= 5, font= 16, command= lambda num =text: button_press(num))
    button.grid(row=row, column=column,padx=35,pady=10, sticky = "nsew")

# Make the button_box expandable
for i in range(4):  # Assuming 4 columns
    button_box.columnconfigure(i, weight=1)

for i in range(5):  # Assuming 5 rows
    button_box.rowconfigure(i, weight=1)

mainloop()
