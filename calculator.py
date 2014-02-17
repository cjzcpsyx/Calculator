import sys
from Tkinter import *

calculatorGUI = Tk()
calculatorGUI.geometry("350x400+200+200")
calculatorGUI.title("Calculator V1.0")
welcomLabel = Label(calculatorGUI, text='Welcome to calculator V1.0', fg='#447bd4').pack()

num1, num2, action, result = float(0), float(0), '', float(0)
error_message = ''

def change_number1():
	return change_number(1)
def change_number2():
	return change_number(2)
def change_number3():
	return change_number(3)
def change_number4():
	return change_number(4)
def change_number5():
	return change_number(5)
def change_number6():
	return change_number(6)
def change_number7():
	return change_number(7)
def change_number8():
	return change_number(8)
def change_number9():
	return change_number(9)
def change_number0():
	return change_number(0)

def change_number(n):
	global num1
	global num2
	global num1Label
	global num2Label
	if action == '':
		num1 = num1 * 10 + n
		num1Label.config(text = str(num1))
	else:
		num2 = num2 * 10 + n
		num2Label.config(text = str(num2))

def change_action_plus():
	return change_action('+')
def change_action_minus():
	return change_action('-')
def change_action_multiply():
	return change_action('*')
def change_action_divide():
	return change_action('/')

def change_action(act):
	global action
	global actionLabel
	action = act
	actionLabel.config(text = action)

def get_result():
	global result
	global resultLabel
	global errorLabel
	if action == '+':
		result = num1 + num2
	if action == '-':
		result = num1 - num2
	if action == '*':
		result = num1 * num2
	if action == '/':
		if num2 == 0:
			error_message = 'Cannot divide by zero!!!'
			errorLabel.config(text = error_message)
		else:
			result = num1 / num2
	resultLabel.config(text = result)

def clear():
	global num1, num2, action, result
	global num1Label, num2Label, actionLabel, resultLabel
	num1 = num2 = result = float(0)
	action = ''
	num1Label.config(text = str(num1))
	num2Label.config(text = str(num2))
	resultLabel.config(text = str(result))
	actionLabel.config(text = action)

num1Label = Label(calculatorGUI, text = str(num1))
actionLabel = Label(calculatorGUI, text = action)
num2Label = Label(calculatorGUI, text = str(num2))
resultLabel = Label(calculatorGUI, text = str(result))
errorLabel = Label(calculatorGUI, text = error_message)
num1Label.pack()
actionLabel.pack()
num2Label.pack()
resultLabel.pack()
errorLabel.pack()

button1 = Button(calculatorGUI, width = 4, text='1', command = change_number1).place(x=100, y=260)
button2 = Button(calculatorGUI, width = 4, text='2', command = change_number2).place(x=140, y=260)
button3 = Button(calculatorGUI, width = 4, text='3', command = change_number3).place(x=180, y=260)
button4 = Button(calculatorGUI, width = 4, text='4', command = change_number4).place(x=100, y=230)
button5 = Button(calculatorGUI, width = 4, text='5', command = change_number5).place(x=140, y=230)
button6 = Button(calculatorGUI, width = 4, text='6', command = change_number6).place(x=180, y=230)
button7 = Button(calculatorGUI, width = 4, text='7', command = change_number7).place(x=100, y=200)
button8 = Button(calculatorGUI, width = 4, text='8', command = change_number8).place(x=140, y=200)
button9 = Button(calculatorGUI, width = 4, text='9', command = change_number9).place(x=180, y=200)
button0 = Button(calculatorGUI, width = 10, text='0', command = change_number0).place(x=100, y=290)

button_plus = Button(calculatorGUI, width = 4, height = 3, text='+', command = change_action_plus).place(x=220, y=200)
button_minus = Button(calculatorGUI, width = 4, text='-', command = change_action_minus).place(x=220, y=170)
button_multiply = Button(calculatorGUI, width = 4, text='*', command = change_action_multiply).place(x=180, y=170)
button_divide = Button(calculatorGUI, width = 4, text='/', command = change_action_divide).place(x=140, y=170)
button_equal = Button(calculatorGUI, width = 4, height = 3, text='=', command = get_result).place(x=220, y=260)
button_clear = Button(calculatorGUI, width = 4, text = 'C', command = clear).place(x=100, y=170)



calculatorGUI.mainloop()