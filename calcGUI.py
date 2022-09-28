# O J Hunt
#14/09/22
# **************************************************
# Python calclator with GUI (Graphic User Interface)
# ***************************************************

from tkinter import * # import the tkinter library

def button_press(num):  # defining each button press
    global equation_text

    equation_text = equation_text + str(num)

    equation_label.set(equation_text)
    

def equals():  # This block checks for the button press(equals)
   
    global equation_text

    try: #try is used in try... except blocks. It defines a block of code to test if it contains any errors
        # You can define different blocks for different error types, and blocks to exceif nothing went wrong.
        total = str(eval(equation_text)) # parses the expression argue ment and evaluates it as a python expression.

        equation_label.set(total)   #

        equation_text = total

    except SyntaxError: # Check for syntax error

        equation_label.set("syntaxerror")

        equation_text = ""

    except ZeroDivisionError: # check for division by zero

        equation_label.set("arithmetic error")

        equation_text = ""

def clear(): # clears the equation_label for the next calculation
    global equation_text

    equation_label.set("")
    
    equation_text = ""




    # designing the user interface

window =Tk() # you can use window, root, ... or a descriptive variable of your own
window.title("Python Calculator") # title in window bar
window.geometry("435x635") # size of window depandant on your design
window.configure(bg="coral") # window colour depandant on your design

equation_text = "" # starting off with no text 

equation_label = StringVar()

label = Label(window, textvariable=equation_label, font=("console",50 ), bg="coral", width=24, height=2)
label.pack()

frame = Frame(window)
frame.pack()

button1 = Button(frame, text=1, height=4, width=9, font=35,  bg= "mediumturquoise", command=lambda: button_press(1))
button1.grid(row=0, column=0)

button2 = Button(frame, text=2, height=4, width=9, font=35, bg= "mediumturquoise", command=lambda: button_press(2))
button2.grid(row=0, column=1)

button3 = Button(frame, text=3, height=4, width=9, font=35, bg= "mediumturquoise", command=lambda: button_press(3))
button3.grid(row=0, column=2)

button4 = Button(frame, text=4, height=4, width=9, font=35, bg= "mediumturquoise", command=lambda: button_press(4))
button4.grid(row=1, column=0)

button5 = Button(frame, text=5, height=4, width=9, font=35, bg= "mediumturquoise", command=lambda: button_press(5))
button5.grid(row=1, column=1)

button6 = Button(frame, text=6, height=4, width=9, font=35, bg= "mediumturquoise", command=lambda: button_press(6))
button6.grid(row=1, column=2)

button7 = Button(frame, text=7, height=4, width=9, font=35, bg= "mediumturquoise", command=lambda: button_press(7))
button7.grid(row=2, column=0)

button8 = Button(frame, text=8, height=4, width=9, font=35, bg= "mediumturquoise", command=lambda: button_press(8))
button8 .grid(row=2, column=1)

button9 = Button(frame, text=9, height=4, width=9, font=35, bg= "mediumturquoise", command=lambda: button_press(9))
button9.grid(row=2, column=2)

button0 = Button(frame, text=0, height=4, width=9, font=35, bg= "mediumturquoise", command=lambda: button_press(0))
button0.grid(row=3, column=1)



# create the operation buttons

plus = Button(frame, text='+', height=4, width=9, font=35, bg= "mediumturquoise", command=lambda: button_press('+'))
plus.grid(row=0, column=3)

minus = Button(frame, text='-', height=4, width=9, font=35, bg= "mediumturquoise", command=lambda: button_press('-'))
minus.grid(row=1, column=3)

multiply = Button(frame, text='x', height=4, width=9, font=35, bg= "mediumturquoise", command=lambda: button_press('*'))
multiply.grid(row=2, column=3)

divide = Button(frame, text='/', height=4, width=9, font=35, bg= "mediumturquoise", command=lambda: button_press('/'))
divide.grid(row=3, column=3)

# create equals

equal = Button(frame, text='=', height=4, width=9, font=35, bg= "mediumturquoise", command=equals)
equal.grid(row=3, column=2)

# create decimal

decimal = Button(frame, text='.', height=4, width=9, font=35, bg= "mediumturquoise", command=lambda: button_press('.'))
decimal.grid(row=3, column=0)

# Create clear button

clear = Button(window, text='clear', height=200, width=200, font=35, bg= "mediumturquoise", command=clear)
clear.pack()


window.mainloop()