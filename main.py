# importing everyting from tkinter
from tkinter import *
import customtkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# expression to access among all the functions
expression = ""
# functions
def input_number(number, equation):
    # accessing the global expression variable
    global expression
    # concatenation of string
    expression = expression + str(number)
    equation.set(expression)


def clear_input_field(equation):
    global expression
    expression = ""
    # setting empty string in the input field
    equation.set("Enter the expression")


def evaluate(equation):
    global expression
    # trying to evaluate the expression
    try:
        result = str(eval(expression))
        # showing the result in the input field
        equation.set(result)
        # setting expression to empty string
        expression = ""
    except:
        # some error occured
        # showing it to the user equation.set("Enter a valid expression")
        expression = ""
    # creating the GUI


def main():
    # main window
    window = customtkinter.CTk()
    # setting the title of GUI window
    window.title("Calculator")
    # set the configuration of GUI window
    window.geometry("600x220")
    # varible class instantiation
    equation = StringVar()
    # input field for the expression
    input_field =  customtkinter.CTkEntry(master=window,
                               placeholder_text="Enter the Expression",
                               textvariable = equation,
                               width=120,
                               height=25,
                               border_width=2,
                               corner_radius=10,)
    # we are using grid position
    # for the arrangement of the widgets
    input_field.grid(columnspan=4, ipadx=100, ipady=10)
    # creating buttons and placing them at respective positions, origin being (0,0)
    
    #Button for 1, the declaration below is attached to the object and sets its position
    _1 = customtkinter.CTkButton(
        text="1",
        command=lambda: input_number(1, equation),
        master=window,
    )
    _1.grid(row=2, column=0,pady=5, padx=5)
    
    _2 = customtkinter.CTkButton(
       
        text="2",
        command=lambda: input_number(2, equation),
        master=window,
    )
    _2.grid(row=2, column=1, pady=5, padx=5,)
    
    _3 = customtkinter.CTkButton(
       
        text="3",
        command=lambda: input_number(3, equation),
        master=window,
    )
    _3.grid(row=2, column=2, pady=5, padx=5,)
    
    _4 = customtkinter.CTkButton(
       
        text="4",
        command=lambda: input_number(4, equation),
        master=window,
    )
    _4.grid(row=3, column=0, pady=5, padx=5,)
    
    _5 = customtkinter.CTkButton(
       
        text="5",
        command=lambda: input_number(5, equation),
        master=window,
    )
    _5.grid(row=3, column=1, pady=5, padx=5,)
    
    _6 = customtkinter.CTkButton(
       
        text="6",
        command=lambda: input_number(6, equation),
        master=window,
    )
    _6.grid(row=3, column=2, pady=5, padx=5,)
    
    _7 = customtkinter.CTkButton(
       
        text="7",
        command=lambda: input_number(7, equation),
        master=window,
    )
    _7.grid(row=4, column=0, pady=5, padx=5,)
    
    _8 = customtkinter.CTkButton(
       
        text="8",
        command=lambda: input_number(8, equation),
        master=window,
    )
    _8.grid(row=4, column=1, pady=5, padx=5,)
    
    _9 = customtkinter.CTkButton(
       
        text="9",
        command=lambda: input_number(9, equation),
        master=window,
    )
    _9.grid(row=4, column=2, pady=5, padx=5,)
    
    _0 = customtkinter.CTkButton(
       
        text="0",
        command=lambda: input_number(0, equation),
        master=window,
    )
    _0.grid(row=5, column=0, pady=5, padx=5,)
    
    plus = customtkinter.CTkButton(
       
        text="+",
        command=lambda: input_number("+", equation),
        master=window,
    )
    plus.grid(row=2, column=3, pady=5, padx=5,)
    
    minus = customtkinter.CTkButton(
       
        text="-",
        command=lambda: input_number("-", equation),
        master=window,
    )
    minus.grid(row=3, column=3, pady=5, padx=5,)
    
    multiply = customtkinter.CTkButton(
       
        text="*",
        command=lambda: input_number("*", equation),
        master=window,
    )
    multiply.grid(row=4, column=3, pady=5, padx=5,)
    
    divide = customtkinter.CTkButton(
       
        text="/",
        command=lambda: input_number("/", equation),
        master=window,
    )
    divide.grid(row=5, column=3, pady=5, padx=5,)
    
    equal = customtkinter.CTkButton(
       
        text="=",
        command=lambda: evaluate(equation),
        master=window,
    )
    equal.grid(row=5, column=2, pady=5, padx=5,)
    
    clear = customtkinter.CTkButton(
       
        text="Clear",
        command=lambda: clear_input_field(equation),
        master=window,
    )
    clear.grid(row=5, column=1)
    # showing the GUI
    window.mainloop()


# start of the program
if __name__ == "__main__":
    main()
