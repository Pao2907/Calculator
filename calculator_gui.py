# Create GUI
from tkinter import*

root = Tk()
root.configure(bg='#283136') 
root.minsize(304,333) 
root.maxsize(304,333) 
root.title("Calculator")

entry = Entry(root, width=35, borderwidth=0, justify="right", relief=RIDGE, fg="White", font=("Helvetica", "11", "bold"),bg="#283136")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=30)

expr = Label(root, text=" ", width=35,padx=0,pady=8, borderwidth=0, justify="right", relief=RIDGE, fg="#798288", font=("Helvetica", "9", "bold"),bg="#283136")
expr.place(relx = 1.0,rely = 0.0,anchor ='ne')

one = Button(root, justify="center", text="1", width=8, pady=10, relief=FLAT, fg="White",font=("Helvetica", "9"), bg="#44535b",activebackground='Gray')
two = Button(root, justify="center",text="2", width=8, pady=10, relief=FLAT, fg="White",font=("Helvetica", "9"), bg="#44535b",activebackground='Gray')
three = Button(root,justify="center", text="3", width=8, pady=10, relief=FLAT, fg="White",font=("Helvetica", "9"), bg="#44535b",activebackground='Gray')
four = Button(root, justify="center",text="4", width=8, pady=10, relief=FLAT, fg="White",font=("Helvetica", "9"), bg="#44535b",activebackground='Gray')
five = Button(root, justify="center",text="5", width=8, pady=10, relief=FLAT, fg="White",font=("Helvetica", "9"), bg="#44535b",activebackground='Gray')
six = Button(root, justify="center",text="6", width=8, pady=10, relief=FLAT, fg="White",font=("Helvetica", "9"), bg="#44535b",activebackground='Gray')
seven = Button(root, justify="center",text="7", width=8, pady=10, relief=FLAT, fg="White",font=("Helvetica", "9"), bg="#44535b",activebackground='Gray')
eight = Button(root, justify="center",text="8", width=8, pady=10, relief=FLAT, fg="White",font=("Helvetica", "9"), bg="#44535b",activebackground='Gray')
nine = Button(root, justify="center",text="9", width=8, pady=10, relief=FLAT, fg="White",font=("Helvetica", "9"), bg="#44535b",activebackground='Gray')
zero = Button(root, justify="center",text="0", width=8, pady=10, relief=FLAT, fg="White",font=("Helvetica", "9"), bg="#44535b",activebackground='Gray')
decimal = Button(root, justify="center",text=".", width=8, pady=10, relief=FLAT, fg="White",font=("Helvetica", "9"), bg="#44535b",activebackground='Gray')


plus = Button(root, justify="center",text="+",  width=10,pady=10, relief=FLAT, fg="White",font=("Helvetica", "9"), bg="#33434c",activebackground='Gray')
minus = Button(root, justify="center",text="-",  width=10,pady=10, relief=FLAT, fg="White",font=("Helvetica", "9"), bg="#33434c",activebackground='Gray')
times = Button(root, justify="center",text="x", width=10,pady=10, relief=FLAT, fg="White",font=("Arial", "9"), bg="#33434c",activebackground='Gray')
divide = Button(root, justify="center",text="/", width=10, pady=10, relief=FLAT, fg="White",font=("Helvetica", "9"), bg="#33434c",activebackground='Gray')
equals = Button(root, justify="center",text="=", width=10, pady=10, relief=FLAT, fg="White",font=("Helvetica", "9"), bg="Orange",activebackground='Gray')

clear = Button(root, justify="center",text="C", width=8, pady=10, relief=FLAT, fg="White",font=("Helvetica", "9"), bg="#33434c", activebackground='Gray')
delete = Button(root, justify="center",text="Del", width=8, pady=10, relief=FLAT, fg="White",font=("Helvetica", "9"), bg="#33434c",activebackground='Gray')
leftparenthesis = Button(root, justify="center",text="(", width=8, pady=10, relief=FLAT, fg="White",font=("Helvetica", "9"), bg="#33434c",activebackground='Gray')
rightparenthesis = Button(root, justify="center",text=")", width=8, pady=10, relief=FLAT, fg="White",font=("Helvetica", "9"), bg="#33434c",activebackground='Gray')


entry.insert(0,"0")

one.grid(row=4, column=0, padx=3, pady=3)
two.grid(row=4, column=1,padx=3, pady=3)
three.grid(row=4, column=2,padx=3, pady=3)
plus.grid(row=4, column=3,padx=3, pady=3)


four.grid(row=3, column=0,padx=3, pady=3)
five.grid(row=3, column=1,padx=3, pady=3)
six.grid(row=3, column=2,padx=3, pady=3)
minus.grid(row=3, column=3,padx=3, pady=3)


seven.grid(row=2, column=0,padx=3, pady=3)
eight.grid(row=2, column=1,padx=3, pady=3)
nine.grid(row=2, column=2,padx=3, pady=3)
times.grid(row=2, column=3,padx=3, pady=3)


clear.grid(row=1, column=0,padx=3, pady=3)
leftparenthesis.grid(row=1, column=1,padx=3, pady=3)
rightparenthesis.grid(row=1, column=2,padx=3, pady=3)
divide.grid(row=1, column=3,padx=3, pady=3)



zero.grid(row=5, column=1,padx=3, pady=3)
decimal.grid(row=5, column=0,padx=3, pady=3)
delete.grid(row=5, column=2,padx=3, pady=3)
equals.grid(row=5, column=3,padx=3, pady=3)



root.mainloop()
