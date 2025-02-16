
def button_press(num):
    global equation_text
    equation_text = equation_text+str(num)
    equation_label.set(equation_text)
def equals():
    global equation_text
    try:
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text =total
    except ZeroDivisionError:
        equation_label.set("arithemetic error")
        equation_text =""
    except SyntaxError:
        equation_label.set("Synatax Error")
        equation_text =""
def clear():
    global equation_text
    equation_label.set("")
    equation_text = ""

import tkinter as tk
root = tk.Tk()
root.title("Calculating program")
root.geometry("600x600")
equation_text = ""
equation_label = tk.StringVar()

label = tk.Label(root,textvariable = equation_label, font =("Airal",22), background= "white", width=30,height=2,)
label.pack(padx = 30, pady = 30)
class Button_Widget(tk.Button):

    def __init__(self,master, text, height, width, font, command):
        super().__init__(master, text= text, height= height, width= width, font= font, command= command)
        self.text = text
        self.height = height
        self.width = width
        self.font = font
        self.command = command

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

b1= Button_Widget(frame,"1",2,4,("Arial",18),lambda :button_press("1"))
b1.grid( row = 0, column =0)

b2= Button_Widget(frame,"2",2,4,("Arial",18),lambda :button_press("2"))
b2.grid( row = 0, column =1)

b3= Button_Widget(frame,"3",2,4,("Arial",18),lambda :button_press("3"))
b3.grid( row = 0, column =2 )

b4= Button_Widget(frame,"4",2,4,("Arial",18),lambda :button_press("4"))
b4.grid( row = 1, column =0 )

b5= Button_Widget(frame,"5",2,4,("Arial",18),lambda :button_press("5"))
b5.grid( row = 1, column =1 )

b6= Button_Widget(frame,"6",2,4,("Arial",18),lambda :button_press("6"))
b6.grid( row = 1, column =2 )

b7= Button_Widget(frame,"7",2,4,("Arial",18),lambda :button_press("7"))
b7.grid( row = 2, column =0 )

b8= Button_Widget(frame,"8",2,4,("Arial",18),lambda :button_press("8"))
b8.grid( row = 2, column =1 )

b9= Button_Widget(frame,"9",2,4,("Arial",18),lambda :button_press("9"))
b9.grid( row = 2, column =2 )

b0= Button_Widget(frame,"0",2,4,("Arial",18),lambda :button_press("0"))
b0.grid( row = 3, column =1 )

Plus= Button_Widget(frame,"+",2,4,("Arial",18),lambda :button_press("+"))
Plus.grid( row = 0, column =3 )

Minus= Button_Widget(frame,"-",2,4,("Arial",18),lambda :button_press("-"))
Minus.grid( row = 1, column =3 )

Multiply= Button_Widget(frame,"*",2,4,("Arial",18),lambda :button_press("*"))
Multiply.grid( row = 2, column =3 )

division= Button_Widget(frame,"/",2,4,("Arial",18),lambda :button_press("/"))
division.grid( row = 3, column =3 )

equal_to = Button_Widget(frame,"=",2,4,("Arial",18),lambda :equals())
equal_to.grid( row = 3, column =2 )

Clr = Button_Widget(frame,"Cls",2,4,("Arial",18),lambda : clear())
Clr.grid( row = 3, column =0 )



root.mainloop()

