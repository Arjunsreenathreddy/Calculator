import tkinter
from tkinter import *

# Create the main window
window = Tk()
window.geometry("600x800")
window.title("Basic_Calculator")

# StringVar to update the label display
var = StringVar()
label = Label(window, textvariable=var, background="white", width=200, height=10, borderwidth=12, relief="sunken", font=58)
label.pack(expand=True)

# Create a frame for the buttons
button_box = Frame(window, height=200, width=500, bg="White")
button_box.pack(fill="both", expand=True)

# Global variables
var_str = ""
last_was_equal = False  # Flag to track if "=" was pressed

# Function for button presses
def button_press(num):
    global var_str, last_was_equal
    if last_was_equal:  # If "=" was pressed previously, clear the input before adding new numbers
        var_str = ""
        last_was_equal = False  # Reset flag
    var_str += str(num)
    var.set(var_str)

# Function to evaluate the expression
def equal():
    global var_str, last_was_equal
    try:
        total = str(eval(var_str))  # Evaluate the mathematical expression
        var.set(total)
        var_str = total  # Store the result for further calculations
        last_was_equal = True  # Set flag that "=" was pressed
    except ZeroDivisionError:
        var.set("Error")
        var_str = ""
    except SyntaxError:
        var.set("Syntax Error")
        var_str = ""

# Function to clear the display
def clear():
    global var_str, last_was_equal
    var_str = ""
    var.set("")
    last_was_equal = False  # Reset flag

# Define the buttons (text, row, column)
buttons = [
    ('1', 0, 0), ('2', 0, 1), ('3', 0, 2),
    ('4', 1, 0), ('5', 1, 1), ('6', 1, 2),
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2),
    ('0', 3, 0), ('+', 3, 1), ('-', 0, 3),
    ('/', 1, 3), ('*', 2, 3), ('=', 3, 3),
    ("Cls", 3, 2)
]

# Create and place the buttons in the grid
for text, row, column in buttons:
    if text == "=":
        button = Button(button_box, text="=", width=10, height=5, font=16, command=equal)
    elif text == "Cls":
        button = Button(button_box, text="Cls", width=10, height=5, font=16, command=clear)
    else:
        button = Button(button_box, text=text, relief=RAISED, width=10, height=5, font=16, command=lambda num=text: button_press(num))
    button.grid(row=row, column=column, padx=35, pady=10, sticky="nsew")

# Make the button box expandable
for i in range(4):  # Assuming 4 columns
    button_box.columnconfigure(i, weight=1)

for i in range(5):  # Assuming 5 rows
    button_box.rowconfigure(i, weight=1)

# Run the Tkinter event loop
mainloop()
