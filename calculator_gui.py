# Create GUI
from tkinter import*

root = Tk()
root.configure(bg='#283136') 
root.minsize(304,333) 
root.maxsize(304,333) 
root.title("Calculator")

label_result = tkinter.Label(root, text="", font=("Arial Narrow", 16, 'bold'))
label_result.grid(row=0, column=0, columnspan=4)

button_1 = tkinter.Button(root, text="7", bg='white', command=lambda: add("7"), font=("Arial Narrow", 16, 'bold'))
button_1.grid(row=1, column=0)

button_2 = tkinter.Button(root, text="8", bg='white', command=lambda: add("8"), font=("Arial Narrow", 16, 'bold'))
button_2.grid(row=1, column=1)

button_3 = tkinter.Button(root, text="9", bg='white', command=lambda: add("9"), font=("Arial Narrow", 16, 'bold'))
button_3.grid(row=1, column=2)

button_divide = tkinter.Button(root, text="/", bg='pink', command=lambda: add("/"), font=("Arial Narrow", 16, 'bold'))
button_divide.grid(row=1, column=3)

button_4 = tkinter.Button(root, text="4", bg='white', command=lambda: add("4"), font=("Arial Narrow", 16, 'bold'))
button_4.grid(row=2, column=0)

button_5 = tkinter.Button(root, text="5", bg='white', command=lambda: add("5"), font=("Arial Narrow", 16, 'bold'))
button_5.grid(row=2, column=1)

button_6 = tkinter.Button(root, text="6", bg='white', command=lambda: add("6"), font=("Arial Narrow", 16, 'bold'))
button_6.grid(row=2, column=2)

button_multiply = tkinter.Button(root, text="*", bg='pink', command=lambda: add("*"), font=("Arial Narrow", 16, 'bold'))
button_multiply.grid(row=2, column=3)

button_7 = tkinter.Button(root, text="1", bg='white', command=lambda: add("1"), font=("Arial Narrow", 16, 'bold'))
button_7.grid(row=3, column=0)

button_8 = tkinter.Button(root, text="2", bg='white', command=lambda: add("2"), font=("Arial Narrow", 16, 'bold'))
button_8.grid(row=3, column=1)

button_9 = tkinter.Button(root, text="3", bg='white', command=lambda: add("3"), font=("Arial Narrow", 16, 'bold'))
button_9.grid(row=3, column=2)

button_subtract = tkinter.Button(root, text="-", bg='pink', command=lambda: add("-"), font=("Arial Narrow", 16, 'bold'))
button_subtract.grid(row=3, column=3)

button_0 = tkinter.Button(root, text="00", bg='white', command=lambda: add("00"), font=("Arial Narrow", 16, 'bold'))
button_0.grid(row=4, column=0)

button_0 = tkinter.Button(root, text="0", bg='white', command=lambda: add("0"), font=("Arial Narrow", 16, 'bold'))
button_0.grid(row=4, column=1)

button_dot = tkinter.Button(root, text=".", bg='white', command=lambda: add("."), font=("Arial Narrow", 16, 'bold'))
button_dot.grid(row=4, column=2)

button_add = tkinter.Button(root, text="+", bg='pink', command=lambda: add("+"), font=("Arial Narrow", 16, 'bold'))
button_add.grid(row=4, column=3)

button_clear = tkinter.Button(root, text="C", bg='pink', command=lambda: clear(), font=("Arial Narrow", 16, 'bold'))
button_clear.grid(row=5, column=1)

button_DEL =tkinter.Button(root, text="del", bg='pink', command=funcdel, font=("Arial Narrow", 16, 'bold'))
button_DEL.grid(row=5, column=2)

button_equals = tkinter.Button(root, text="=", bg='pink', width=16, command=lambda: calculate(), font=("Arial Narrow", 16, 'bold'))
button_equals.grid(row=5, column=3, columnspan=3)
