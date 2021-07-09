# This part are the development of Button widgets and their positioning
		self.one = Button(self, justify="center", text="1", width=8, pady=10, relief=FLAT, fg="White",font=("Helvetica", "9"), bg="#44535b",activebackground='Gray', command= lambda:self.click("1"))
		two = Button(self, justify="center",text="2", width=8, pady=10, relief=FLAT, fg="White",font=("Helvetica", "9"), bg="#44535b",activebackground='Gray',command= lambda:self.click("2"))
		three = Button(self,justify="center", text="3", width=8, pady=10, relief=FLAT, fg="White",font=("Helvetica", "9"), bg="#44535b",activebackground='Gray',command= lambda:self.click("3"))
		four = Button(self, justify="center",text="4", width=8, pady=10, relief=FLAT, fg="White",font=("Helvetica", "9"), bg="#44535b",activebackground='Gray',command= lambda:self.click("4"))
		five = Button(self, justify="center",text="5", width=8, pady=10, relief=FLAT, fg="White",font=("Helvetica", "9"), bg="#44535b",activebackground='Gray',command= lambda:self.click("5"))
		six = Button(self, justify="center",text="6", width=8, pady=10, relief=FLAT, fg="White",font=("Helvetica", "9"), bg="#44535b",activebackground='Gray',command= lambda:self.click("6"))
		seven = Button(self, justify="center",text="7", width=8, pady=10, relief=FLAT, fg="White",font=("Helvetica", "9"), bg="#44535b",activebackground='Gray',command= lambda:self.click("7"))
		eight = Button(self, justify="center",text="8", width=8, pady=10, relief=FLAT, fg="White",font=("Helvetica", "9"), bg="#44535b",activebackground='Gray',command= lambda:self.click("8"))
		nine = Button(self, justify="center",text="9", width=8, pady=10, relief=FLAT, fg="White",font=("Helvetica", "9"), bg="#44535b",activebackground='Gray',command= lambda:self.click("9"))
		zero = Button(self, justify="center",text="0", width=8, pady=10, relief=FLAT, fg="White",font=("Helvetica", "9"), bg="#44535b",activebackground='Gray',command= lambda:self.click("0"))
		decimal = Button(self, justify="center",text=".", width=8, pady=10, relief=FLAT, fg="White",font=("Helvetica", "9"), bg="#44535b",activebackground='Gray',command= lambda:self.click("."))

		plus = Button(self, justify="center",text="+",  width=10,pady=10, relief=FLAT, fg="White",font=("Helvetica", "9"), bg="#33434c",activebackground='Gray',command= lambda:self.click("+"))
		minus = Button(self, justify="center",text="-",  width=10,pady=10, relief=FLAT, fg="White",font=("Helvetica", "9"), bg="#33434c",activebackground='Gray',command= lambda:self.click("-"))
		times = Button(self, justify="center",text="x", width=10,pady=10, relief=FLAT, fg="White",font=("Arial", "9"), bg="#33434c",activebackground='Gray',command= lambda:self.click("*"))
		divide = Button(self, justify="center",text="/", width=10, pady=10, relief=FLAT, fg="White",font=("Helvetica", "9"), bg="#33434c",activebackground='Gray',command= lambda:self.click("/"))
		equals = Button(self, justify="center",text="=", width=10, pady=10, relief=FLAT, fg="White",font=("Helvetica", "9"), bg="Orange",activebackground='Gray',command= lambda:self.evaluate())

		clear = Button(self, justify="center",text="C", width=8, pady=10, relief=FLAT, fg="White",font=("Helvetica", "9"), bg="#33434c", activebackground='Gray',command= lambda:self.deleteAll())
		delete = Button(self, justify="center",text="Del", width=8, pady=10, relief=FLAT, fg="White",font=("Helvetica", "9"), bg="#33434c",activebackground='Gray',command= lambda:self.deleteOne())
		leftparen = Button(self, justify="center",text="(", width=8, pady=10, relief=FLAT, fg="White",font=("Helvetica", "9"), bg="#33434c",activebackground='Gray',command= lambda:self.click("("))
		rightparen = Button(self, justify="center",text=")", width=8, pady=10, relief=FLAT, fg="White",font=("Helvetica", "9"), bg="#33434c",activebackground='Gray',command= lambda:self.click(")"))

		self.one.grid(row=5, column=0, padx=3, pady=3)
		two.grid(row=5, column=1,padx=3, pady=3)
		three.grid(row=5, column=2,padx=3, pady=3)
		plus.grid(row=5, column=3,padx=3, pady=3)

		four.grid(row=4, column=0,padx=3, pady=3)
		five.grid(row=4, column=1,padx=3, pady=3)
		six.grid(row=4, column=2,padx=3, pady=3)
		minus.grid(row=4, column=3,padx=3, pady=3)

		seven.grid(row=3, column=0,padx=3, pady=3)
		eight.grid(row=3, column=1,padx=3, pady=3)
		nine.grid(row=3, column=2,padx=3, pady=3)
		times.grid(row=3, column=3,padx=3, pady=3)

		clear.grid(row=2, column=0,padx=3, pady=3)
		leftparen.grid(row=2, column=1,padx=3, pady=3)
		rightparen.grid(row=2, column=2,padx=3, pady=3)
		divide.grid(row=2, column=3,padx=3, pady=3)

		zero.grid(row=6, column=1,padx=3, pady=3)
		decimal.grid(row=6, column=0,padx=3, pady=3)
		delete.grid(row=6, column=2,padx=3, pady=3)
		equals.grid(row=6, column=3,padx=3, pady=3)

	def save(self, *_):
		self.destroy()

#=========================================================
root = Calculator()
root.configure(bg='#283136') 
root.master.minsize(304,333) 
root.master.maxsize(304,333) 
root.master.title("Calculator")
root.mainloop()
