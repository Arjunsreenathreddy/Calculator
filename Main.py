import tkinter as tk

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

root = tk.Tk()
root.title("Calculating Program")
root.geometry("600x600")

equation_text = ""
equation_label = tk.StringVar()

# Label with padding
label = tk.Label(root, textvariable=equation_label, font=("Arial", 22), background="white", width=30, height=2)
label.pack(padx=30, pady=30)

class Button_Widget(tk.Button):
    def __init__(self, master, text, command):
        super().__init__(master, text=text, height=2, width=4, font=("Arial", 18), command=command)

# Frame with padding
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)
# Button layout (text, row, col)
buttons = [
    ("1", 0, 0), ("2", 0, 1), ("3", 0, 2), ("+", 0, 3),
    ("4", 1, 0), ("5", 1, 1), ("6", 1, 2), ("-", 1, 3),
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("*", 2, 3),
    (".", 3, 0), ("0", 3, 1),  ("/", 3, 3),
]
# Create buttons dynamically
for text, row, col in buttons:
    btn = Button_Widget(frame, text, lambda t=text: button_press(t))
    btn.grid(row=row, column=col, padx=5, pady=5)

# Equal button
Equal_button = Button_Widget(frame, "=", lambda :equals())
Equal_button.grid(row=3, column=2)

# Clear button spanning columns 0 to 3
clear_button = Button_Widget(frame, "Clear", lambda: clear())
clear_button.grid(row=4, column=0,columnspan=4,padx=5, pady=5,sticky="nsew")

root.mainloop()
