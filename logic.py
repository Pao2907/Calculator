import tkinter

root = tkinter.Tk()
root.title("Calculator")

expression = ""

# Create functions
#Add, Clear, Delete, and Calculate
def add(value):
    global expression
    expression += value
    label_result.config(text=expression)
    
def clear():
    global expression
    expression = ""
    label_result.config(text=expression)
    
def calculate():
    global expression
    result = ""
    if expression != "":
        try:
            result = eval(expression)
        except:
            result = "error"
            expression = ""
    label_result.config(text=result)
    expression = str(result)

def funcdel():
    global  expression
    expression = expression[0:len(expression)-1]
    label_result.config(text=expression)


# Create key bindings
def key_handler(event):
    global expression
    if event.keysym in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0"):
        add(event.keysym)
    elif event.keysym == "plus":
        add("+")
    elif event.keysym == "minus":
        add("-")
    elif event.keysym == "asterisk":
        add("*")
    elif event.keysym == "slash":
        add("/")
    elif event.keysym in ("c", "C"):
        clear()
    elif event.keysym == "period":
        add(".")
    elif event.keysym in ("Return", "equal"):
        calculate()
    elif event.keysym == "BackSpace":
        expression = expression[0:len(expression)-1]
        label_result.config(text=expression)
        
    
root.bind("<Key>", key_handler)
