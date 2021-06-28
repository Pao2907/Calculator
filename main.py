# Calculator Logic
import tkinter

root = tkinter.Tk()
root.title("Calculator")

expression = ""

# Create functions
#Add, clear, and calculate
def add(value):
    global expression
    expression += value
    label_result.config(text=expression)
    
def clear():
    global expression
    expression = ""
    label_result.config(text=expression)
    
def calculate():
    pass
