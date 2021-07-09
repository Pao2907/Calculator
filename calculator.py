#calculator

#input from user
	#take as string, store to ans
#when equal sign is clicked, eval(ans)

def evaluate():
	try:
		ans=eval(entry)
	except ZeroDivisionError: 
		print("Math Error")
	except:
		print("Syntax Error")

	else:
		print("answer: ",ans)

#Clear all characters
def deleteAll():
	global entry
	entry=" "

#backspace
def deleteOne():
	global entry
	x = len(entry)-1
	entry = entry.replace(entry[x], ' ')
	x -= 1
	print(entry)

close = False
while close==False:
	entry = input("Enter the expression: ")
	option = input("Exit(0), delete(1), clear(2) or continue(3)?")
	if option=='1':
		deleteOne()
		evaluate()
	if option=='2':
		deleteAll()
	if option=='3':
		evaluate()
		option = input("Exit(0) or continue(3)?")
	if option=='0':
		close = True
		exit()


