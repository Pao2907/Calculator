from tkinter import*

class Calculator(Frame):
	
	#constructor for the Calculator Window
	def __init__(self, master=None):
		super().__init__(master)
		self.pack()
		self.createWidgets()
		self.new = False

		#User Input (Note: not disabled, user keys can be used)
		self.entry = Entry(self, width=35, borderwidth=0, justify="right", relief=RIDGE, fg="White", font=("Helvetica", "11", "bold"),bg="#283136")
		self.entry.grid(row=1, column=0, columnspan=4, padx=10, pady=30)
		#Expression container so user can see the expression after evaluation
		self.expr = Label(self, text=" ", width=35,padx=0,pady=8, borderwidth=0, justify="right", relief=RIDGE, fg="#798288", font=("Helvetica", "9", "bold"),bg="#283136")
		self.expr.place(relx = 1.0,rely = 0.0,anchor ='ne')

	#for numbers and operators                  
	def click(self,input):
		global new
		if self.new==True:
			self.entry.delete(0,END)
			self.new=False
		old=self.entry.get()
		self.entry.delete(0, END)
		self.entry.insert(0, old+input)
		self.expr.configure(text=self.entry.get())
		return self.entry.get()

	#for equal sign
	def evaluate(self):
		try:
			ans = self.entry.get()
			ans=eval(ans)
		except ZeroDivisionError: 
			self.entry.delete(0, END)
			self.entry.insert(0,"Math Error")
		except:
			self.entry.delete(0, END)
			self.entry.insert(0,"Syntax Error")
		else:
			self.entry.delete(0, END)
			self.entry.insert(0,ans)
		global new 
		self.new= True
		return self.new
	#Clear all characters
	def deleteAll(self):
		self.entry.delete(0, END)
		self.expr.configure(text=self.entry.get())
	#backspace
	def deleteOne(self):
		global new
		if self.new==True:
			self.entry.delete(0,END)
			self.new=False
		current=self.entry.get()
		self.entry.delete(len(current)-1, END)
		self.expr.configure(text=self.entry.get())

	#Part to create expression container and buttons
	def createWidgets(self):
